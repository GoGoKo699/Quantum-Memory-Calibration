"""Finite arithmetic checks for a calibrated passive memory construction."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, exp, isclose


def suffix_histograms(weights):
    """Count suffix strings by Hamming weight and signed Z energy."""
    suffix = [None] * (len(weights) + 1)
    suffix[-1] = [Counter({0: 1})]
    for index in range(len(weights) - 1, -1, -1):
        weight = weights[index]
        suffix[index] = [Counter() for _ in range(len(suffix[index + 1]) + 1)]
        for ones, histogram in enumerate(suffix[index + 1]):
            for energy, count in histogram.items():
                suffix[index][ones][energy + weight] += count
                suffix[index][ones + 1][energy - weight] += count
    return suffix


def spectral_band(weights, level_count):
    size = len(weights)
    sector = size // 2
    suffix = suffix_histograms(weights)
    lower_edge = -size * level_count
    band_width = 2 * size
    histogram = Counter()
    for energy, count in suffix[0][sector].items():
        index = (energy - lower_edge) // band_width
        assert 0 <= index < level_count
        histogram[index] += count
    index = min(histogram, key=lambda candidate: (-histogram[candidate], candidate))
    lower = lower_edge + index * band_width
    return suffix, lower, lower + band_width, histogram[index]


def zero_completions(suffix, index, ones, energy, lower, upper):
    if 0 <= ones < len(suffix[index + 1]):
        return sum(
            count
            for offset, count in suffix[index + 1][ones].items()
            if lower <= energy + offset < upper
        )
    return 0


def unrank(weights, suffix, lower, upper, rank):
    ones = len(weights) // 2
    energy = 0
    bits = []
    for index, weight in enumerate(weights):
        count = zero_completions(suffix, index, ones, energy + weight, lower, upper)
        bit = int(rank >= count)
        if bit:
            rank -= count
        energy += weight * (1 - 2 * bit)
        ones -= bit
        bits.append(bit)
    assert rank == ones == 0 and lower <= energy < upper
    return tuple(bits)


def rank_string(weights, suffix, lower, upper, bits):
    ones = len(weights) // 2
    energy = 0
    rank = 0
    for index, (weight, bit) in enumerate(zip(weights, bits)):
        if bit:
            rank += zero_completions(suffix, index, ones, energy + weight, lower, upper)
        energy += weight * (1 - 2 * bit)
        ones -= bit
    assert ones == 0 and lower <= energy < upper
    return rank


def verify_bands():
    cases = 0
    for size, level_count, symbols in [(1, 4, range(4)), (4, 8, [0, 2, 5, 7]),
                                        (5, 10, [0, 4, 5, 9]), (6, 12, [0, 5, 11])]:
        for indices in product(symbols, repeat=size):
            weights = tuple(2 * index + 1 - level_count for index in indices)
            suffix, lower, upper, best_count = spectral_band(weights, level_count)
            by_band = {}
            direct = Counter()
            for bits in product((0, 1), repeat=size):
                if sum(bits) != size // 2:
                    continue
                energy = sum(weight * (1 - 2 * bit) for weight, bit in zip(weights, bits))
                direct[energy] += 1
                left = ((energy + size * level_count) // (2 * size)) * 2 * size
                left -= size * level_count
                by_band.setdefault(left, []).append(bits)
            best_left = min(by_band, key=lambda candidate: (-len(by_band[candidate]), candidate))
            accepted = by_band[best_left]
            assert suffix[0][size // 2] == direct
            assert lower == best_left and best_count == len(accepted)
            assert comb(size, size // 2) <= level_count * best_count
            for rank, bits in enumerate(accepted):
                assert unrank(weights, suffix, lower, upper, rank) == bits
                assert rank_string(weights, suffix, lower, upper, bits) == rank
            cases += 1
    return cases


def verify_quantization():
    size = 4
    scale = 2
    resolution = 3
    levels = 2 * size * scale * resolution
    hold_scale = Fraction(3, 2)
    uncertainty = Fraction(7, 5)
    common_offset = Fraction(-327, 11)
    cases = 0
    for indices in product((0, levels // 2 - 1, levels // 2, levels - 1), repeat=size):
        weights = tuple(2 * index + 1 - levels for index in indices)
        suffix, lower, upper, count = spectral_band(weights, levels)
        strings = [unrank(weights, suffix, lower, upper, rank) for rank in range(count)]
        for bin_offsets in product((0, 1), repeat=size):
            couplings = tuple(common_offset + uncertainty * (Fraction(2 * (index + offset), levels) - 1)
                              for index, offset in zip(indices, bin_offsets))
            energies = [hold_scale * sum(g * (1 - 2 * bit) for g, bit in zip(couplings, bits))
                        / uncertainty for bits in strings]
            assert max(energies) - min(energies) <= Fraction(2, resolution)
            cases += 1
    return cases


class BinaryField:
    def __init__(self, degree, modulus):
        self.size = 1 << degree
        self.modulus = modulus

    def mul(self, left, right):
        result = 0
        while right:
            if right & 1:
                result ^= left
            right >>= 1
            left <<= 1
            if left & self.size:
                left ^= self.modulus
        return result

    def inv(self, value):
        assert value
        result = 1
        for _ in range(self.size - 2):
            result = self.mul(result, value)
        return result

    def evaluate(self, polynomial, point):
        result = 0
        for coefficient in reversed(polynomial):
            result = self.mul(result, point) ^ coefficient
        return result

    def solve(self, matrix, width):
        """Return one solution of an augmented system, including singular systems."""
        matrix = [row[:] for row in matrix]
        pivots = []
        for column in range(width):
            row = len(pivots)
            pivot = next((candidate for candidate in range(row, len(matrix))
                          if matrix[candidate][column]), None)
            if pivot is None:
                continue
            matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
            scale = self.inv(matrix[row][column])
            matrix[row] = [self.mul(value, scale) for value in matrix[row]]
            for candidate, values in enumerate(matrix):
                if candidate != row and values[column]:
                    scale = values[column]
                    matrix[candidate] = [value ^ self.mul(scale, pivot_value)
                                         for value, pivot_value in zip(values, matrix[row])]
            pivots.append(column)
        if any(not any(row[:-1]) and row[-1] for row in matrix):
            return None
        solution = [0] * width
        for row, column in enumerate(pivots):
            solution[column] = matrix[row][-1]
        return solution

    def powers(self, point, highest):
        values = [1]
        for _ in range(highest):
            values.append(self.mul(values[-1], point))
        return values

    def interpolate(self, points, values):
        matrix = [self.powers(point, len(points) - 1) + [value]
                  for point, value in zip(points, values)]
        return self.solve(matrix, len(points))

    def decode(self, points, received, dimension, radius):
        """Decode a stripe by solving the monic Welch–Berlekamp system."""
        numerator_size = dimension + radius
        system = []
        for point, value in zip(points, received):
            powers = self.powers(point, numerator_size - 1)
            system.append(powers + [self.mul(value, power) for power in powers[:radius]]
                          + [self.mul(value, powers[radius])])
        solution = self.solve(system, numerator_size + radius)
        if solution is None:
            return None

        numerator = solution[:numerator_size]
        locator = solution[numerator_size:] + [1]
        quotient = [0] * dimension
        for index in range(dimension - 1, -1, -1):
            quotient[index] = numerator[index + radius]
            for shift, value in enumerate(locator):
                numerator[index + shift] ^= self.mul(quotient[index], value)
        if any(numerator):
            return None
        codeword = tuple(self.evaluate(quotient, point) for point in points)
        if sum(left != right for left, right in zip(codeword, received)) > radius:
            return None
        return codeword


def verify_stripe(field, length, dimension, radius):
    points = tuple(range(length))
    codewords = [tuple(field.evaluate(polynomial, point) for point in points)
                 for polynomial in product(range(field.size), repeat=dimension)]
    errors = [values for values in product(range(field.size), repeat=length)
              if sum(bool(value) for value in values) <= radius]
    syndromes = {}
    for error in errors:
        prefix_fit = field.interpolate(points[:dimension], error[:dimension])
        representative = tuple(value ^ field.evaluate(prefix_fit, point)
                               for value, point in zip(error, points))
        assert not any(representative[:dimension])
        assert representative not in syndromes or syndromes[representative] == error
        syndromes[representative] = error
        decoded = field.decode(points, representative, dimension, radius)
        assert decoded is not None
        assert tuple(left ^ right for left, right in zip(representative, decoded)) == error

    covered = set()
    for codeword in codewords:
        for error in errors:
            received = tuple(left ^ right for left, right in zip(codeword, error))
            assert received not in covered
            covered.add(received)
            assert field.decode(points, received, dimension, radius) == codeword
            prefix_fit = field.interpolate(points[:dimension], received[:dimension])
            representative = tuple(value ^ field.evaluate(prefix_fit, point)
                                   for value, point in zip(received, points))
            assert syndromes[representative] == error

    for received in product(range(field.size), repeat=length):
        if received not in covered:
            assert field.decode(points, received, dimension, radius) is None
    return len(covered), field.size ** length


def greedy_binary_code(length, dimension, distance):
    codewords = [0]
    for _ in range(dimension):
        generator = next(
            candidate
            for candidate in range(1 << length)
            if all((candidate ^ word).bit_count() >= distance for word in codewords)
        )
        codewords += [word ^ generator for word in codewords]
    return codewords


def verify_concatenated_outer():
    field = BinaryField(2, 0b111)
    points = (0, 1, 2)
    inner_length = 5
    inner_codes = greedy_binary_code(inner_length, 2, 3)
    assert min((left ^ right).bit_count() for left, right in combinations(inner_codes, 2)) == 3

    def decode_inner(received):
        within_radius = [symbol for symbol, codeword in enumerate(inner_codes)
                         if (received ^ codeword).bit_count() <= 1]
        assert len(within_radius) <= 1
        return within_radius[0] if within_radius else 0

    def decode_outer(received):
        mask = (1 << inner_length) - 1
        symbols = tuple(decode_inner((received >> (pos * inner_length)) & mask)
                        for pos in range(len(points)))
        return field.decode(points, symbols, 1, 1)

    length = len(points) * inner_length
    cases = 0
    for data in range(field.size):
        stripe = (data,) * len(points)
        encoded = sum(inner_codes[symbol] << (pos * inner_length)
                      for pos, symbol in enumerate(stripe))
        for weight in range(4):
            for positions in combinations(range(length), weight):
                noise = sum(1 << bit for bit in positions)
                assert decode_outer(encoded ^ noise) == stripe
                cases += 1
    return cases


def gaussian_characteristic(argument):
    return exp(-argument * argument / 2)


def verify_correlated_twirl():
    gaps = (0.28, -0.39)
    labels = tuple(product((0, 1), repeat=2))
    energies = {label: sum(bit * gap for bit, gap in zip(label, gaps)) for label in labels}
    probabilities = {}
    for mask in labels:
        total = 0.0
        for left in labels:
            for right in labels:
                parity = sum(bit * (a ^ b) for bit, a, b in zip(mask, left, right))
                total += (-1) ** parity * gaussian_characteristic(energies[left] - energies[right])
        probabilities[mask] = total / len(labels) ** 2

    assert min(probabilities.values()) >= 0
    assert isclose(sum(probabilities.values()), 1)
    marginal_a = probabilities[1, 0] + probabilities[1, 1]
    marginal_b = probabilities[0, 1] + probabilities[1, 1]
    assert isclose(marginal_a, (1 - gaussian_characteristic(gaps[0])) / 2)
    assert isclose(marginal_b, (1 - gaussian_characteristic(gaps[1])) / 2)
    assert 0 <= marginal_a <= gaps[0] ** 2 / 4
    assert 0 <= marginal_b <= gaps[1] ** 2 / 4
    joint = probabilities[1, 1]
    joint_formula = 1 - sum(gaussian_characteristic(gap) for gap in gaps)
    joint_formula += (gaussian_characteristic(sum(gaps))
                      + gaussian_characteristic(gaps[0] - gaps[1])) / 2
    assert isclose(joint, joint_formula / 4)
    assert joint > marginal_a * marginal_b

    for left in labels:
        for right in labels:
            difference = tuple(a ^ b for a, b in zip(left, right))
            from_shifts = 0.0
            for shift in labels:
                shifted_left = tuple(a ^ b for a, b in zip(left, shift))
                shifted_right = tuple(a ^ b for a, b in zip(right, shift))
                from_shifts += gaussian_characteristic(energies[shifted_left] - energies[shifted_right])
            from_shifts /= len(labels)
            from_paulis = sum(probability * (-1) ** sum(a * b for a, b in zip(mask, difference))
                              for mask, probability in probabilities.items())
            assert isclose(from_shifts, from_paulis)
    return joint, marginal_a * marginal_b


def main():
    cases = verify_bands()
    quantized = verify_quantization()
    stripe_four = verify_stripe(BinaryField(2, 0b111), 3, 1, 1)
    stripe_eight = verify_stripe(BinaryField(3, 0b1011), 5, 3, 1)
    concatenated = verify_concatenated_outer()
    joint, product_marginals = verify_correlated_twirl()
    print(f"Signed fixed-weight bands and rank/unrank: {cases} exhaustive profile cases")
    print(f"Calibration-cell corner spectra: {quantized} exact rational checks")
    print(f"GF(4) [3,1,3] stripe: {stripe_four[0]} correctable words among {stripe_four[1]} tested")
    print(f"GF(8) [5,3,3] stripe: {stripe_eight[0]} correctable words among {stripe_eight[1]} tested")
    print(f"Binary [5,2,3] plus GF(4) [3,1,3]: {concatenated} exhaustive message-pattern pairs")
    print(f"Common-phase twirl: joint error {joint:.8f}, product of marginals {product_marginals:.8f}")


if __name__ == "__main__":
    main()

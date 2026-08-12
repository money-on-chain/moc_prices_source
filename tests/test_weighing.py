import unittest
from decimal import Decimal

from moc_prices_source.weighing import weighted_median


class WeightedMedianTests(unittest.TestCase):

    def test_empty_input_returns_none(self):
        """Empty values and weights return None."""
        self.assertIsNone(weighted_median([], []))

    def test_single_value_returns_that_value(self):
        """A single value is returned unchanged."""
        self.assertEqual(weighted_median([42], [1]), 42)

    def test_values_without_weights_are_rejected(self):
        """Values without matching weights raise ValueError."""
        with self.assertRaises(ValueError):
            weighted_median([10, 20], [])

    def test_two_equally_weighted_values_return_their_average(self):
        """Two equally weighted values return their arithmetic average."""
        self.assertEqual(weighted_median([10, 20], [0.5, 0.5]), 15)

    def test_two_unequally_weighted_values_return_weighted_average(self):
        """Two values use both weights when calculating their average."""
        self.assertEqual(weighted_median([10, 20], [0.8, 0.2]), 12)

    def test_two_unsorted_values_keep_weights_attached(self):
        """Sorting two values preserves each value-to-weight association."""
        self.assertEqual(weighted_median([20, 10], [0.2, 0.8]), 12)

    def test_odd_equal_weight_input_returns_middle_value(self):
        """An odd number of equally weighted values returns the middle value."""
        self.assertEqual(weighted_median([30, 10, 20], [1, 1, 1]), 20)

    def test_even_input_returns_weighted_average_of_middle_values(self):
        """Four values return the weighted average of the two middle values."""
        result = weighted_median(
            [10.0, 20.0, 40.0, 1_000.0],
            [0.1, 0.3, 0.5, 0.1],
        )

        # (20 * 0.3 + 40 * 0.5) / (0.3 + 0.5) = 32.5
        self.assertEqual(result, 32.5)

    def test_zero_weight_value_is_ignored(self):
        """A zero-weight outlier does not affect the result."""
        self.assertEqual(
            weighted_median([10, 20, 1_000], [0.5, 0.5, 0.0]),
            15,
        )

    def test_zero_weight_value_with_different_type_is_ignored(self):
        """A disabled value does not constrain the active values' type."""
        result = weighted_median(
            [Decimal('10'), 999],
            [Decimal('1'), Decimal('0')],
        )

        self.assertEqual(result, Decimal('10'))
        self.assertIsInstance(result, Decimal)

    def test_decimal_input_preserves_decimal_type(self):
        """Decimal inputs produce a Decimal result without losing precision."""
        result = weighted_median(
            [Decimal('10.1'), Decimal('20.2')],
            [Decimal('0.5'), Decimal('0.5')],
        )

        self.assertEqual(result, Decimal('15.15'))
        self.assertIsInstance(result, Decimal)

    def test_dominant_first_weight_does_not_wrap_to_last_value(self):
        """A dominant lowest value is returned without wrapping to the highest."""
        result = weighted_median(
            [10, 20, 30, 1_000],
            [0.6, 0.2, 0.1, 0.1],
        )

        self.assertEqual(result, 10)

    def test_dominant_interior_weight_returns_its_value(self):
        """A dominant interior source is returned without blending a neighbor."""
        result = weighted_median(
            [10, 20, 30, 40],
            [0.1, 0.6, 0.2, 0.1],
        )

        self.assertEqual(result, 20)

    def test_dominant_interior_weight_is_found_after_sorting(self):
        """A dominant interior source is found when the input is unsorted."""
        result = weighted_median(
            [40, 20, 10, 30],
            [0.1, 0.6, 0.1, 0.2],
        )

        self.assertEqual(result, 20)

    def test_dominant_last_weight_does_not_wrap_to_first_value(self):
        """A dominant highest value is returned without wrapping to the lowest."""
        result = weighted_median(
            [10, 20, 30, 1_000],
            [0.1, 0.1, 0.2, 0.6],
        )

        self.assertEqual(result, 1_000)

    def test_dominant_highest_value_is_found_after_sorting(self):
        """A dominant highest value is found when the input is unsorted."""
        result = weighted_median(
            [30, 1_000, 10, 20],
            [0.2, 0.6, 0.1, 0.1],
        )

        self.assertEqual(result, 1_000)


if __name__ == '__main__':
    unittest.main()

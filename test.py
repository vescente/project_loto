import unittest
from loto import generate_unique_numbers, Card

class TestLoto(unittest.TestCase):

    def setUp(self):
        self.testlen = 80
        self.testmin = 0
        self.testmax = 100

    def test_generate_unique_numbers_length(self):
        actual = generate_unique_numbers(self.testlen, self.testmin, self.testmax)
        self.assertEqual(len(actual), self.testlen)

    def test_generate_unique_numbers_values(self):
        actual = generate_unique_numbers(self.testlen, self.testmin, self.testmax)
        for item in actual:
            self.assertTrue(self.testmin <= item <= self.testmax)

    def test_generate_unique_numbers_uniqueness(self):
        actual = generate_unique_numbers(self.testlen, self.testmin, self.testmax)
        self.assertEqual(len(set(actual)), self.testlen)

    def test_generate_unique_numbers_max_possible_count(self):
        max_possible_len = 101
        actual = generate_unique_numbers(max_possible_len, self.testmin, self.testmax)
        self.assertEqual(len(actual), max_possible_len)

    def test_card_initialization(self):
        card = Card()
        self.assertEqual(len(card._data), card._rows * card._cols)
        self.assertEqual(sum(1 for num in card._data if num != card._empty_value), card._rows * card._nums_in_row)

    def test_card_contains(self):
        card = Card()
        number = card._data[0]
        self.assertIn(number, card)
        self.assertNotIn(999, card)

    def test_card_cross_number(self):
        card = Card()
        number = card._data[0]
        card.cross_number(number)
        self.assertEqual(card._data[0], card._crossed_value)

    def test_card_is_closed(self):
        card = Card()
        for number in card._data:
            if number != card._empty_value:
                card.cross_number(number)
        self.assertTrue(card.is_closed())

if __name__ == '__main__':
    unittest.main()
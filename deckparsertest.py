from deckparser import *
import unittest

class TestDeckParser(unittest.TestCase):

	def test_deck(self):
		deck = DeckParser("sample_input.txt").deck
		deck_length = 45

		self.assertEqual(len(deck), deck_length)

		for card in set(deck):
			self.assertTrue(deck.count(card) <= 3)
			self.assertTrue(deck.count(card) > 0)

	def test_draw(self):
		deck_parser = DeckParser("sample_input.txt")
		one = deck_parser.draw()
		ten = deck_parser.draw(num_cards=10)

		self.assertEqual(len(one), 1)
		self.assertEqual(len(ten), 10)

	def test_sample_hand(self):
		deck_parser = DeckParser("sample_input.txt")
		hand = deck_parser.sample_hand()

		self.assertEqual(len(hand), 5)

if __name__ == '__main__':
	unittest.main()

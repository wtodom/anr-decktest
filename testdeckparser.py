from deckparser import *
import unittest

class TestDeckParser(unittest.TestCase):

	def test_deck(self):
		deck = DeckParser("sample_input.txt").deck
		deck_length = len(deck)

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

	def test_repeated_sample_hands(self):
		deck_parser = DeckParser("sample_input.txt")
		deck_length = len(deck_parser.deck)
		for i in range(10):
			deck_parser.sample_hand()
			# if this passes ten times then the cards are being replaced.
			self.assertEqual(len(deck_parser.deck), deck_length - 5)

	def test_deck_reset(self):
		deck_parser = DeckParser("sample_input.txt")
		deck_length = len(deck_parser.full_deck)
		deck_parser.draw(num_cards=4)
		self.assertEqual(len(deck_parser.deck), 41)
		deck_parser.reset_deck()
		self.assertEqual(len(deck_parser.deck), deck_length)

if __name__ == '__main__':
	unittest.main()

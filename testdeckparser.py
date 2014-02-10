from deckparser import *
import unittest

class TestDeckParser(unittest.TestCase):

	def test_deck(self):
		deck = DeckParser("netrunnerdb_sample.txt").deck
		deck_length = len(deck)

		self.assertEqual(len(deck), deck_length)

		for card in set(deck):
			self.assertTrue(deck.count(card) <= 3)
			self.assertTrue(deck.count(card) > 0)

	def test_draw(self):
		deck_parser = DeckParser("netrunnerdb_sample.txt")
		one = deck_parser.draw()
		ten = deck_parser.draw(num_cards=10)

		self.assertEqual(len(one), 1)
		self.assertEqual(len(ten), 10)

	def test_sample_hand(self):
		deck_parser = DeckParser("netrunnerdb_sample.txt")
		hand = deck_parser.sample_hand()

		self.assertEqual(len(hand), 5)

	def test_repeated_sample_hands(self):
		deck_parser = DeckParser("netrunnerdb_sample.txt")
		deck_length = len(deck_parser.deck)
		for i in range(10):
			deck_parser.sample_hand()
			# if this passes ten times then the cards are being replaced.
			self.assertEqual(len(deck_parser.deck), deck_length - 5)

	def test_deck_reset(self):
		deck_parser = DeckParser("netrunnerdb_sample.txt")
		deck_length = len(deck_parser.full_deck)
		deck_parser.draw(num_cards=4)
		self.assertEqual(len(deck_parser.deck), 41)
		deck_parser.reset_deck()
		self.assertEqual(len(deck_parser.deck), deck_length)

	def test_unique_cards(self):
		deck_parser = DeckParser("netrunnerdb_sample.txt")
		cards = deck_parser.unique_cards()
		self.assertEqual(len(cards), len(set(cards)))
		for card in cards:
			self.assertTrue(card in set(deck_parser.full_deck))

	def test_full_deck(self):
		deck_parser = DeckParser("netrunnerdb_sample.txt")
		full_deck = deck_parser.full_deck
		num_cards = len(set(full_deck))
		card_list = deck_parser.cards_with_count()
		self.assertEqual(num_cards, len(card_list))
		for card in card_list:
			card_name = card[3::]
			card_count = int(card[0])
			self.assertTrue(full_deck.count(card_name) == card_count)

if __name__ == '__main__':
	unittest.main()

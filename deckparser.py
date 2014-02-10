from __future__ import print_function

import copy, random, re


class DeckParser:

	def __init__(self, infile):
		self.regexpr = " (.*?) \("
		self.infile = infile
		self.hand_size = 5
		self.deck = self.parse_input()
		self.full_deck = copy.deepcopy(self.deck)
		self.deck_size = len(self.full_deck)

	def parse_input(self):
		with open(self.infile, "r") as f:
			lines = f.readlines()
		cards = []
		for line in lines:
			if "andromeda" in line.lower():
				self.hand_size = 9
			if line[0].isdigit():
				for i in range(int(line[0])):  # between 1 and 3, inclusive
					card = re.findall(self.regexpr, line)
					cards.append(card[0])
		random.shuffle(cards)
		return cards

	def sample_hand(self):
		if len(self.deck) != self.deck_size:
			self.reset_deck()
		self.shuffle()
		return self.draw(num_cards=self.hand_size)

	def draw(self, num_cards=1):
		remaining = len(self.deck)
		if num_cards > remaining:
			print("Cannot draw {} cards - only {} left in deck.".format(num_cards, remaining))
			return []
		else:
			return [self.deck.pop() for i in range(num_cards)]

	def reset_deck(self):
		self.deck = copy.deepcopy(self.full_deck)

	def shuffle(self):
		random.shuffle(self.deck)

	def unique_cards(self):
		return set(self.full_deck)

	def cards_with_count(self):
		card_list = []
		for card in self.unique_cards():
			card_count = self.full_deck.count(card)
			card_list.append(str(card_count) + "x " + card)
		return card_list

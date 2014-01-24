import copy, random, re

class DeckParser:

	def __init__(self, infile):
		self.regexpr = " (.*?) \("
		self.infile = infile
		self.deck = self.parse_input()
		self.full_deck = copy.deepcopy(self.deck)
		self.deck_size = len(self.full_deck)

	def parse_input(self):
		with open(self.infile, "r") as f:
			lines = f.readlines()
		cards = []
		for line in lines:
			if line[0].isdigit():
				for i in range(int(line[0])):  # between 1 and 3, inclusive
					card = re.findall(self.regexpr, line)
					cards.append(card[0])
		random.shuffle(cards)
		return cards

	def sample_hand(self):
		if len(self.deck) != self.deck_size:
			self.reset_deck()
		random.shuffle(self.deck)
		return self.draw(num_cards=5)

	def draw(self, num_cards=1):
		return [self.deck.pop() for i in range(num_cards)]

	def reset_deck(self):
		self.deck = copy.deepcopy(self.full_deck)

	def shuffle(self):
		random.shuffle(self.deck)

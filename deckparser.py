import re

class DeckParser:

	def __init__(self, infile):
		self.regexpr = "x (.*?) \("
		self.infile = infile
		self.deck = self.parse_input()

	def parse_input(self):
		with open(self.infile, "r") as f:
			lines = f.readlines()
		cards = []
		for line in lines:
			if line[0].isdigit():
				for i in range(int(line[0])):  # between 1 and 3, inclusive
					card = re.findall(self.regexpr, line)
					cards.append(card[0])
		return cards

	def sample_hand(self):
		pass

	def draw(self, num_cards=1):
		pass

	def validate_deck(self):
		pass
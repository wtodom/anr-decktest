import re

class DeckParser:

	def __init__(self, text):
		self.regexpr = "x (.*?) \("
		self.plaintext = text
		self.full_deck = self.parse_input()
		self.deck = self.full_deck

	def parse_input(self):
		cards = []
		for line in self.plaintext:
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
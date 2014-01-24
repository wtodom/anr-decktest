from deckparser import *

with open("sample_input.txt", "r") as f:
	deck = f.readlines()
	d = DeckParser(deck)
	for card in d.full_deck:
		print(card)

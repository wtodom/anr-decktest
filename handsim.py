from deckparser import *


d = DeckParser("sample_input.txt")
for card in d.full_deck:
	print(card)

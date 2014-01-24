import sys
from deckparser import *


def main_menu(deck):
	print()
	print("1) Draw sample starting hand")
	print("2) Draw card")
	print("3) Draw multiple cards")
	print("4) Shuffle deck")
	print("5) Reset deck")
	print("6) Exit")
	print()

	choice = input(">> ")

	if choice == "1":
		for card in deck.sample_hand():
			print(card)
	elif choice == "2":
		print(deck.draw())
	elif choice == "3":
		print("How many cards?")
		num = input(">> ")
		for card in deck.draw(num_cards=num):
			print(card)
	elif choice == "4":
		deck.shuffle()
	elif choice == "5":
		deck.reset()
	elif choice == "6":
		print("Bye!")
		sys.exit()
	else:
		print("Invalid selection. Please choose one of the above options.")

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 {} (textfile)".format(__name__))
		sys.exit()
	dp = DeckParser(sys.argv[1])

	while True:
		main_menu(dp)

if __name__ == '__main__':
	main()

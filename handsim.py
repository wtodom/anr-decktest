from __future__ import print_function
from deckparser import *

import sys


v = sys.version_info
if v < (3, 0):
	input = raw_input

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
	print()

	if choice == "1":
		print("Sample hand:")
		for card in deck.sample_hand():
			print(card)
	elif choice == "2":
		print("You drew:")
		print(deck.draw()[0])
	elif choice == "3":
		num = get_num_cards()
		print()
		print("You drew:")
		for card in deck.draw(num_cards=num):
			print(card)
	elif choice == "4":
		deck.shuffle()
		print("Your deck has been shuffled.")
	elif choice == "5":
		deck.reset_deck()
		print("Your deck has been reset.")
	elif choice == "6":
		print("Bye!")
		sys.exit()
	else:
		print("Invalid selection. Please choose one of the above options.")

def get_num_cards():
	print("How many cards?")
	num = input(">> ")
	try:
		num = int(num)
	except:
		print("Invalid input - must enter an integer.")
		get_num_cards()
	return int(num)

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 {} (textfile)".format(__name__))
		sys.exit()
	dp = DeckParser(sys.argv[1])

	while True:
		main_menu(dp)

if __name__ == '__main__':
	main()

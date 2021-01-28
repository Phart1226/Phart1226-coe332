# file to read in animals.json and print one animal at random to screen
import json
import random

with open('animals.json', 'r') as f:
	animals = json.load(f)
	spot = random.randint(0,19)
	print(f"This animal has a head of a {animals['animals'][spot]['head']},")
	print(f"a body of a {animals['animals'][spot]['body']},")
	print(f"{animals['animals'][spot]['arms']} arms,")
	print(f"{animals['animals'][spot]['legs']} legs,")
	print(f"and {animals['animals'][spot]['tail']} tails.")

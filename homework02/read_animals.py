#!/usr/bin/env python3
import json
import random
import sys

# generate the average of a given body part from the list of animals
def avg_body_part(animals_list, body_part):
    avg_bp = 0

    for animal in animals_list:
        avg_bp += int(animal[body_part])
    
    return avg_bp / float(len(animals_list))		

def main():

    with open(sys.argv[1], 'r') as f:
        animal_dict = json.load(f)
        animals = animal_dict['animals']
        avg_arms = avg_body_part(animals, 'arms')
        avg_legs = avg_body_part(animals, 'legs')
        avg_tails = avg_body_part(animals, 'tail')

	 
        print(random.choice(animals))
        print('Average number of arms:', avg_arms)
        print('Average number of legs:', avg_legs)
        print('Average number of tails:', avg_tails)

if __name__ == '__main__':
    main()

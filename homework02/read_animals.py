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
        rand_ani = random.choice(animals)
        avg_arms = avg_body_part(animals, 'arms')
        avg_legs = avg_body_part(animals, 'legs')
        avg_tails = avg_body_part(animals, 'tail')
        
        print()
        print('The random animal has the head of a', rand_ani['head'])
        print('A body of a(n)', rand_ani['body'][0:rand_ani['body'].find('-')], 'and a(n)', rand_ani['body'][rand_ani['body'].find('-') + 1 : len(rand_ani['body'])])
        print(rand_ani['arms'], 'arms')
        print(rand_ani['legs'], 'legs')
        print('And', rand_ani['tail'], 'tails')
        print()
        print('Body Part Averages for the Whole List of Animals:')
        print('Arms:', avg_arms)
        print('Legs:', avg_legs)
        print('Tails:', avg_tails)

if __name__ == '__main__':
    main()

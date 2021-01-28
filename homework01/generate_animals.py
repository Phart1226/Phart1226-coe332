#file to generate 20 distinct animals and write them into animals.json
import petname
import random
import json

animals = {}
animals['animals'] = []
animalList = ['snake', 'bull', 'lion', 'raven', 'bunny']

while (len(animals['animals']) < 20):
	arms = random.randrange(2,11,2)
	legs = random.randrange(3,13,3)
	animals['animals'].append({'head':animalList[random.randint(0,4)], 'body': petname.Name()+ '-' + petname.Name(), 'arms':arms, 'legs':legs, 'tail': arms+legs})

with open('animals.json', 'w') as out:
	json.dump(animals, out, indent=2)
	


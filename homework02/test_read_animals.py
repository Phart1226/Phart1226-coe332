#!/usr/bin/env python3
import unittest
from read_animals import avg_body_part

class TestReadAnimals(unittest.TestCase):
	
	
	def test_avg_body_part(self):   
		animals = [{'head': 'bull', 'body' : 'sheep-bunny', 'arms' : 2, 'legs' : 12, 'tail' : 14}, {'head' : 'snake', 'body' : 'parrot-bream', 'arms' : 6, 'legs' : 6, 'tail' : 12}]
		self.assertEqual(avg_body_part(animals, 'arms'), 4.0)
		self.assertEqual(avg_body_part(animals, 'legs'), 9.0)
		self.assertEqual(avg_body_part(animals, 'tail'), 13.0)
		self.assertRaises(TypeError, avg_body_part, 'hello', 'tails')
		self.assertRaises(KeyError, avg_body_part, animals, 'feet')	

if __name__ == '__main__':
    unittest.main()

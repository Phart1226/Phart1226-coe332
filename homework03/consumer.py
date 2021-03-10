import json
import requests

# grab all aniamls in the json file
response_anim = requests.get(url="http://localhost:5012/animals")

# grab all animals in json file that have 4 arms
response_arms = requests.get(url="http://localhost:5012/animals/arms/?arms=4")

# grab all animals in json file that have head of a raven
response_head = requests.get(url="http://localhost:5012/animals/head/?head=raven")

# print each response
print('ALL ANIMALS:')
print(response_anim.json())
print()

print('ANIMALS WITH 4 ARMS:')
print(response_arms.json())
print()

print('ANIMALS WITH A RAVEN HEAD')
print(response_head.json())
print()

import json
import requests

# reset database
response_setDB = requests.get(url="http://10.104.201.42:5000/animals/reset")

# grab all animals in db
response_animals = requests.get(url="http://10.104.201.42:5000/animals")

# grab all animal uuids
response_keys = requests.get(url="http://10.104.201.42:5000/animals/keys")

# grab animal with a specific UUID
#response_uuid = requests.get(url="http://10.104.201.42:5000/animals/uuid/?uuid=130bb2f6-558b-44b1-afed-c7f4adbddb27")

# update an animals stats given its UUID
#response_update = requests.get(url="http://10.104.201.42:5000/animals/update/?uuid=130bb2f6-558b-44b1-afed-c7f4adbddb27&head=snake&legs=23&tail=32")


# grab all animals in json file that are within the startDate and endDate
p = {'startDate':'2014-01-01', 'endDate':'2021-01-01'}
response_dates = requests.get(url="http://10.104.201.42:5000/animals/dates/", params = p)

# get average legs per animal
response_legs = requests.get(url="http://10.104.201.42:5000/animals/legs")

# get count of animals in database
response_count = requests.get(url="http://10.104.201.42:5000/animals/count")


# print reset database message
print('RESETTING DATABASE...')
print(response_setDB.content)
print()

# print all animals in db
print('ALL ANIMALS')
print(response_animals.json())
print()

# print reset database message
print('ANIMAL UUIDS')
print(response_keys.json())
print()

print('ANIMAL WITH UUID')
#print(response_uuid.json())
print()

print('ANIMALS WITHIN A DATE RANGE')
print(response_dates.json())
print()

print('AVERAGE NUM LEGS PER ANIMAL')
print(response_legs.content)
print()

print('NUMBER OF ANIMALS')
print(response_count.content)
print()

print('UPDATED ANIMAL')
#print(response_update.json())
print()



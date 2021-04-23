# Midterm Project

For the midterm project, the goal was to containerize an instance of a redis server as well as an updated Flask app. By interacting together, predefined routes within the Flask app query the redis database, pull, and manipulate stored animals.   

## Building the Flask app and Redis Container

After cloning and navigating into the midterm folder, build the container by running the following command:

```bash
docker-compose -p phart_midTerm up --build
```

This runs the dockerfile and creates an instance of a redis server and makes the Flask app python files accessible within the container.

## Querying the Routes in App.py

From within the web directory of the midterm folder, run:

```bash
python3 consumer.py 
```

This file contains 7 predefined GET commands to query the redis database where the animal data is stored.

Below is an example of the output from this command:


```bash
[phart@isp02 web]$ python3 consumer.py
ALL ANIMALS
[{'head': 'snake', 'body': 'shrew-rhino', 'arms': 6, 'legs': 12, 'tail': 18, 'created_on': '2001-01-29'}, {'head': 'bull', 'body': 'moray-gator', 'arms': 4, 'legs': 6, 'tail': 10, 'created_on': '2008-12-14'}, {'head': 'raven', 'body': 'sawfly-wahoo', 'arms': 2, 'legs': 12, 'tail': 14, 'created_on': '2014-12-29'}, {'head': 'lion', 'body': 'husky-oryx', 'arms': 6, 'legs': 3, 'tail': 9, 'created_on': '2015-08-11'}, {'head': 'raven', 'body': 'jackal-fawn', 'arms': 8, 'legs': 12, 'tail': 20, 'created_on': '2016-10-24'}, {'head': 'bunny', 'body': 'drum-quail', 'arms': 4, 'legs': 6, 'tail': 10, 'created_on': '2006-05-06'}, {'head': 'snake', 'body': 'yak-bass', 'arms': 6, 'legs': 3, 'tail': 9, 'created_on': '2014-11-14'}, {'head': 'bull', 'body': 'coyote-man', 'arms': 4, 'legs': 9, 'tail': 13, 'created_on': '2018-05-24'}, {'head': 'raven', 'body': 'quail-salmon', 'arms': 2, 'legs': 3, 'tail': 5, 'created_on': '2014-05-22'}, {'head': 'lion', 'body': 'stag-cougar', 'arms': 6, 'legs': 3, 'tail': 9, 'created_on': '2016-05-20'}, {'head': 'snake', 'body': 'gannet-snake', 'arms': 8, 'legs': 3, 'tail': 11, 'created_on': '2012-01-23'}, {'head': 'lion', 'body': 'pony-gannet', 'arms': 6, 'legs': 9, 'tail': 15, 'created_on': '2008-09-20'}, {'head': 'snake', 'body': 'pig-poodle', 'arms': 6, 'legs': 12, 'tail': 18, 'created_on': '2010-08-29'}, {'head': 'lion', 'body': 'tapir-deer', 'arms': 2, 'legs': 9, 'tail': 11, 'created_on': '2007-12-01'}, {'head': 'lion', 'body': 'horse-moth', 'arms': 8, 'legs': 9, 'tail': 17, 'created_on': '2005-08-30'}, {'head': 'lion', 'body': 'gnat-louse', 'arms': 6, 'legs': 3, 'tail': 9, 'created_on': '2020-11-21'}, {'head': 'bunny', 'body': 'mantis-bison', 'arms': 10, 'legs': 3, 'tail': 13, 'created_on': '2007-05-23'}, {'head': 'raven', 'body': 'mako-prawn', 'arms': 8, 'legs': 6, 'tail': 14, 'created_on': '2018-07-22'}, {'head': 'bull', 'body': 'jackal-mako', 'arms': 4, 'legs': 3, 'tail': 7, 'created_on': '2008-05-26'}, {'head': 'lion', 'body': 'mullet-mammal', 'arms': 4, 'legs': 9, 'tail': 13, 'created_on': '2008-09-07'}]

ANIMAL UUIDS
{'1': "b'73dfca19-9b4e-48f3-92ab-7c8f49ebec73'", '2': "b'a7f8d3a4-cff6-409c-b33c-907c11b7d3a9'", '3': "b'73c5fb88-b454-4c58-941c-d7b16a72b4ae'", '4': "b'e63b0700-4bd6-4712-83fd-c6a94aa7fc7d'", '5': "b'148d12cb-1f34-4d83-96e2-d19293861f3a'", '6': "b'13a29310-4136-4023-b52b-4dd408e25ee1'", '7': "b'8debbe4d-855a-4063-933a-d2cd4c024fbb'", '8': "b'd25edbd4-2b64-4d63-b42a-d075557fdc58'", '9': "b'130bb2f6-558b-44b1-afed-c7f4adbddb27'", '10': "b'c84b37a7-c559-439a-8e2e-a9e66c137a05'", '11': "b'15a73c37-ef17-46ad-afa0-18f11a2c3e1b'", '12': "b'fae8949f-0627-432b-af5e-18d3efcf2134'", '13': "b'21db2357-5cb8-4b54-9447-2599afad846a'", '14': "b'24e11ad1-81be-4fe2-a088-db08d3adbb2c'", '15': "b'753f25c9-614d-4d06-b9cb-c2100860e314'", '16': "b'875f7a20-e96a-4573-ab14-f96aa84218cf'", '17': "b'3651721b-2fe5-49b8-b632-2db1d7dfe180'", '18': "b'f6a0f814-a395-4547-9c8e-c6f6c4df6829'", '19': "b'0e4099cf-968d-411a-886d-f28d6744eb0a'", '20': "b'cde73d23-d6d1-4b27-a373-f269ab032939'"}

ANIMAL WITH UUID
{'head': 'raven', 'body': 'quail-salmon', 'arms': 2, 'legs': 3, 'tail': 5, 'created_on': '2014-05-22'}

ANIMALS WITHIN A DATE RANGE
[{'head': 'raven', 'body': 'sawfly-wahoo', 'arms': 2, 'legs': 12, 'tail': 14, 'created_on': '2014-12-29'}, {'head': 'lion', 'body': 'husky-oryx', 'arms': 6, 'legs': 3, 'tail': 9, 'created_on': '2015-08-11'}, {'head': 'raven', 'body': 'jackal-fawn', 'arms': 8, 'legs': 12, 'tail': 20, 'created_on': '2016-10-24'}, {'head': 'snake', 'body': 'yak-bass', 'arms': 6, 'legs': 3, 'tail': 9, 'created_on': '2014-11-14'}, {'head': 'bull', 'body': 'coyote-man', 'arms': 4, 'legs': 9, 'tail': 13, 'created_on': '2018-05-24'}, {'head': 'snake', 'body': 'quail-salmon', 'arms': 2, 'legs': '23', 'tail': '32', 'created_on': '2014-05-22'}, {'head': 'lion', 'body': 'stag-cougar', 'arms': 6, 'legs': 3, 'tail': 9, 'created_on': '2016-05-20'}, {'head': 'lion', 'body': 'gnat-louse', 'arms': 6, 'legs': 3, 'tail': 9, 'created_on': '2020-11-21'}, {'head': 'raven', 'body': 'mako-prawn', 'arms': 8, 'legs': 6, 'tail': 14, 'created_on': '2018-07-22'}]

AVERAGE NUM LEGS PER ANIMAL
b'7.75'

NUMBER OF ANIMALS
b'20'

UPDATED ANIMAL
{'head': 'snake', 'body': 'quail-salmon', 'arms': 2, 'legs': '23', 'tail': '32', 'created_on': '2014-05-22'}
```

ALL ANIMALS: a list of all the current animals and their stats stored in the redis database

ANIMAL UUIDS: a list of all the uuids for each animal in the redis database. These are also the keys used to uniquely store each animal in the database.

ANIMAL WITH UUID: Returns the animal with the UUID that is predefined in the route to grab a specific animal from the database. A different UUID can be queried using the following command:

```bash
curl localhost:5012/animals/uuid/?uuid==<uuid>
```

ANIMALS WITHIN A DATE RANGE: a list of all animals that were created within 2014 and 2021. This a predefined range within consumer.py. A different range can be queried using the following curl command:

```bash
curl localhost:5012/animals/dates/?startDate=<yyyy-mm-dd>&endDate=<yyyy-mm-dd>
```

ANIMALS NUM LEGS PER ANIMAL: query to get the average number of legs per animal in the database

NUMBER OF ANIMALS: query to get the number of animals in the database

UPDATED ANIMAL: updates an animal given a uuid and animal stats, returns the updated animal, and updates the animal in the database. The output returns the predefined animal with predefined stats to update in the route, however a different animal can be update by the following curl command:

```bash
curl localhost:5012/animals/update/?uuid=<uuid>&<stat>=<updated stat>
```

## Resetting the Database With New Animals

```bash
curl localhost:5012/animals/reset
```

If this command runs successfully, a sucessful run message outputs


# Homework03

For this homework assignment, the goal is to extract qualified animals from an animals.json datafile using GET requests to ping a flask app running locally on the isp machine. The extraction qualifications have been predefined within consumers.py. 

## Building the Flask app

After cloning and navigating into the homework03 folder, build the flask app by running the following command:

```bash
docker build -t "flask-hw03-hart" .
```

## Running the Flask app Locally on the ISP Machine

```bash
 docker run --name "preston-hw03" -d -p 5012:5000 flask-hw03-hart
```

---
**NOTE**

If the previous command produces an error then this Flask app is already running on port 5012 and does not need to be rebuilt or reran.

---

## Running the consumer.py file to extact animals from animals.json

From within the homework03 directory, run:

```bash
python3 consumer.py
``` 

```bash
[phart@isp02 homework03]$ python3 consumer.py
ALL ANIMALS:
{'animals': [{'arms': 4, 'body': 'buck-satyr', 'head': 'raven', 'legs': 9, 'tail': 13}, {'arms': 4, 'body': 'tomcat-squid', 'head': 'bunny', 'legs': 6, 'tail': 10}, {'arms': 10, 'body': 'guinea-lion', 'head': 'bull', 'legs': 6, 'tail': 16}, {'arms': 8, 'body': 'kiwi-spider', 'head': 'snake', 'legs': 12, 'tail': 20}, {'arms': 10, 'body': 'serval-whale', 'head': 'bunny', 'legs': 9, 'tail': 19}, {'arms': 4, 'body': 'crane-boar', 'head': 'snake', 'legs': 12, 'tail': 16}, {'arms': 4, 'body': 'asp-perch', 'head': 'bull', 'legs': 6, 'tail': 10}, {'arms': 10, 'body': 'oriole-burro', 'head': 'bunny', 'legs': 3, 'tail': 13}, {'arms': 4, 'body': 'turkey-gnat', 'head': 'raven', 'legs': 6, 'tail': 10}, {'arms': 6, 'body': 'imp-weasel', 'head': 'raven', 'legs': 9, 'tail': 15}, {'arms': 2, 'body': 'iguana-boar', 'head': 'raven', 'legs': 9, 'tail': 11}, {'arms': 10, 'body': 'robin-hippo', 'head': 'bunny', 'legs': 12, 'tail': 22}, {'arms': 10, 'body': 'wahoo-viper', 'head': 'snake', 'legs': 9, 'tail': 19}, {'arms': 2, 'body': 'roughy-worm', 'head': 'bunny', 'legs': 6, 'tail': 8}, {'arms': 8, 'body': 'dove-goat', 'head': 'raven', 'legs': 9, 'tail': 17}, {'arms': 4, 'body': 'swine-whale', 'head': 'raven', 'legs': 9, 'tail': 13}, {'arms': 2, 'body': 'owl-tetra', 'head': 'raven', 'legs': 9, 'tail': 11}, {'arms': 2, 'body': 'gator-wasp', 'head': 'snake', 'legs': 6, 'tail': 8}, {'arms': 4, 'body': 'oryx-perch', 'head': 'snake', 'legs': 12, 'tail': 16}, {'arms': 6, 'body': 'asp-poodle', 'head': 'snake', 'legs': 12, 'tail': 18}]}

ANIMALS WITH 4 ARMS:
[{'body': 'buck-satyr', 'head': 'raven', 'legs': 9, 'tail': 13, 'arms': 4}, {'body': 'tomcat-squid', 'head': 'bunny', 'legs': 6, 'tail': 10, 'arms': 4}, {'body': 'crane-boar', 'head': 'snake', 'legs': 12, 'tail': 16, 'arms': 4}, {'body': 'asp-perch', 'head': 'bull', 'legs': 6, 'tail': 10, 'arms': 4}, {'body': 'turkey-gnat', 'head': 'raven', 'legs': 6, 'tail': 10, 'arms': 4}, {'body': 'swine-whale', 'head': 'raven', 'legs': 9, 'tail': 13, 'arms': 4}, {'body': 'oryx-perch', 'head': 'snake', 'legs': 12, 'tail': 16, 'arms': 4}]

ANIMALS WITH A RAVEN HEAD
[{'body': 'buck-satyr', 'head': 'raven', 'legs': 9, 'tail': 13, 'arms': 4}, {'body': 'turkey-gnat', 'head': 'raven', 'legs': 6, 'tail': 10, 'arms': 4}, {'body': 'imp-weasel', 'head': 'raven', 'legs': 9, 'tail': 15, 'arms': 6}, {'body': 'iguana-boar', 'head': 'raven', 'legs': 9, 'tail': 11, 'arms': 2}, {'body': 'dove-goat', 'head': 'raven', 'legs': 9, 'tail': 17, 'arms': 8}, {'body': 'swine-whale', 'head': 'raven', 'legs': 9, 'tail': 13, 'arms': 4}, {'body': 'owl-tetra', 'head': 'raven', 'legs': 9, 'tail': 11, 'arms': 2}]
```
## Stop the Running Flask app

To see all the currently running Flask apps on the server, run the following command:

```bash
docker ps -a
```

Find the app that is running on port 5012 and copy the container ID

Run the following command, pasting in the copied container ID:

```bash
docker stop <container ID>
```

## Remove the Stopped Flask app

To remove the stopped Flask app permanently from the server, run the following command, pasting in the previously copied container ID

```bash
docker rm <container ID>
```



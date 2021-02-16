# Homework02

For this homework assignment a list of 20 random animals and their individual characteristics are generated. A tool was created to pick one animal at random and print out its characteristics. A newly added feature of the tool calcualtes and prints out the average number of arms, legs, and tails from all the animals in the list.

## Download and Run Scripts Directly

After cloning and navigating into the homework02 folder, generate animals.json by running the command:

```bash
python3 generate_animals.py animals.json
```

To utilize the tool and generate output from the list of animals, run the command:

```bash
python3 read_animals.py animals.json
```

## Build an image with the Dockerfile

From within the homework02 directory, run:

```bash
docker build -t phart26/json-parser:0.1 .
``` 

## Running the Scripts in the Container

To generate the animals.json file, run:

```bash
docker-compose run gen-anim       # generates a new file in the test subfolder
```

To utilize the tool and see the new body part averages feature, run:

```bash
docker-compose run read-ani       # generates output
```

## Running the Unit Tests

The unit tests have been containerized to make the running procedure simplier.
The command below tests assert calls to the function avg\_body\_part(), testing the
simple average calcualtion the function performs as well as its ability to catch a TypeError and KeyError 

```bash
docker-compose run test-anim
```


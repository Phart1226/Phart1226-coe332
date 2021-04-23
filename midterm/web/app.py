from flask import Flask, request
import petname
import random
import json 
import uuid
import datetime
import redis

app = Flask(__name__)
rd = redis.StrictRedis(host='redis', port=6379, db=0)
# test route
@app.route('/', methods = ['GET'])
def helloworld():
    return "Hello World!!! Coming to you from a docker container"

# returns all animal entries in the the database
@app.route('/animals', methods= ['GET'])
def get_animals():
     animals = []
     for key in rd.keys():
         animals.append(json.loads(rd.get(key).decode('utf-8')))


     return json.dumps(animals)

# returns all animal UUIDs
@app.route('/animals/keys', methods= ['GET'])
def get_animal_keys():
     animals = {}
     count = 1
     for key in rd.keys():
         animals[str(count)] = str(key)
         count += 1

     return json.dumps(animals)

# return an animal given its UUID
@app.route('/animals/uuid/', methods= ['GET'])
def get_ani():
     id_ani = request.args.get('uuid')
     return json.dumps(json.loads(rd.get(id_ani).decode('utf-8')))

# return average number of legs per animal
@app.route('/animals/legs', methods= ['GET'])
def get_legs():
     animals = []
     avg_legs = 0
     
     for key in rd.keys():
         animals.append(json.loads(rd.get(key).decode('utf-8')))
     
     for animal in animals:
         avg_legs += int(animal['legs'])

     return str(avg_legs / 20.0)

# return number of animals in db
@app.route('/animals/count', methods= ['GET'])
def get_count():
     return str(len(rd.keys()))

# update an animals characteristics given an UUID and stats
# the stats coming in are individual parameters
@app.route('/animals/update/', methods= ['GET'])
def update_ani():
     id_ani = request.args.get('uuid')
     params = request.args
     animal = json.loads(rd.get(id_ani).decode('utf-8'))

     # iterate through the keys in params and change those stats in the animal
     for key in params:
         # force loop to not add uuid to the current stats
         if key == 'uuid':
             continue

         animal[key] = params[key]

     # update the db with the new animal
     rd.set(id_ani, json.dumps(animal))
     

     return json.dumps(animal)

# return all animals created between a range of dates
@app.route('/animals/dates/', methods= ['GET'])    
def get_ani_dates():
     start_date = datetime.datetime.strptime(request.args.get('startDate'), '%Y-%m-%d')
     end_date = datetime.datetime.strptime(request.args.get('endDate'), '%Y-%m-%d') 
     animals = []
     animals_dates = []
     
     # finds all animals in db
     for key in rd.keys():
         animals.append(json.loads(rd.get(key).decode('utf-8')))

     # finds all animals that were created within the range of dates
     for animal in animals:
         create_on = datetime.datetime.strptime(animal['created_on'], '%Y-%m-%d')
         if (create_on >= start_date) and (create_on <= end_date):
             animals_dates.append(animal)        

     return json.dumps(animals_dates)

@app.route('/animals/reset', methods= ['GET'])
def reset_db():
    # clears current db entries
    rd.flushdb()
    
      
    for i in range(20):
        
        # generating a random date between 2000 and 2021
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date(2021, 2, 1)
        time_between= end_date - start_date
        days_between = time_between.days
        random_num_days = random.randrange(days_between)
        
        this_animal = {}
        id_ani = str(uuid.uuid4())
        this_animal['head'] = random.choice(['snake', 'bull', 'lion', 'raven', 'bunny'])
        this_animal['body'] = petname.name() + '-' + petname.name()
        this_animal['arms'] = random.randint(1,5) * 2
        this_animal['legs'] = random.randint(1,4) * 3
        this_animal['tail'] = this_animal['legs'] + this_animal['arms']
        this_animal['created_on'] = str(start_date + datetime.timedelta(days=random_num_days))

        # add animal to redis db with uuid as key and animal list as value
        rd.set(id_ani, json.dumps(this_animal))
       
    return 'Successfully cleared the database and entered in 20 new animals'




     
# the next statement should always appear at the bottom of your flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

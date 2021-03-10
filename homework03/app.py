from flask import Flask, request
import petname
import random
import json 

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def helloworld():
    return "Hello World!!! Coming to you from a docker container"

@app.route('/animals', methods= ['GET'])
def gen_anim():
     animals = []
     with open('/app/animals.json', 'r') as json_file:
          animals = json.load(json_file)

     return animals

@app.route('/animals/arms/', methods= ['GET'])
def get_arms():
     arms = request.args.get('arms')
     animals = gen_anim()
     ani_arms = [animal for animal in animals["animals"] if animal["arms"] == int(arms)]
     
     return json.dumps(ani_arms)
 
@app.route('/animals/head/', methods= ['GET'])    
def get_head():
     head = request.args.get('head')
     animals = gen_anim()
     ani_head = [animal for animal in animals["animals"] if animal["head"] == head]
     
     return json.dumps(ani_head)


     
# the next statement should always appear at the bottom of your flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

from flask import Flask
import petname
import random

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def helloworld():
    return "Hello World!!! Coming to you from a docker container"
@app.route('/animal', methods= ['GET'])
def gen_anim():
     this_animal = {}
     this_animal['head'] = random.choice(['snake', 'bull', 'lion', 'raven', 'bunny'])
     this_animal['body'] = petname.name() + '-' + petname.name()
     this_animal['arms'] = random.randint(1,5) * 2
     this_animal['legs'] = random.randint(1,4) * 3
     this_animal['tail'] = this_animal['legs'] + this_animal['arms']

     print_str = 'Head:' + str(this_animal['head']) + ', Body:' + str(this_animal['body']) + ', Arms:' + str(this_animal['arms']) + ', Legs:' + str(this_animal['arms']) + ', Tails:' + str(this_animal['tail']) + '\n'

     return print_str

# the next statement should always appear at the bottom of your flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

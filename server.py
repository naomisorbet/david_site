import random

from flask import Flask
app = Flask(__name__)

def get_saying():
    sayings = ["bumble bees", "while you were sleeping", "hot tea",             "slippers", "caulk", "cold feet"]
    return random.choice(sayings)

@app.route("/")
def index():
    return "<h1> %s </h1>" % get_saying()
    
if __name__ == "__main__": # i.e. if we're running this file directly, as
# opposed to through a module
    app.run(debug=True)
    
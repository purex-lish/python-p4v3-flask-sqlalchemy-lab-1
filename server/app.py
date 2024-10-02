# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>')
def get_earthquake(id):
    earthquake = Earthquake.query.get(id)
    if earthquake is None:
        #return 404 error
        return make_response('{"message": "Earthquake ' + str(id) + ' not found."}', 404, {'Content-Type': 'application/json'})
    #Return the earthquake details in JSON format if found
    response_data = {
        "id": earthquake.id,
        "location": earthquake.location,
        "magnitude": earthquake.magnitude,
        "year" : earthquake.year
    }
    #manually create a JSON string
    return make_response(str(response_data).replace("'", '"'), 200, {'Content-Type': 'application/json'})

@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

    quakes_data = [{
        "id": quake.id,
        "location": quake.location,
        "magnitude": quake.magnitude,
        "year": quake.year
                           
        } for quake in quakes]
    
    response_data = {
        "count": len(quakes_data),
        "quakes": quakes_data
    }


     # Manually create a JSON string
    json_response = str(response_data).replace("'", '"')
    return make_response(json_response, 200, {'Content-Type': 'application/json'})



if __name__ == '__main__':
    app.run(port=5555, debug=True)

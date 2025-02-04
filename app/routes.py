from flask import Blueprint, jsonify, abort, request, make_response
from app import db
from app.models.planet import Planet
from app.models.moon import Moon

# class Planet():
#     def __init__(self, id, name, description, moon_count):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moon_count = moon_count
        
# planets = [
#     Planet(1, "mercury", "partly molten or liquid", 0),
#     Planet(2, "Venus", "brightest planet", 0),
#     Planet(3, "Earth", "habitable planet", 1),
# ]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["POST"])

def handle_planets():
    request_data = request.get_json()
    
    new_planet = Planet.get_from_dictionary(request_data)

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been successfully created!", 201)

@planet_bp.route("", methods=["GET"])
def get_planets():
    name_query = request.args.get("name")
    moon_query = request.args.get("moon_count")
    description_query = request.args.get("description")

    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    elif moon_query and description_query:
        planets = Planet.query.filter_by(moon_count=int(moon_query), description=description_query)
    else:
        planets = Planet.query.all()

    planets_response = []
    for planet in planets:
        planets_response.append(planet.create_dictionary())

    return jsonify(planets_response)

# Get one planet
@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return planet.create_dictionary(), 200

# Update one planet
@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
        planet = validate_planet(planet_id)
        request_data = request.get_json()
        planet.name = request_data["name"]
        planet.description = request_data["description"]
        planet.moon_count = request_data["moon_count"]
        
        db.session.commit()
        
        return make_response(f"Planet {planet.name} has been successfully updated.", 200)


# Delete one planet
@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    
    db.session.delete(planet)
    db.session.commit()
    
    return make_response(f"Planet {planet.name} has been successfully deleted.", 200)
    

def validate_planet(planet_id):
    try: 
        planet_id = int(planet_id)
    except:
        abort(make_response({"message": f"planet #{planet_id} is not valid"}, 400))
        
    planet = Planet.query.get(planet_id)
    if not planet:
        abort(make_response({"message": f"planet #{planet_id} is not found"}, 404))

    return planet   


moon_bp = Blueprint("moon", __name__, url_prefix="/moons")

@moon_bp.route("", methods=["POST"])
def create_moon():
    request_data = request.get_json()
    
    new_moon = Moon(
        name=request_data["name"] 
        )

    db.session.add(new_moon)
    db.session.commit()

    return make_response(f"Moon {new_moon.name} has been successfully created!", 201)

@moon_bp.route("", methods=["GET"])
def read_moons():
    moons = Moon.query.all()

    moons_response = []
    for moon in moons:
        moons_response.append(
            {
            "id": moon.id,
            "name": moon.name
            }
        )

    return jsonify(moons_response)

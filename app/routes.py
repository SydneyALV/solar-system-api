from flask import Blueprint

class Planet():
    def __init__(self, id, name, description, moon_count):
        self.id = id
        self.name = name
        self.description = description
        self.moon_count = moon_count
        
planets= [
    Planet(1, "mercury", "partly moltenor liquid", 0),
    Planet(2, "Venus", "brightest planet", 0),
    Planet(3, "Earth", "habitable planet", 1),
]

planets_bp = Blueprint("planets", __name__, url_prefix= "/planets")
@planets_bp.route("", methods= ["GET"])

def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(planet)
    return planets_response
        



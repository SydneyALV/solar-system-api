from flask import Blueprint, jsonify

class Planet():
    def __init__(self, id, name, description, moon_count):
        self.id = id
        self.name = name
        self.description = description
        self.moon_count = moon_count
        
planets = [
    Planet(1, "mercury", "partly moltenor liquid", 0),
    Planet(2, "Venus", "brightest planet", 0),
    Planet(3, "Earth", "habitable planet", 1),
]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])

def handle_planets():
    planets_response = []
    
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moon count": planet.moon_count
        })
    
    return jsonify(planets_response)
        



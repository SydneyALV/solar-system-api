from flask import Blueprint, jsonify, abort, request, make_response
from app import db
from app.models.planet import Planet

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["POST"])

def handle_planets():
    request_data = request.get_json()
    
    new_planet = Planet(
        name = request_data["name"],
        description = request_data["description"],
        moon_count = request_data["moon_count"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been successfully created!", 201)

@planet_bp.route("", methods=["GET"])

def get_planets():
    planets_response = []

    planets = Planet.query.all()

    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moon_count": planet.moon_count
        }
        )

    return jsonify(planets_response)

# @planet_bp.route("/<planet_id>", methods=["DELETE"])

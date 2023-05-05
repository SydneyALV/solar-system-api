from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moon_count = db.Column(db.Integer)

    def create_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "moon_count": self.moon_count
        }

    @classmethod
    def get_from_dictionary(cls, planet_data):
        new_planet = cls(
            name=planet_data["name"],
            description=planet_data["description"],
            moon_count=planet_data["moon_count"]
        )
        return new_planet
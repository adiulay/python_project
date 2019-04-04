from flask import Flask, request
from maple_story import MapleStory
from magician import Magician
from warrior import Warrior
import json

app = Flask(__name__)

SERVER_DB = 'maple_story.sqlite'

character_manager = MapleStory(SERVER_DB)

@app.route('/characters', methods=['POST'])
def add_character():
    """Adds a character to the MapleStory"""
    info = request.json
    try:
        if info['level'] > 200:
            response = app.response_class(
                response=str('Level should not be greater than 200'),
                status=400
            )
            return response
    except:
        response = app.response_class(
            response=str('Input Numbers only'),
            status=400
        )
        return response

    try:
        if info['job'] == 'Warrior':
            character = Warrior(
                info['name'],
                info['job'],

                info['level'],

                info['health'],
                info['health_regeneration'],

                info['attack_damage'],
                info['magic_damage'],

                info['armor'],
                info['magic_resist'],

                info['sword'],
                info['skill_ability']
            )
            character.add_health()
            character.add_armor()
            character.add_attack_damage()
            character_manager.add(character)
            response = app.response_class(
                status=200,
                response='Warrior Class has been added!'
            )
            return response
        elif info['job'] == 'Magician':
            character = Magician(
                info['name'],
                info['job'],

                info['level'],

                info['health'],
                info['health_regeneration'],

                info['attack_damage'],
                info['magic_damage'],

                info['armor'],
                info['magic_resist'],

                info['wand'],
                info['spell_cast']
            )
            character.add_magic_damage()
            character.add_health_regeneration()
            character.add_magic_resist()
            character_manager.add(character)

            response = app.response_class(
                status=200,
                response='Magician Class has been added!'
            )
            return response

    except ValueError as e:
        response = app.response_class(
            response=str('Your error: {}'.format(e)),
            status=400
        )
        return response
    except KeyError as e:
        response = app.response_class(
            response=str('Missing Key: {}'.format(e)),
            status=400
        )
        return response

@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    """Delete an existing student from the Student Manager"""

    if id < 0:
        response = app.response_class(
            status=400
        )
        return response

    try:
        character_manager.delete(id)

        response = app.response_class(
            status=200,
            response=str('Character ID: {} deleted'.format(id))
        )
        return response

    except ValueError as e:
        status_code = 400

        if str(e) == "Character ID: {} does not exist".format(id):
            status_code = 404

        response = app.response_class(
            response=str(e),
            status=status_code
        )
        return response





if __name__ == '__main__':
    app.run()
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

    for character in character_manager.get_all():
        if character.get_name() == info['name']:
            response = app.response_class(
                status=404,
                response=str('Name already in used')
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

        if info['job'] == 'Magician':
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
    """Delete an existing character from the Character Manager"""

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

@app.route('/characters/<int:id>', methods=['PUT'])
def update_character(id):
    """Updates an Existing Character"""
    info = request.json

    if id == 0:
        response = app.response_class(
            status=400,
            response=str('ID cannot be less than or equal to 0')
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

            character.id = id
            character_manager.update(character)
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

            character.id = id
            character_manager.update(character)

        response = app.response_class(
            status=200,
            response='Character id: {}, has been updated!'.format(id)
        )
    except ValueError as e:
        status_code = 400

        if str(e) == "Invalid Character Object":
            status_code = 404

        response = app.response_class(
            response=str(e),
            status=status_code
        )
    except KeyError as e:
        response = app.response_class(
            response=str('Missing Key: {}'.format(e)),
            status=400
        )

    return response

@app.route('/characters/all', methods=['GET'])
def get_all_characters():
    """Gets all characters in the Character Manager"""

    characters = character_manager.get_all()

    character_list = []

    for character in characters:
        character_list.append(character.to_dict())

    response = app.response_class(
        status=200,
        response=json.dumps(character_list),
        mimetype='application/json'
    )

    return response

@app.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    """Gets an existing character in the Character Manager"""

    if id == 0:
        response = app.response_class(
            status=400
        )
        return response

    try:
        character = character_manager.get(id)

        character_tostring = character.to_dict()

        response = app.response_class(
            status=200,
            response=json.dumps(character_tostring),
            mimetype='application/json'
        )
    except ValueError as e:
        response = app.response_class(
            status=404,
            response=str(e),
            mimetype='application/json'
        )
    except AttributeError as e:
        response = app.response_class(
            status=400,
            response=str('Character ID: {}, Does not exist'.format(id)),
            mimetype='application/json'
        )

    return response

@app.route('/characters/<type>', methods=['GET'])
def get_character_by_type(type):
    """Gets the character by type from database"""

    characters_type = character_manager.get_all_by_type(type)

    character_list = []

    if characters_type is None:
        response = app.response_class(
            status=200,
            response=str('Job type: {}, does not exist'.format(type))
        )
        return response
    else:
        for character in characters_type:
            character_list.append(character.to_dict())

    response = app.response_class(
        status=200,
        response=json.dumps(character_list),
        mimetype='application/json'
    )
    return response



if __name__ == '__main__':
    app.run()
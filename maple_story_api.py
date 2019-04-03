from flask import Flask, request
from maple_story import MapleStory
from magician import Magician
from warrior import Warrior
import json

app = Flask(__name__)

server = MapleStory('Windia.json')

@app.route('/maplestory/character', methods=['POST'])
def add_character():
    """adds new character to maplestory"""
    info = request.json

    try:
        if server.character_exist(info['ID']) is True:
            response = app.response_class(
                response="Character ID: {} already existed".format(info['ID']),
                status=400
            )
            return response

        else:
            if info['Job'] == 'Warrior':
                warrior = Warrior(info["ID"], info['Name'], info['Health']['Health'], info['Health']['Health Regeneration'],
                                  info['Offense']['Attack Damage'], info['Offense']['Magic Damage'], info['Defense']['Armor'],
                                  info['Defense']['Magic Resist'], info['Sword Name'])

                warrior.set_experience_info(info['Level']['Experience'])
                warrior.add_armor()
                warrior.add_attack_damage()
                warrior.add_health()
                warrior.set_special_skill(info['Ultimate Skill'])

                server.add(warrior)

            elif info['Job'] == 'Magician':
                magician = Magician(info["ID"], info['Name'], info['Health']['Health'], info['Health']['Health Regeneration'],
                                    info['Offense']['Attack Damage'], info['Offense']['Magic Damage'], info['Defense']['Armor'],
                                    info['Defense']['Magic Resist'], info['Wand Name'])

                magician.set_experience_info(info['Level']['Experience'])
                magician.add_health_regeneration()
                magician.add_magic_damage()
                magician.add_magic_resist()
                magician.set_spellcast(info['Special Cast'])

                server.add(magician)

        response = app.response_class(
            response='Character ID <{}> created!'.format(info['ID']),
            status=200
        )
        return response
    except ValueError:
        response = app.response_class(
            response="Character is invalid",
            status=400
        )
        return response
    except KeyError:
        response = app.response_class(
            response='KeyError: Missing/Invalid Input',
            status=400
        )
        return response

@app.route('/maplestory/character/<entity_id>', methods=['PUT'])
def update_character(entity_id):
    info = request.json
    try:
        if info['Job'] == 'Warrior':
            warrior = Warrior(info["ID"], info['Name'], info['Health']['Health'], info['Health']['Health Regeneration'],
                              info['Offense']['Attack Damage'], info['Offense']['Magic Damage'],
                              info['Defense']['Armor'],
                              info['Defense']['Magic Resist'], info['Sword Name'])

            warrior.set_experience_info(info['Level']['Experience'])
            warrior.add_armor()
            warrior.add_attack_damage()
            warrior.add_health()
            warrior.set_special_skill(info['Ultimate Skill'])

            if str(info['ID']) == entity_id:
                server.update(warrior)

        elif info['Job'] == 'Magician':
            magician = Magician(info["ID"], info['Name'], info['Health']['Health'],
                                info['Health']['Health Regeneration'], info['Offense']['Attack Damage'],
                                info['Offense']['Magic Damage'], info['Defense']['Armor'],
                                info['Defense']['Magic Resist'], info['Wand Name'])

            magician.set_experience_info(info['Level']['Experience'])
            magician.add_health_regeneration()
            magician.add_magic_damage()
            magician.add_magic_resist()
            magician.set_spellcast(info['Special Cast'])

            if str(info['ID']) == entity_id:
                server.update(magician)
            else:
                response = app.response_class(
                    response='Character does not exist',
                    status=404
                )
                return response

        response = app.response_class(
            response='Character ID <{}> updated!'.format(info['ID']),
            status=200
        )
        return response
    except ValueError:
        response = app.response_class(
            response="Character is invalid",
            status=400
        )
        return response
    except KeyError:
        response = app.response_class(
            response='KeyError: Missing/Invalid Input',
            status=400
        )
        return response

@app.route('/maplestory/character/delete/<entity_id>', methods=['DELETE'])
def delete_character(entity_id):
    counter = 0

    try:
        for character in server.get_all():
            if character.get_id() == int(entity_id):
                counter += 1
                server.delete(int(entity_id))
                response = app.response_class(
                    status=200,
                    response='Character ID <{}> Deleted'.format(entity_id)
                )
                return response
        if counter == 0:
            response = app.response_class(
                status=404,
                response='Character Does Not Exist'
            )
            return response
    except ValueError:
        response = app.response_class(
            response="Character is invalid",
            status=400
        )
        return response
    except KeyError:
        response = app.response_class(
            response='KeyError: Missing/Invalid Input',
            status=400
        )
        return response

@app.route('/maplestory/character/<entity_id>', methods=['GET'])
def get_character_by_id(entity_id):
    all_characters = server.get_all()

    cart = []

    try:
        for character in all_characters:
            if character.get_id() == int(entity_id):
                cart.append(character.to_dict())

        if len(cart) > 0:
            response = app.response_class(
                status=200,
                response=json.dumps(cart),
                mimetype='application/json'
            )
            return response
        else:
            response = app.response_class(
            status=404,
            response='Character ID: <{}> does not exist'.format(entity_id)
            )
            return response
    except ValueError:
        response = app.response_class(
            response="Character is invalid",
            status=400
        )
        return response

@app.route('/maplestory/character/all', methods=['GET'])
def get_all():
    """Returns all the info as a list of objects character records"""
    all_characters = server.get_all()

    cart = []

    for character in all_characters:
        cart.append(character.to_dict())

    response = app.response_class(
        status=200,
        response=json.dumps(cart),
        mimetype='application/json'
    )

    return response

@app.route('/maplestory/character/all/<type>', methods=['GET'])
def get_all_by_type(type):
    """returns a list of characters by type"""
    all_characters = server.get_all()

    type_list = []

    for character in all_characters:
        if character.get_type() == type:
            type_list.append(character.to_dict())

    if len(type_list) > 0:
        response = app.response_class(
            status=200,
            response=json.dumps(type_list),
            mimetype='application/json'
        )
        return response
    else:
        response = app.response_class(
             status=400,
            response="Type: <{}> Does not exist in the server".format(type),
            mimetype='application/json'
        )
        return response

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request
from maple_story import MapleStory
from magician import Magician
from warrior import Warrior
import json

app = Flask(__name__)

SERVER_DB = 'maple_story.sqlite'

character_manager = MapleStory(SERVER_DB)

@app.route('/character_list', methods=['POST'])
def add_character():
    """Adds a character to the MapleStory"""
    info = request.json

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
            character_manager.add(character)
            response = app.response_class(
                status=200,
                response='Warrior Class has beed added!'
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
            character_manager.add(character)

            response = app.response_class(
                status=200,
                response='Magician has been added!'
            )
            return response

    # except ValueError as e:
    #     response = app.response_class(
    #         response=str(e),
    #         status=400
    #     )
    #     return response
    except KeyError as e:
        response = app.response_class(
            response=str('Missing Key: {}'.format(e)),
            status=400
        )
        return response



if __name__ == '__main__':
    app.run()
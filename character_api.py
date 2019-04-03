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
        if info['Job'] == 'Warrior':
            character = Warrior(
                info['Name'],
                info['Job'],

                info['Level'],

                info['Sword Name'],
                info['Ultimate Skill'],

                info['Health'],
                info['Health Regeneration'],

                info['Attack Damage'],
                info['Magic Damage'],

                info['Armor'],
                info['Magic Resist'],
            )
            character_manager.add(character)
            response = app.response_class(
                status=200,
                response='Warrior Class has beed added!'
            )
            return response
        elif info['Job'] == 'Magician':
            character = Magician(
                info['Name'],
                info['Job'],

                info['Level'],

                info['Health'],
                info['Health Regeneration'],

                info['Attack Damage'],
                info['Magic Damage'],

                info['Armor'],
                info['Magic Resist'],

                info['Wand Name'],
                info['Special Cast'],
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
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from abstract_character import AbstractCharacter
from magician import Magician
from warrior import Warrior
import os


class MapleStory():
    def __init__(self, db_filename):
        """initializes and constructs the object through database"""
        MapleStory._validate_string_input('File path', db_filename)

        engine = create_engine('sqlite:///{}'.format(db_filename))

        Base = declarative_base()

        Base.metadata.bind = engine

        self._db_session = sessionmaker(bind=engine)

    def add(self, character):
        """Adds an object id to the session and assigns"""

        MapleStory._validate_string_input('Object', character)

        if character is None or not isinstance(character, AbstractCharacter):
            raise ValueError('Invalid Character Object')

        session = self._db_session()

        session.add(character)
        session.commit()

        character_id = character.id

        session.close()

        return character_id

    def get(self, id: int):
        """Retrieves an id from the session by utilizing queries"""

        MapleStory._validate_int_exists('Input', id)

        session = self._db_session()

        existing_warrior = session.query(Warrior).filter(Warrior.id == id, Warrior.job == 'Warrior').first()
        existing_magician = session.query(Magician).filter(Magician.id == id, Magician.job == 'Magician').first()

        session.close()

        if existing_magician != None:
            return existing_magician

        if existing_warrior != None:
            return existing_warrior

        session.close()

    def get_all(self):
        """Returns a list of all character objects from database session"""

        session = self._db_session()

        existing_warrior = session.query(Warrior).filter(Warrior.job == 'Warrior').all()
        existing_magician = session.query(Magician).filter(Magician.job == 'Warrior').all()

        existing_characters = existing_warrior + existing_magician

        session.close()

        return existing_characters



    def get_all_by_type(self, type):
        """Takes in the type and returns a list of entity objects that contains the given type"""

        MapleStory._validate_string_input('Type', type)

        session = self._db_session()

        existing_warrior = session.query(Warrior).filter(Warrior.job == type).all()
        existing_magician = session.query(Magician).filter(Magician.job == type).all()

        session.close()

        if existing_warrior is None:
            return existing_magician
        elif existing_magician is None:
            return existing_warrior

    def update(self, character):
        """Takes an entity object and updates it with the objects id"""
        MapleStory._validate_string_input('Object', character)

        if character is not isinstance(character, AbstractCharacter):
            raise ValueError('Invalid Character Object')

        session = self._db_session()

        if character.job == 'Warrior':
            existing_character = session.query(Warrior).filter(Warrior.id == character.id).first()
            existing_character.copy(character) #look into this

        if character.job == 'Magician':
            existing_character = session.query(Magician).filter(Magician.id == character.id).first()
            existing_character.copy(existing_character)

        session.commit()
        session.close()

    def delete(self, id: int):
        """Deletes an existing student"""

        MapleStory._validate_int_exists('Integer', id)

        session = self._db_session()

        existing_character = session.query(AbstractCharacter).filter(AbstractCharacter.id == id).first()

        if existing_character is None:
            raise ValueError('Character ID: {} does not exist'.format(id))

        session.delete(existing_character)
        session.commit()

        session.close()

    @staticmethod
    def _validate_int_exists(display_name, integer):
        """Checks input if its none, empty or not an integer"""

        if integer is None:
            raise TypeError('{}: cannot be none.'.format(display_name))

        if integer == '':
            raise TypeError('{}: cannot be empty'.format(display_name))

        if integer != int(integer):
            raise TypeError('{} must be integer type'.format(display_name))

    @staticmethod
    def _validate_string_input(display_name, input):
        """Checks to see if the string is none or empty, raises exceptions"""

        if input is None:
            raise TypeError('{}: cannot be none.'.format(display_name))

        if input == '':
            raise TypeError('{}: cannot be empty'.format(display_name))

    @staticmethod
    def _validate_file_path(display_name, filepath):
        """Checks to see if name is in the filepath or not"""

        if not os.path.isfile(filepath):
            raise ValueError('{} must be a file, specifically a {} file.'.format(filepath, display_name))
from sqlalchemy import Column, Integer, String
from base import Base

class AbstractCharacter(Base):
    """Character Declarative"""

    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    job = Column(String(250), nullable=False)
    level = Column(Integer, nullable=False)
    health = Column(Integer, nullable=False)
    health_regeneration = Column(Integer, nullable=False)
    attack_damage = Column(Integer, nullable=False)
    magic_damage = Column(Integer, nullable=False)
    armor = Column(Integer, nullable=False)
    magic_resist = Column(Integer, nullable=False)

    def __init__(self, name, job, level, health, health_regen, attack_damage, magic_damage, armor, magic_resist):
        """Constructor for the character class"""

        AbstractCharacter._validate_string_input('Name', name)
        self._name = name

        AbstractCharacter._validate_string_input('Level', level)
        self._level = int(level)

        AbstractCharacter._validate_string_input('Job', job)
        self._job = job

        AbstractCharacter._validate_string_input('Health', health)
        self._health = int(health)

        AbstractCharacter._validate_string_input('Health Regeneration', health_regen)
        self._health_regeneration = int(health_regen)

        AbstractCharacter._validate_string_input('Attack Damage', attack_damage)
        self._attack_damage = int(attack_damage)

        AbstractCharacter._validate_string_input('Magic Damage', magic_damage)
        self._magic_damage = int(magic_damage)

        AbstractCharacter._validate_string_input('Armor', armor)
        self._armor = int(armor)

        AbstractCharacter._validate_string_input('Magic Resist', magic_resist)
        self._magic_resist = int(magic_resist)

    def get_details(self):
        """An abstract method, Outputs details of the object <character>"""

        raise NotImplementedError("Requires an implementation of a subclass on information")

    def get_type(self):
        """An abstract method, returns the type when implemented"""

        raise NotImplementedError("Requires an implementation of a subclass on type")

    def to_dict(self):
        """An abstract method, returns the required information in dictionary"""

        raise NotImplementedError("Requires an implementation of a subclass on to_dict()")

    def copy(self, object):
        """copies data from both Warrior and Magician object to this object"""

        if isinstance(object, AbstractCharacter):
            self._name = object.name

            self._job = object.job

            self._level = object.level

            self._health = object.health

            self._health_regeneration = object.health_regeneration

            self._attack_damage = object.attack_damage

            self._magic_damage = object.magic_damage

            self._armor = object.armor

            self._magic_resist = object.magic_resist

    @staticmethod
    def _validate_string_input(display_name, user_input):
        """Checks to see if the input is none or empty"""

        if user_input is None:
            raise TypeError('{} cannot be None'.format(display_name))

        if user_input == '':
            raise TypeError('{} cannot be empty'.format(display_name))

    @staticmethod
    def _validate_id_input(display_name, user_input):
        """Checks to see if the input is an integer"""

        if user_input != int(user_input):
            raise TypeError('{} must be an integer.'.format(display_name))

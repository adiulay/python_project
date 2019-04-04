from sqlalchemy import Column, Integer, String
from abstract_character import AbstractCharacter


class Magician(AbstractCharacter):
    """An inherited class that has all of the abstracts from the AbstractCharacter with default variables specific for
    Magician class"""

    MAGICIAN_TYPE = 'Magician'

    wand = Column(String(250))
    spell_cast = Column(String(250))

    def __init__(self, name, job, level, health, health_regen, attack_damage, magic_damage, armor, magic_resist, wand, spell_cast):
        """Constructor that initiates the Magician class with special abilities"""

        Magician._retrieving_errors(name, 'name')
        Magician._retrieving_errors(job, 'job')
        Magician._retrieving_errors(level, 'level')
        Magician._retrieving_errors(health, 'Health')
        Magician._retrieving_errors(health_regen, 'Health Regeneration')
        Magician._retrieving_errors(attack_damage, 'Attack Damage')
        Magician._retrieving_errors(magic_damage, 'Magic Damage')
        Magician._retrieving_errors(armor, 'Armor')
        Magician._retrieving_errors(magic_resist, 'Magic Resist')
        Magician._retrieving_errors(wand, 'Wand Name')
        Magician._retrieving_errors(spell_cast, 'spell cast')
        super().__init__(name, Magician.MAGICIAN_TYPE, level, health, health_regen, attack_damage, magic_damage, armor, magic_resist)

        self.wand = wand
        self.spell_cast = spell_cast

    def get_wand(self):
        """returns the name of wand"""
        return self.wand

    def add_health_regeneration(self):
        """Increases health regeneration"""
        self.health_regeneration += 50 * self.level

    def add_magic_damage(self):
        """Increases magic damage"""
        self.magic_damage += 50 * self.level

    def add_magic_resist(self):
        """Increases magic resist"""
        self.magic_resist += 50 * self.level

    def get_description(self):
        """Returns the description of the class"""
        return "Description: A Magician class that focuses on Health Regeneration, Magic Damage, and Magic Resist"

    def get_details(self):
        """Returns a list of information of the object"""
        _detail_information = []

        _detail_information.append("Name: {}".format(self.name))
        _detail_information.append("Level: {}".format(self.level))
        _detail_information.append("Class Type: {}".format(self.job))
        _detail_information.append("Health: {:.1f}".format(self.health))
        _detail_information.append("Health Regeneration: {:.1f}".format(self.health_regeneration))
        _detail_information.append("Attack Damage: {:.1f}".format(self.attack_damage))
        _detail_information.append("Magic Damage: {:.1f}".format(self.magic_damage))
        _detail_information.append("Armor: {:.1f}".format(self.armor))
        _detail_information.append("Magic Resist: {:.1f}".format(self.magic_resist))
        _detail_information.append("Wand name: {}".format(self.wand))
        _detail_information.append("Magician's main special booster:\n Health Regeneration: {}\n Magic Damage: "
                                    "{}\n Magic Resist: {}".format(
                self.health_regeneration,
                self.magic_damage,
                self.magic_resist))

        return _detail_information

    def get_type(self):
        """Returns the type of class it is in"""
        return 'Magician'

    def set_spellcast(self, spell_name):
        """changes the spellcast name"""
        self.spell_cast = spell_name

    def get_spellcast(self):
        """Returns the spell incantation"""
        return self.spell_cast

    def reset_spellcast(self):
        """resets to its original incantation"""
        self.spell_cast = 'AVADA KEDAVRA'

    def to_dict(self):
        """converts the information into dictionary for easy use for api"""
        dict = {}

        dict['name'] = self.name
        dict['job'] = self.job

        dict['level'] = self.level

        dict['wand'] = self.wand
        dict['spell_cast'] = self.spell_cast

        dict['health'] = self.health
        dict['health_regeneration'] =  self.health_regeneration

        dict['attack_damage'] = self.attack_damage
        dict['magic_damage'] = self.magic_damage

        dict['armor'] = self.armor,
        dict['magic_resist'] = self.magic_resist

        return dict

    def copy(self, object):
        """copies data from magician object to this object"""

        if isinstance(object, Magician):
            self.name = object.name

            self.job = object.job

            self.level = object.level

            self.health = object.health

            self.health_regeneration = object.health_regeneration

            self.attack_damage = object.attack_damage

            self.magic_damage = object.magic_damage

            self.armor = object.armor

            self.magic_resist = object.magic_resist

            self.wand = object.wand

            self.spell_cast = object.spell_cast

    @staticmethod
    def _retrieving_errors(user_input, missing_output):
        """Static Method to check if the input is empty or is None"""
        if user_input is None:
            raise AttributeError("AttributeError: Missing {}, user inputted {}".format(missing_output, user_input))

        if user_input == "":
            raise AttributeError("AttributError: Missing {}, user inputted {}".format(missing_output, user_input))

from sqlalchemy import Column, Integer, String
from abstract_character import AbstractCharacter


class Warrior(AbstractCharacter):
    """An inherited class that has all of the abstracts from the AbstractCharacter with default variables specific for Warrior class"""

    WARRIOR_TYPE = 'Warrior'

    sword = Column(String(250))
    skill_ability = Column(String(250))

    def __init__(self, name, job, level, health, health_regen, attack_damage, magic_damage, armor, magic_resist, sword, skill_ability):
        """Constructor that initiates the warrior class with special abilities"""

        Warrior._retrieving_errors(name, 'name')
        Warrior._retrieving_errors(job, 'job')
        Warrior._retrieving_errors(level, 'level')
        Warrior._retrieving_errors(health, 'Health')
        Warrior._retrieving_errors(health_regen, 'Health Regeneration')
        Warrior._retrieving_errors(attack_damage, 'Attack Damage')
        Warrior._retrieving_errors(magic_damage, 'Magic Damage')
        Warrior._retrieving_errors(armor, 'Armor')
        Warrior._retrieving_errors(magic_resist, 'Magic Resist')
        Warrior._retrieving_errors(sword, 'Sword Name')
        Warrior._retrieving_errors(skill_ability, 'skill ability')
        super().__init__(name, Warrior.WARRIOR_TYPE, level, health, health_regen, attack_damage, magic_damage, armor, magic_resist)

        self._sword = sword
        self._skill_ability = skill_ability

    def get_sword(self):
        """returns a sword type"""
        return self._sword

    def add_armor(self):
        """Increases armor stats"""

        self._armor += 50 * self.get_level()

    def add_attack_damage(self):
        """Increases attack damage"""

        self._attackdmg += 50 * self.get_level()

    def add_health(self):
        """Increases health"""

        self._health += 50 * self.get_level()

    def get_description(self):
        """Returns the description of the class"""
        return "Description: A Warrior class that focuses on Health, Armor, and Attack Damage"

    def get_details(self):
        """returns a list of information of the object"""
        _detail_information = []

        _detail_information.append("Name: {}".format(self._name))
        _detail_information.append("Level: {}".format(self._level))
        _detail_information.append("Class Type: {}".format(self._job))
        _detail_information.append("Health: {:.1f}".format(self._health))
        _detail_information.append("Health Regeneration: {:.1f}".format(self._health_regeneration))
        _detail_information.append("Attack Damage: {:.1f}".format(self._attackdmg))
        _detail_information.append("Magic Damage: {:.1f}".format(self._magicdmg))
        _detail_information.append("Armor: {:.1f}".format(self._armor))
        _detail_information.append("Magic Resist: {:.1f}".format(self._magicresist))
        _detail_information.append("Sword Name: {}".format(self._sword))
        _detail_information.append("Warrior's main special booster:\n Armor: {}\n Attack Damage: {}\n Health: {}".format(self._armor, self._attackdmg, self._health))

        return _detail_information

    def get_type(self):
        """returns the type of class it is in"""
        return 'Warrior'

    def set_special_skill(self, skill_name):
        """changes the skill name"""
        self._skill_ability = skill_name

    def get_special_skill(self):
        """Returns the skill name"""
        return self._skill_ability

    def reset_special_skill(self):
        """resets to its original skill name"""
        self._skill_ability = 'GETSUGA TENSHOU'

    def to_dict(self):
        """converts the information into dictionary for easy use for api"""
        dict = {}

        dict['Name'] = self._name
        dict['Job'] = self._job

        dict['Level'] = self._level

        dict['Sword Name'] = self._sword
        dict['Ultimate Skill'] = self._skill_ability

        dict['Health'] = self._health
        dict['Health Regeneration'] = self._health_regeneration

        dict['Attack Damage'] = self._attackdmg
        dict['Magic Damage'] = self._magicdmg

        dict['Armor'] = self._armor,
        dict['Magic Resist'] = self._magicresist

        return dict

    def copy(self, object):
        """copies from warrior to base for updating"""

        if isinstance(object, Warrior):
            self._name = object.name

            self._job = object.job

            self._level = object.level

            self._health = object.health

            self._healthregen = object.health_regeneration

            self._attackdmg = object.attack_damage

            self._magicdmg = object.magic_damage

            self._armor = object.armor

            self._magicresist = object.magic_resist

    @staticmethod
    def _retrieving_errors(user_input, missing_output):
        """Static Method to check if the input is empty or is None"""
        if user_input is None:
            raise ValueError("AttributeError: Missing {}, user inputted {}".format(missing_output, user_input))

        if user_input == "":
            raise ValueError("AttributError: Missing {}, user inputted {}".format(missing_output, user_input))
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

        self.sword = sword
        self.skill_ability = skill_ability

    def get_sword(self):
        """returns a sword type"""
        return self.sword

    def add_armor(self):
        """Increases armor stats"""

        self.armor += 50 * self.level

    def add_attack_damage(self):
        """Increases attack damage"""

        self.attack_damage += 50 * self.level

    def add_health(self):
        """Increases health"""

        self.health += 50 * self.level

    def get_description(self):
        """Returns the description of the class"""
        return "Description: A Warrior class that focuses on Health, Armor, and Attack Damage"

    def get_details(self):
        """returns a list of information of the object"""
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
        _detail_information.append("Sword Name: {}".format(self.sword))
        _detail_information.append("Warrior's main special booster:\n Armor: {}\n Attack Damage: {}\n Health: {}".format(self.armor, self.attack_damage, self.health))

        return _detail_information

    def get_type(self):
        """returns the type of class it is in"""
        return 'Warrior'

    def set_special_skill(self, skill_name):
        """changes the skill name"""
        self.skill_ability = skill_name

    def get_special_skill(self):
        """Returns the skill name"""
        return self.skill_ability

    def reset_special_skill(self):
        """resets to its original skill name"""
        self.skill_ability = 'GETSUGA TENSHOU'

    def to_dict(self):
        """converts the information into dictionary for easy use for api"""
        dict = {}

        dict['name'] = self.name
        dict['job'] = self.job

        dict['level'] = self.level

        dict['health'] = self.health
        dict['health_regeneration'] = self.health_regeneration

        dict['attack_damage'] = self.attack_damage
        dict['magic_damage'] = self.magic_damage

        dict['armor'] = self.armor
        dict['magic_resist'] = self.magic_resist

        dict['sword'] = self.sword
        dict['skill_ability'] = self.skill_ability

        return dict

    def copy(self, object):
        """copies from warrior to base for updating"""

        if isinstance(object, Warrior):
            self.name = object.name

            self.job = object.job

            self.level = object.level

            self.health = object.health

            self.health_regeneration = object.health_regeneration

            self.attack_damage = object.attack_damage

            self.magic_damage = object.magic_damage

            self.armor = object.armor

            self.magic_resist = object.magic_resist

            self.sword = object.sword

            self.skill_ability = object.skill_ability

    @staticmethod
    def _retrieving_errors(user_input, missing_output):
        """Static Method to check if the input is empty or is None"""
        if user_input is None:
            raise ValueError("AttributeError: Missing {}, user inputted {}".format(missing_output, user_input))

        if user_input == "":
            raise ValueError("AttributError: Missing {}, user inputted {}".format(missing_output, user_input))
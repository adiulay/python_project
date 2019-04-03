import unittest
import inspect
from unittest import TestCase
from magician import Magician

class TestWarrior(TestCase):
    """Unit test for class Warrior"""

    def setUp(self):
        """Sets up imitation objects"""
        self._evan = Magician(4, 'Evan', 71, 43, 76, 96, 66, 82, 'Renegade Dragon')
        self._evan.set_experience_info(1600)
        self._evan.add_health_regeneration()
        self._evan.add_magic_damage()
        self._evan.add_magic_resist()
        self._evan.set_spellcast('Dragon Spark!')
        self._details = ['Name: Evan',
                         'Level: 16',
                         'Class Type: Magician',
                         'Health: 71.0',
                         'Health Regeneration: 843.0',
                         'Attack Damage: 76.0',
                         'Magic Damage: 896.0',
                         'Armor: 66.0',
                         'Magic Resist: 882.0',
                         'Wand name: Renegade Dragon',
                         "Magician's main special booster:\n"
                         ' Health Regeneration: 843.0\n'
                         ' Magic Damage: 896.0\n'
                         ' Magic Resist: 882.0']
        self._to_dict_object = {
                                "ID": 4,
                                "Name": "Evan",
                                "Job": "Magician",
                                "Level": {
                                    "Level": 16,
                                    "Experience": 1600
                                },
                                "Wand Name": "Renegade Dragon",
                                "Special Cast": "Dragon Spark!",
                                "Health": {
                                    "Health": 71.0,
                                    "Health Regeneration": 843.0
                                },
                                "Offense": {
                                    "Attack Damage": 76.0,
                                    "Magic Damage": 896.0
                                },
                                "Defense": {
                                    "Armor": 66.0,
                                    "Magic Resist": 882.0
                                }
                            }
        self._type = 'Magician'
        self._description = 'Description: A Magician class that focuses on Health Regeneration, Magic Damage, ' \
                            'and Magic Resist'

        self.logPoint()

    def test_get_wand(self):
        """A010 - Tests for the get wand method"""
        self.assertEqual(self._evan.get_wand(), 'Renegade Dragon')

        self.logPoint()

    def test_add_magic_resist(self):
        '''B010 - Tests if the magic resist is equal to what has been added to the class'''
        self.assertEqual(self._evan.get_magicresist(), 882)

        self.logPoint()

    def test_add_magic_damage(self):
        '''C010 - Tests if the magic damage is equal to what has been added to the class'''
        self.assertEqual(self._evan.get_magicdmg(), 896)

        self.logPoint()

    def test_add_health_regen(self):
        '''D010 - Tests if the health regen is equal to what has been added to the class'''
        self.assertEqual(self._evan.get_healthregen(), 843)

        self.logPoint()

    def test_get_description(self):
        """E010 - Tests if the get_description method is equal to the correct output"""
        self.assertEqual(self._evan.get_description(), self._description)

        self.logPoint()

    def test_get_details(self):
        """F010 - Tests if the get_detail method is equal to the imitation list self._details"""
        self.assertEqual(self._evan.get_details(), self._details)

        self.logPoint()

    def test_get_type(self):
        """G010 - Tests the get_type method for type"""
        self.assertEqual(self._evan.get_type(), self._type)

        self.logPoint()

    def test_set_spellcast(self):
        """H010 - Tests if the correct spellcast was set"""
        self._evan.set_spellcast('Tester')

        self.assertEqual(self._evan.get_spellcast(), 'Tester')

        self.logPoint()

    def test_get_spellcast(self):
        """I010 - Tests if the correct spellcast name was gotten"""
        self.assertEqual(self._evan.get_spellcast(), "Dragon Spark!")

        self.logPoint()

    def test_reset_spellcast(self):
        """J010 - Tests if the spellcast name was reset correctly"""
        self._evan.reset_spellcast()

        self.assertEqual(self._evan.get_spellcast(), 'AVADA KEDAVRA')

        self.logPoint()

    def test_to_dict(self):
        """K010 - Tests if to dict method correctly formatted the object"""
        self.assertEqual(self._evan.to_dict(), self._to_dict_object)

        self.logPoint()

    def tearDown(self):
        """Tears down from setup"""
        self.logPoint()

    def logPoint(self):
        """Utility function used for module functions and class methods"""

        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in {} - {}()'.format(currentTest, callingFunction))

if __name__ == '__main__':
    unittest.main()

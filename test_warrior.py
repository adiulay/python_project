import unittest
import inspect
from unittest import TestCase
from warrior import Warrior

class TestWarrior(TestCase):
    """Unit test for class Warrior"""

    def setUp(self):
        """Sets up imitation objects"""

        self._aran = Warrior(16, 'Aran', 96, 77, 72, 92, 56, 36, 'Morningstar')
        self._aran.set_experience_info(5200)
        self._aran.add_armor()
        self._aran.add_attack_damage()
        self._aran.add_health()
        self._aran.set_special_skill('Fenrir Roar!')
        self._details = ['Name: Aran',
                         'Level: 52',
                         'Class Type: Warrior',
                         'Health: 2696.0',
                         'Health Regeneration: 77.0',
                         'Attack Damage: 2672.0',
                         'Magic Damage: 92.0',
                         'Armor: 2656.0',
                         'Magic Resist: 36.0',
                         'Sword Name: Morningstar',
                         "Warrior's main special booster:\n"
                         ' Armor: 2656.0\n'
                         ' Attack Damage: 2672.0\n'
                         ' Health: 2696.0']
        self._to_dict_object = {
                                "ID": 16,
                                "Name": "Aran",
                                "Job": "Warrior",
                                "Level": {
                                    "Level": 52,
                                    "Experience": 5200
                                },
                                "Sword Name": "Morningstar",
                                "Ultimate Skill": "Fenrir Roar!",
                                "Health": {
                                    "Health": 2696.0,
                                    "Health Regeneration": 77.0
                                },
                                "Offense": {
                                    "Attack Damage": 2672.0,
                                    "Magic Damage": 92.0
                                },
                                "Defense": {
                                    "Armor": 2656.0,
                                    "Magic Resist": 36.0
                                }
                            }
        self._type = 'Warrior'
        self._description = 'Description: A Warrior class that focuses on Health, Armor, and Attack Damage'
        self.logPoint()

    def test_validate(self):
        self.assertRaisesRegex(ValueError, "AttributeError: Missing ID, user inputted None", Warrior, None, None, None, None, None, None, None, None
                           , None)

        self.assertRaisesRegex(ValueError, "AttributError: Missing ID, user inputted ", Warrior, '', '', '',
                               '', '', '', '', ''
                               , '')

        # self.assertRaisesRegex(ValueError, "AttributeError: Missing name, user inputted None", Warrior, 3, None, None, None, None, None, None, None,
        #                        None)
        # self.assertRaisesRegex(ValueError, "AttributeError: Missing Health, user inputted None", Warrior, 3, 'Aran', None, None, None, None, None,
        #                        None, None)
        # self.assertRaisesRegex(ValueError, "Health Regen cannot be empty", Warrior, 3, 'Aran', 20, None, None, None,
        #                        None, None, None)
        # self.assertRaisesRegex(ValueError, "Attack Damage cannot be empty", Warrior, 3, 'Aran', 20, 0.5, None, None,
        #                        None, None, None)
        # self.assertRaisesRegex(ValueError, "Magic Damage cannot be empty", Warrior, 3, 'Aran', 20, 0.5, 35, None, None,
        #                        None, None)
        # self.assertRaisesRegex(ValueError, "Armor cannot be empty", Warrior, 3, 'Aran', 20, 0.5, 35, 20, None, None,
        #                        None)
        # self.assertRaisesRegex(ValueError, "Magic Resist cannot be empty", Warrior, 3, 'Aran', 20, 0.5, 35, 20, 3, None,
        #                        None)
        # self.assertRaisesRegex(ValueError, "Sword cannot be empty", Warrior, 3, 'Aran', 20, 0.5, 35, 20, 3, 20, None)

    def test_get_sword(self):
        """A010 - Tests if the correct sword name is gotten"""
        self.assertEqual(self._aran.get_sword(), "Morningstar")

        self.logPoint()

    def test_add_armor(self):
        '''B010 - Tests if the armor boost is equal to what has been added to the class'''
        self._aran.add_armor()
        self.assertEqual(self._aran.get_armor(), 5256)

        self.logPoint()

    def test_add_attack_damage(self):
        '''C010 - Tests if the damage boost is equal to what has been added to the class'''
        self._aran.add_attack_damage()
        self.assertEqual(self._aran.get_attackdmg(), 5272)

        self.logPoint()

    def test_add_health(self):
        '''D010 - Tests if the health boost is equal to what has been added to the class'''
        self._aran.add_health()
        self.assertEqual(self._aran.get_health(), 5296)

        self.logPoint()

    def test_get_description(self):
        """E010 - Tests if the get_description method is equal to the correct output"""
        self.assertEqual(self._aran.get_description(), self._description)

        self.logPoint()

    def test_get_details(self):
        """F010 - Tests if the get_detail method is equal to the imitation list self._details"""
        self.assertEqual(self._aran.get_details(), self._details)

        self.logPoint()

    def test_get_type(self):
        """G010 - Tests the get_type method for type"""
        self.assertEqual(self._aran.get_type(), self._type)

        self.logPoint()

    def test_set_special_skill(self):
        """H010 - Tests if the correct special skill name was set"""
        self._aran.set_special_skill('Tester')

        self.assertEqual(self._aran.get_special_skill(), 'Tester')

        self.logPoint()

    def test_get_special_skill(self):
        """I010 - Tests if the correct special skill name was gotten"""
        self.assertEqual(self._aran.get_special_skill(), 'Fenrir Roar!')

        self.logPoint()

    def test_reset_special_skill(self):
        """J010 - Tests if the special skill was reset correctly"""
        self._aran.reset_special_skill()

        self.assertEqual(self._aran.get_special_skill(), 'GETSUGA TENSHOU')

        self.logPoint()

    def test_to_dict(self):
        """K010 - Tests if the to_dict method correctly formatted the object"""
        self.assertEqual(self._aran.to_dict(), self._to_dict_object)

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

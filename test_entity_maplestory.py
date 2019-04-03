import unittest
from unittest import TestCase
import inspect
from maple_story import MapleStory
from warrior import Warrior
from magician import Magician
from unittest.mock import MagicMock
from unittest.mock import patch, mock_open
import json
import os

class TestMapleStory(TestCase):
    """Unit Test for Class MapleStory <entity>"""
    MOCK_JSON = []

    @patch('builtins.open', mock_open(read_data=''))
    def setUp(self):
        json.loads = MagicMock(return_value=TestMapleStory.MOCK_JSON)
        self._test_maple_story = MapleStory('testing.json')
        # for character in MOCK_JSON:
        #     self._test_maple_story.add(character)

        self._hayato = Warrior(23, 'Hayato', 100, 100, 100, 0, 100, 0, 'Soul Stalker')
        self._mihile = Warrior(34, 'Mihile', 82, 22, 68, 39, 58, 32, 'Excalibur')
        self._ichigo = Warrior(47, 'Ichigo', 92, 18, 32, 10, 88, 70, 'Zangetsu')
        self._aizen = Warrior(16, 'Aizen', 96, 77, 72, 92, 56, 36, 'Kyoka Suigetsu')
        self._aran = Warrior(16, 'Aran', 96, 77, 72, 92, 56, 36, 'Morningstar')

        self._harry_potter = Magician(0, 'Harry Potter', 100, 50, 0, 500, 0, 100, 'Deletus')
        self._cleric = Magician(1, 'Cleric', 23, 51, 9, 52, 14, 95, 'Mithrill')
        self._ice_mage = Magician(2, 'Ice Mage', 16, 21, 40, 62, 98, 80, 'Cromi')
        self._fire_mage = Magician(3, 'Fire Mage', 16, 21, 40, 62, 98, 80, 'Phoenix')
        self._evan = Magician(4, 'Evan', 71, 43, 76, 96, 66, 82, 'Renegade Dragon')


        self._update = Magician(1, 'Update_Dark Magician', 100, 1000, 100, 2500, 100, 2100, "Dark Magician's Staff")
        self._update2 = Warrior(0, 'Updater_Black_Luster_Soldier', 3000, 100, 3000, 100, 2500, 100, "Black Luster Soldier's Sword")

        self.logPoint()

    def test_add_validation(self):
        """01A - Valid Add job_class"""

        #must have invalid input undefined
        self.assertRaisesRegex(TypeError, 'Object: cannot be none.', self._test_maple_story.add, None)

        # must have invalid input empty
        self.assertRaisesRegex(TypeError, 'Object: cannot be empty', self._test_maple_story.add, '')
        self.logPoint()

    def test_add_length(self):
        """01B - When adding, checks to see the length of list is correct, minus the repeats"""

        self._test_maple_story.add(self._hayato)

        self.assertEqual(len(self._test_maple_story.get_all()), 1)

        #forcing adding the same object, must reject upon adding
        self._test_maple_story.add(self._hayato)
        self.assertEqual(len(self._test_maple_story.get_all()), 1)

        #adding a different object, same class
        self._test_maple_story.add(self._mihile)
        self.assertEqual(len(self._test_maple_story.get_all()), 2)

        #adding different object, different class
        self._test_maple_story.add(self._harry_potter)
        self.assertEqual(len(self._test_maple_story.get_all()), 3)

        os.remove("testing.json")
        self.logPoint()

    def test_add_unique_id(self):
        """01C - forces to make unique id when adding and removing <must be unique>"""

        self._test_maple_story.add(self._hayato)
        self.assertEqual(self._hayato.get_id(), 0)

        self._test_maple_story.add(self._aran)
        self.assertEqual(self._aran.get_id(), 1)

        self._test_maple_story.add(self._harry_potter)
        self.assertEqual(self._harry_potter.get_id(), 2)

        #forcing adding same object, id should be the same regardless <because nothing happens>
        self._test_maple_story.add(self._hayato)
        self.assertEqual(self._hayato.get_id(), 0)

        #forcing delete would keep having unique when added back on
        self._test_maple_story.delete(0)
        self._test_maple_story.add(self._hayato)
        self.assertEqual(self._hayato.get_id(), 3)

        os.remove("testing.json")
        self.logPoint()

    def test_validate_string_path(self):
        """01D - Validates the initiation of class <with filepath required>"""
        # self.assertRaisesRegex(ValueError, "{} must be a file, specifically a json file.".format(self._windia_json), self._test_maplestory)
        self.assertRaisesRegex(TypeError, 'File path: cannot be empty', MapleStory, '')
        self.assertRaisesRegex(TypeError, 'File path: cannot be none.', MapleStory, None)

        self.logPoint()

    def test_get_validate(self):
        """02A - validates taking in int"""

        # Fails on getting none
        self.assertRaisesRegex(TypeError, 'Input: cannot be none.', self._test_maple_story.get, None)

        # Fails on getting empty
        self.assertRaisesRegex(TypeError, 'Input: cannot be empty', self._test_maple_story.get, '')

        self.logPoint()

    def test_get_retrieval(self):
        """02B - Successfully on getting the object by id"""

        self._test_maple_story.add(self._cleric)
        self._test_maple_story.add(self._evan)
        self._test_maple_story.add(self._fire_mage)

        #successfully returns id with entity
        self.assertIsInstance(self._test_maple_story.get(0), object)

        # double checks entity is the same by accessing name from object
        self.assertEqual(self._test_maple_story.get(0).get_name(), 'Cleric')

        #both id from object and get are the same
        self.assertEqual(self._test_maple_story.get(2).get_id(), 2)

        # returns none when not in list
        self.assertIsNone(self._test_maple_story.get(25))

        os.remove("testing.json")
        self.logPoint()

    def test_character_exist_validation(self):
        """validates argument that it cannot be empty or none, as well as that it returns true or false"""
        self._test_maple_story.add(self._cleric)
        self._test_maple_story.add(self._evan)
        self._test_maple_story.add(self._fire_mage)

        self.assertRaisesRegex(TypeError, 'Object: cannot be empty', self._test_maple_story.add, '')
        self.assertRaisesRegex(TypeError, 'Object: cannot be none.', self._test_maple_story.add, None)

        self.assertTrue(self._test_maple_story.character_exist(1))
        self.assertTrue(self._test_maple_story.character_exist(0))
        self.assertTrue(self._test_maple_story.character_exist(2))

        self.assertFalse(self._test_maple_story.character_exist(3))

        os.remove("testing.json")
        self.logPoint()

    def test_get_all(self):
        """03A - successful on returning a list if there is any, else returns empty list"""

        self._test_maple_story.add(self._ichigo)
        self._test_maple_story.add(self._mihile)
        self._test_maple_story.add(self._fire_mage)

        self.assertIsInstance(self._test_maple_story.get_all(), list)

        self._test_maple_story.delete(0)
        self._test_maple_story.delete(1)
        self._test_maple_story.delete(2)

        self.assertEqual(self._test_maple_story.get_all(), [])

        self.assertIsInstance(self._test_maple_story.get_all(), list)

        os.remove("testing.json")
        self.logPoint()

    def test_get_all_by_type_validation(self):
        """04A - validates the type as string"""

        # must have invalid input
        self.assertRaisesRegex(TypeError, 'Type: cannot be none.', self._test_maple_story.get_all_by_type, None)

        # must have empty input
        self.assertRaisesRegex(TypeError, 'Type: cannot be empty', self._test_maple_story.get_all_by_type, '')

        self.logPoint()

    def test_get_all_by_type(self):
        """04B - successfully returns list of the same type"""

        # magicians class
        self._test_maple_story.add(self._fire_mage)
        self._test_maple_story.add(self._ice_mage)

        # warrior class
        self._test_maple_story.add(self._aizen)
        self._test_maple_story.add(self._hayato)
        self._test_maple_story.add(self._aran)
        self._test_maple_story.add(self._mihile)

        # returns 4 warriors
        self.assertEqual(len(self._test_maple_story.get_all_by_type('Warrior')), 4)

        # returns 2 magicians
        self.assertEqual(len(self._test_maple_story.get_all_by_type('Magician')), 2)

        os.remove("testing.json")
        self.logPoint()

    def test_update_validate(self):
        """05A - Validates the object input"""

        # must have invalid input
        self.assertRaisesRegex(TypeError, 'Object: cannot be none.', self._test_maple_story.update, None)

        # must have empty input
        self.assertRaisesRegex(TypeError, 'Object: cannot be empty', self._test_maple_story.update, '')

        self.logPoint()

    def test_update_success(self):
        """05B - Successfully updates an existing class with new class"""

        self._test_maple_story.add(self._hayato)
        self._test_maple_story.add(self._aran)
        self._test_maple_story.add(self._mihile)

        self.assertEqual(self._test_maple_story.get(0).get_name(), 'Hayato')

        # updates current object from the list to a new one
        self._test_maple_story.update(self._update2)

        self.assertEqual(self._test_maple_story.get(0).get_name(), 'Updater_Black_Luster_Soldier')

        self.assertNotEqual(self._test_maple_story.get(0).get_name(), 'Hayato')

        os.remove("testing.json")
        self.logPoint()

    def test_delete_validate(self):
        """06A - validation"""

        # must have invalid input
        self.assertRaisesRegex(TypeError, 'Integer: cannot be none.', self._test_maple_story.delete, None)

        # must have empty input
        self.assertRaisesRegex(TypeError, 'Integer: cannot be empty', self._test_maple_story.delete, '')

        self.logPoint()

    def test_delete(self):
        """06B - checks if the id matches from the list and removes it"""

        self._test_maple_story.add(self._cleric)
        self._test_maple_story.add(self._fire_mage)
        self._test_maple_story.add(self._hayato)
        self._test_maple_story.add(self._update2)
        self._test_maple_story.add(self._update)
        self._test_maple_story.add(self._mihile)
        self._test_maple_story.add(self._ice_mage)

        self.assertEqual(len(self._test_maple_story.get_all()), 7)

        self._test_maple_story.delete(6)

        self.assertEqual(len(self._test_maple_story.get_all()), 6)

        os.remove("testing.json")
        self.logPoint()

    def tearDown(self):
        """tears down from setup"""
        self.logPoint()

    def logPoint(self):
        """utility function used for module functions and class methods"""

        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in {} - {}()'.format(currentTest, callingFunction))


if __name__ == '__main__':
    unittest.main()
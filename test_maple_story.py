import unittest
from unittest import TestCase
import inspect
from maple_story import MapleStory
from warrior import Warrior
from magician import Magician

from sqlalchemy import create_engine
from base import Base
import os


class TestMapleStory(TestCase):
    """Unit Test for Class MapleStory <entity>"""

    def setUp(self):
        """sets up creating objects for the testing phase"""
        engine = create_engine('sqlite:///tests_ms.sqlite')

        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        self._test_maple_story = MapleStory('tests_ms.sqlite')


        self._hayato = Warrior('Hayato', 'Warrior', 89, 100, 100, 100, 0, 100, 0, 'Soul Stalker', 'Soul Exchange!')
        self._mihile = Warrior('Mihile', 'Warrior', 197, 22, 68, 39, 58, 32, 74,  'Excalibur', 'Excalibur, Obliterate!')
        self._ichigo = Warrior('Ichigo', 'Warrior', 134, 18, 32, 10, 88, 70, 24, 'Zangetsu', 'Bankai!')
        self._aizen = Warrior('Aizen', 'Warrior', 17, 77, 72, 92, 56, 36, 79, 'Kyoka Suigetsu', 'Kai!')
        self._aran = Warrior('Aran', 'Warrior', 6, 77, 72, 92, 56, 36, 35, 'Morningstar', 'Morning Glory!')

        self._harry_potter = Magician('Harry Potter', 'Magician', 23, 50, 0, 500, 0, 100, 71, 'Deletus', 'Expecto, Patronum!')
        self._cleric = Magician('Cleric', 'Magician', 40, 51, 9, 52, 14, 95, 52, 'Mithrill', 'Holy Symbol!')
        self._ice_mage = Magician('Ice Mage', 'Magician', 118, 21, 40, 62, 98, 80, 48, 'Cromi', 'Absolute Zero!')
        self._fire_mage = Magician('Fire Mage', 'Magician', 77, 21, 40, 62, 98, 80, 83, 'Phoenix', 'Infinite Fiery!')
        self._evan = Magician('Evan', 'Magician', 46, 43, 76, 96, 66, 82, 89, 'Renegade Dragon', 'Taigas, Obliterate!')


        self._update = Magician('Update_Dark Magician', 'Magician', 120, 1000, 100, 2500, 100, 2100, 2163,
                                "Dark Magician's Staff", 'Dark Magic Attack!')
        self._update2 = Warrior('Updater_Black_Luster_Soldier', 'Warrior', 9, 100, 3000, 100, 2500, 100, 432,
                                "Black Luster Soldier's Sword", 'Slash slash slash!')

        self._test_maple_story.add(self._hayato)
        self._test_maple_story.add(self._harry_potter)

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

        self._test_maple_story.add(self._mihile)

        self.assertEqual(len(self._test_maple_story.get_all()), 3)

        #forcing adding the same object, must reject upon adding
        self._test_maple_story.add(self._mihile)
        self.assertEqual(len(self._test_maple_story.get_all()), 3)

        #adding a different object, same class
        self._test_maple_story.add(self._ichigo)
        self.assertEqual(len(self._test_maple_story.get_all()), 4)

        #adding different object, different class
        self._test_maple_story.add(self._cleric)
        self.assertEqual(len(self._test_maple_story.get_all()), 5)

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
    #
    def test_get_retrieval(self):
        """02B - Successfully on getting the object by id"""

        #successfully returns id with entity
        self.assertIsInstance(self._test_maple_story.get(1), object)

        # double checks entity is the same by accessing name from object
        self.assertEqual(self._test_maple_story.get(2).get_name(), 'Harry Potter')

        # returns none when not in list
        self.assertIsNone(self._test_maple_story.get(25))

        self.logPoint()

    def test_get_all(self):
        """03A - successful on returning a list if there is any, else returns empty list"""

        self._test_maple_story.add(self._ichigo)
        self._test_maple_story.add(self._mihile)
        self._test_maple_story.add(self._fire_mage)

        self.assertIsInstance(self._test_maple_story.get_all(), list)

        self._test_maple_story.delete(1)
        self._test_maple_story.delete(2)

        for character in self._test_maple_story.get_all():
            if character.get_type() == 'Warrior':
                self.assertEqual(character.get_type(), 'Warrior')
            elif character.get_type() == 'Magician':
                self.assertEqual(character.get_type(), 'Magician')


        self.assertIsInstance(self._test_maple_story.get_all(), list)

        self.logPoint()

    def test_get_all_by_type_validation(self):
        """04A - validates the type as string"""

        # must have invalid input
        self.assertRaisesRegex(TypeError, 'Type: cannot be none.', self._test_maple_story.get_all_by_type, None)

        # must have empty input
        self.assertRaisesRegex(TypeError, 'Type: cannot be empty', self._test_maple_story.get_all_by_type, '')

        self.logPoint()

    def test_update_validate(self):
        """05A - Validates the object input"""

        # must have invalid input
        self.assertRaisesRegex(TypeError, 'Object: cannot be none.', self._test_maple_story.update, None)

        # must have empty input
        self.assertRaisesRegex(TypeError, 'Object: cannot be empty', self._test_maple_story.update, '')

        self.logPoint()
    #
    def test_update_success(self):
        """05B - Successfully updates an existing class with new class"""

        self.assertEqual(self._test_maple_story.get(1).name, 'Hayato')

        retrieved_character = self._test_maple_story.get(1)

        retrieved_character.name = 'Yato'
        self._test_maple_story.update(retrieved_character)

        self.assertEqual(self._test_maple_story.get(1).name, 'Yato')

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
        self._test_maple_story.add(self._update2)
        self._test_maple_story.add(self._update)
        self._test_maple_story.add(self._mihile)
        self._test_maple_story.add(self._ice_mage)

        self.assertEqual(len(self._test_maple_story.get_all()), 8)

        self._test_maple_story.delete(6)

        self.assertEqual(len(self._test_maple_story.get_all()), 7)

        self.logPoint()

    def tearDown(self):
        """tears down from setup"""

        os.remove('tests_ms.sqlite')
        self.logPoint()

    def logPoint(self):
        """utility function used for module functions and class methods"""

        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in {} - {}()'.format(currentTest, callingFunction))

if __name__ == '__main__':
    unittest.main()
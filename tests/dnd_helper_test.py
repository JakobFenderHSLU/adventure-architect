from Utility.ItemHelper import check_attribute, check_attributes

import unittest

EXAMPLE_NPC = {
    'name': 'Elias Blackthorn',
    'Actions': [
        {"name": "Sword Attack", "description": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. "
                                                "Hit: 10 (1d10 + 5) piercing damage."}
    ],
    'Stats': {
        "Strength": 12,
        "Dexterity": 14,
        "Constitution": 10,
        "Intelligence": 16,
        "Wisdom": 13,
        "Charisma": 15
    },
    'Armor Class': 16,
    'Race': 'Human',
    'Image generation prompt': '',
    'Legendary Actions': [],
    'Empty Stats': {},
    'Condition Immunities': None
}


class TestCheckAttribute(unittest.TestCase):
    def test_existing_string_attribute(self):
        self.assertTrue(check_attribute('name', EXAMPLE_NPC))

    def test_existing_list_attribute(self):
        self.assertTrue(check_attribute('Actions', EXAMPLE_NPC))

    def test_existing_dict_attribute(self):
        self.assertTrue(check_attribute('Stats', EXAMPLE_NPC))

    def test_existing_nonempty_attribute(self):
        self.assertTrue(check_attribute('Armor Class', EXAMPLE_NPC))

    def test_missing_attribute(self):
        self.assertFalse(check_attribute('Quirks', EXAMPLE_NPC))

    def test_empty_string_attribute(self):
        self.assertFalse(check_attribute('Image generation prompt', EXAMPLE_NPC))

    def test_empty_list_attribute(self):
        self.assertFalse(check_attribute('Legendary Actions', EXAMPLE_NPC))

    def test_empty_dict_attribute(self):
        self.assertFalse(check_attribute('Empty Stats', EXAMPLE_NPC))

    def test_none_attribute_value(self):
        self.assertFalse(check_attribute('Condition Immunities', EXAMPLE_NPC))


class TestCheckAttributes(unittest.TestCase):
    def test_all_existing_attributes(self):
        attributes_to_check = [
            'name',
            'Actions',
            'Stats',
            'Armor Class'
        ]
        self.assertTrue(check_attributes(attributes_to_check, EXAMPLE_NPC))

    def test_missing_attribute(self):
        attributes_to_check = [
            'name',
            'Quirks'
        ]
        self.assertFalse(check_attributes(attributes_to_check, EXAMPLE_NPC))

    def test_empty_attributes(self):
        attributes_to_check = [
            'Image generation prompt',
            'Legendary Actions',
            'Empty Stats',
        ]
        self.assertFalse(check_attributes(attributes_to_check, EXAMPLE_NPC))


if __name__ == '__main__':
    unittest.main()

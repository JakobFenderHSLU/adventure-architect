possible_monster_types = ["Aberration", "Beast", "Celestial", "Construct", "Dragon", "Elemental", "Fey", "Fiend",
                          "Giant", "Humanoid", "Monstrosity", "Ooze", "Plant", "Undead"]
possible_challenge_ratings = ["0", "1/8", "1/4", "1/2", range(1, 31)]
possible_size = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]
possible_environments = ["Arctic", "Coastal", "Desert", "Forest", "Grassland", "Hill", "Mountain", "Swamp", "Underdark",
                            "Underwater", "Urban"]

monster_template = """{
    "Name": "",
    "Size": "",
    "Type": "",
    "Environment": "",
    "Alignment": "",
    "Visual Description": "",
    "Quirks": "",
    "Additional Information": "",
    "Tactics": "",
    "Stats": {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    },
    "Armor Class": 0,
    "Hit Points": 0,
    "Speed": "",
    "Saving Throws": "",
    "Skills": "",
    "Damage Vulnerabilities": "",
    "Damage Resistances": "",
    "Damage Immunities": "",
    "Condition Immunities": "",
    "Senses": "",
    "Languages": "",
    "Challenge Rating": "",
    "Actions": [
        {
            "Name": "",
            "Description": ""
        }
    ],
    "Bonus Actions": [
        {
            "Name": "",
            "Description": ""
        }
    ],
    "Legendary Action Description": "",
    "Legendary Actions": [
        {
            "Name": "",
            "Description": ""
        }
    ],
    "Lair Action Description": "",
    "Lair Actions": [
        {
            "Name": "",
            "Description": ""
        }
    ],
}"""
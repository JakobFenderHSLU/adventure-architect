possible_races = ['Aarakocra', 'Aasimar', 'Air Genasi', 'Astral Elf', 'Autognome', 'Bugbear', 'Centaur', 'Changeling',
                  'Deep Gnome', 'Dragonborn', 'Duergar', 'Dwarf', 'Earth Genasi', 'Eladrin', 'Elf', 'Fairy',
                  'Feral Tiefling', 'Firbolg', 'Fire Genasi', 'Giff', 'Githyanki', 'Githzerai', 'Gnome', 'Goblin',
                  'Goliath', 'Grung', 'Hadozee', 'Half-Elf', 'Half-Orc', 'Halfling', 'Harengon', 'Hobgoblin', 'Human',
                  'Kalashtar', 'Kender', 'Kenku', 'Kobold', 'Leonin', 'Lizardfolk', 'Locathah', 'Loxodon', 'Minotaur',
                  'Orc', 'Owlin', 'Plasmoid', 'Satyr', 'Sea Elf', 'Shadar-kai', 'Shifter', 'Simic Hybrid', 'Tabaxi',
                  'Thri-kreen', 'Tiefling', 'Tortle', 'Triton', 'Vedalken', 'Verdan', 'Warforged', 'Water Genasi',
                  'Yuan-ti']
possible_core_races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human', 'Tiefling']
possible_challenge_ratings = ["0", "1/8", "1/4", "1/2"] + [str(i) for i in range(1, 31)]
possible_alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "Neutral", "Chaotic Neutral",
                       "Lawful Evil", "Neutral Evil", "Chaotic Evil"]

possible_npc_types = ["Quest Giver", "Ally", "Enemy", "Shopkeeper", "Service Provider", "Sources of Information",
                      "Worldbuilding"]

npc_template = """{
    "Name": "",
    "Race": "",
    "Alignment": "",
    "Visual Description": "",
    "Image generation prompt": "",
    "Type of NPC": "",
    "Information related to Type of NPC": "",
    "Personality": "",
    "Quirks": "",
    "Goals and Motivations": "",
    "Secrets": "",
    "Attitude towards PCs": "",
    "Additional Information": "",
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
    "Legendary Action Description": "",
    "Legendary Actions": [
        {
            "Name": "",
            "Description": ""
        }
    ],
}"""
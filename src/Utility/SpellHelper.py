possible_spell_levels = ["Cantrip", "1st", "2nd", "3rd"] + [str(i) + "th" for i in range(4, 10)]
possible_spell_schools = ["Abjuration", "Conjuration", "Divination", "Enchantment", "Evocation", "Illusion",
                          "Necromancy", "Transmutation"]
possible_spell_components = ["Verbal", "Somatic", "Material"]
possible_spell_casting_time = ["1 action", "1 bonus action", "1 reaction", "1 minute", "10 minutes", "1 hour",
                               "8 hours", "12 hours", "24 hours"]
possible_spell_durations = ["1 round", "1 minute", "10 minutes", "1 hour", "8 hours", "12 hours",
                            "24 hours", "1 day", "7 days", "10 days", "30 days", "Until dispelled"]
possible_spell_ranges = ["Self", "Touch", "5 feet", "10 feet", "30 feet", "60 feet", "120 feet", "500 feet",
                         "1 mile", "Unlimited"]
possible_spell_area_types = ["Cube", "Cone", "Cylinder", "Line", "Sphere"]
possible_spell_types = ["Attack", "Buff", "Debuff", "Healing", "Utility"]
possible_save_types = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
possible_damage_types = ["Acid", "Bludgeoning", "Cold", "Fire", "Force", "Lightning", "Necrotic", "Piercing",
                         "Poison", "Psychic", "Radiant", "Slashing", "Thunder"]
possible_conditions = ["Blinded", "Charmed", "Deafened", "Frightened", "Grappled", "Incapacitated", "Invisible",
                       "Paralyzed", "Petrified", "Poisoned", "Prone", "Restrained", "Stunned", "Unconscious"]

spell_template = """{
    "Name": "",
    "Level": "",
    "School": "",
    "Range": "",
    "Spell Components": "",
    "Material Components": "",
    "Casting Time": "",
    "Duration": "",
    "Requires Concentration": "",
    "Ritual": "",
    "Spell Type": "",
    "Save Type": "",
    "Spell Area": "",
    "Damage Type": "",
    "Condition": "",
    "Description": ""
}"""

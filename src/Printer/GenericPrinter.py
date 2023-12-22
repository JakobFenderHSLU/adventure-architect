import streamlit as st

from Utility.Utils import check_attribute, check_attributes


def display_text_list(attributes_to_print, generated_item):
    for attribute in attributes_to_print:
        if check_attribute(attribute, generated_item):
            st.write(f"##### {attribute}")
            st.write(f"{generated_item[attribute]}")


def display_stats(generated_item):
    if check_attribute("Stats", generated_item):
        # Add modifier to stats. eg. 14 -> 14 (+2)
        stats = {key: f"{value} ({'+' if (value - 10) // 2 >= 0 else '-'}{(value - 10) // 2})"
                 for key, value in generated_item["Stats"].items()}

        if check_attributes(["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"], stats):
            st.write(f"""
                |STR|DEX|CON|INT|WIS|CHA|
                |:---:|:---:|:---:|:---:|:---:|:---:|
                |{stats["Strength"]}|{stats["Dexterity"]}|{stats["Constitution"]}|{stats["Intelligence"]}|{stats["Wisdom"]}|{stats["Charisma"]}|
                """)


def display_skills(generated_item):
    skill_attributes = ["Saving Throws", "Skills", "Damage Vulnerabilities", "Damage Resistances", "Damage Immunities",
                        "Condition Immunities", "Senses", "Languages", "Challenge Rating"]

    attribute_print_string = ""
    for attribute in skill_attributes:
        if check_attribute(attribute, generated_item):
            attribute_print_string += f"""**{attribute}** {generated_item[attribute]}<br> """

    st.write(attribute_print_string, unsafe_allow_html=True)


def display_combat_information(generated_item):
    if check_attributes(["Armor Class", "Hit Points", "Speed"], generated_item):
        st.write(f"""
            **Armor Class** {generated_item['Armor Class']}<br> 
            **Hit Points**  {generated_item['Hit Points']}<br>
            **Speed** {generated_item['Speed']}
            """, unsafe_allow_html=True)


def display_actions(generated_item):
    if check_attribute("Actions", generated_item):
        st.write("### Actions")
        for action in generated_item["Actions"]:
            st.write(f"""**{action["Name"]}** {action["Description"]}""")
    if check_attribute("Bonus Actions", generated_item):
        st.write("### Bonus Actions")
        for action in generated_item["Bonus Actions"]:
            st.write(f"""**{action["Name"]}** {action["Description"]}""")
    if check_attribute("Legendary Actions", generated_item):
        st.write("### Legendary Actions")
        if check_attribute("Legendary Action Description", generated_item):
            st.write(generated_item["Legendary Action Description"])
        for action in generated_item["Legendary Actions"]:
            st.write(f"""**{action["Name"]}** {action["Description"]}""", unsafe_allow_html=True)
    if check_attribute("Lair Actions", generated_item):
        st.write("### Lair Actions")
        if check_attribute("Lair Action Description", generated_item):
            st.write(generated_item["Lair Action Description"])
        for action in generated_item["Lair Actions"]:
            st.write(f"""**{action["Name"]}** {action["Description"]}""", unsafe_allow_html=True)

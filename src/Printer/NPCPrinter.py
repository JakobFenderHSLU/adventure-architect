import streamlit as st

from Printer.GenericPrinter import display_actions, display_combat_information, display_skills, display_stats, \
    display_text_list
from Utility.Utils import check_attribute, check_attributes


def display_npc(generated_npc):
    display_title_information(generated_npc)
    st.write("___")

    if check_attribute("Image URL", generated_npc):
        st.image(generated_npc["Image URL"], width=400)

    display_text_list(
        ['Visual Description', 'Personality', 'Quirks', 'Goals and Motivations', 'Information related to Type of NPC',
         'Secrets', 'Attitude towards PCs', 'Additional Information'], generated_npc)
    st.write("___")
    display_combat_information(generated_npc)
    st.write("___")
    display_stats(generated_npc)
    st.write("___")
    display_skills(generated_npc)
    st.write("___")
    display_actions(generated_npc)


def display_title_information(generated_npc):
    if check_attribute("Name", generated_npc):
        st.write(f"## {generated_npc['Name']}")
    if check_attributes(["Race", "Alignment", "Type of NPC"], generated_npc):
        st.write(f"""
            *{generated_npc['Race']}, {generated_npc['Alignment']}, {generated_npc['Type of NPC']}*
            """)


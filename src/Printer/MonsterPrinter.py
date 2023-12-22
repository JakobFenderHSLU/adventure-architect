import streamlit as st

from Printer.GenericPrinter import display_actions, display_combat_information, display_skills, display_stats, \
    display_text_list
from Utility.Utils import check_attribute, check_attributes


def display_monster(generated_monster: dict):
    if check_attribute("Name", generated_monster):
        st.write(f"## {generated_monster['Name']}")
    if check_attributes(["Size", "Type", "Alignment", "Environment"], generated_monster):
        st.write(f"""
            *{generated_monster['Size']} {generated_monster['Type']}, {generated_monster['Alignment']}* 
            ({generated_monster['Environment']})
            """)

    display_combat_information(generated_monster)
    st.write("___")
    display_stats(generated_monster)
    st.write("___")
    display_skills(generated_monster)
    st.write("___")
    display_actions(generated_monster)
    st.write("___")

    display_text_list(["Visual Description", "Quirks", "Additional Information", "Tactics"], generated_monster)

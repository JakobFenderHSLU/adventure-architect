import streamlit as st

from Printer.GenericPrinter import display_text_list
from Utility.Utils import check_attribute, check_attributes


def display_spell(generated_spell: dict):
    postfix = ""
    if check_attribute("Requires Concentration", generated_spell):
        if generated_spell["Requires Concentration"] == "Yes":
            postfix += " (Concentration)"
    if check_attribute("Ritual", generated_spell):
        if generated_spell["Ritual"] == "Yes":
            postfix += " (Ritual)"

    if check_attribute("Name", generated_spell):
        st.write(f"### {generated_spell['Name']}{postfix}")
    col = st.columns(4)

    with col[0]:
        if check_attribute("Level", generated_spell):
            st.write("##### Level")
            st.write(f"{generated_spell['Level']}")
        if check_attribute("Duration", generated_spell):
            st.write("##### Duration")
            st.write(f"{generated_spell['Duration']}")

    with col[1]:
        if check_attribute("Casting Time", generated_spell):
            st.write("##### Casting Time")
            st.write(f"{generated_spell['Casting Time']}")
        if check_attribute("School", generated_spell):
            st.write("##### School")
            st.write(f"{generated_spell['School']}")

    with col[2]:
        if check_attribute("Range", generated_spell):
            st.write("##### Range")
            st.write(f"{generated_spell['Range']}")
        if check_attribute("Ritual", generated_spell):
            st.write("##### Ritual")
            st.write(f"{generated_spell['Ritual']}")

    with col[3]:
        if check_attribute("Spell Components", generated_spell):
            st.write("##### Components")
            st.write(f"{generated_spell['Spell Components']}")
        if check_attribute("Spell Type", generated_spell):
            st.write("##### Spell Type")
            st.write(f"{generated_spell['Spell Type']}")

    if check_attribute("Description", generated_spell):
        st.write(f"{generated_spell['Description']}")

    if check_attribute("Material Components", generated_spell):
        st.write(f"*-({generated_spell['Material Components']})*")


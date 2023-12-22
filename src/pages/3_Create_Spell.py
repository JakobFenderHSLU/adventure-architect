import streamlit as st

from Generator.MagicItemGenerator import generate_magic_item
from Generator.SpellGenerator import generate_spell
from Printer.MagicItemPrinter import display_item
from Printer.SpellPrinter import display_spell
from Utility.SpellHelper import possible_spell_levels, possible_spell_ranges, possible_spell_types, \
    possible_spell_components, possible_spell_schools, possible_save_types, possible_spell_area_types, \
    possible_damage_types, possible_conditions, possible_spell_casting_time, possible_spell_durations


st.set_page_config(layout="wide")
_, main, _ = st.columns([1, 3, 1])

with main:
    st.title("Create a Spell")
    st.write("This is a tool to generate flavourful spells for your D&D character. Note that these spells might not "
             "be balanced. Always double check with similar spells and use common sense.")

    with st.form("Spell Generator"):
        cols = st.columns(4)
        with cols[0]:
            selected_level = st.selectbox("Spell level:", ["Random"] + possible_spell_levels)
            selected_range = st.selectbox("Spell Range:", ["Random"] + possible_spell_ranges)
            selected_spell_type = st.selectbox("Spell Type:", ["Random"] + possible_spell_types)
            selected_components = st.multiselect("Spell Components:", ["Random"] + possible_spell_components,
                                                 default=possible_spell_components)

        with cols[1]:
            selected_school = st.selectbox("Spell School:", ["Random"] + possible_spell_schools)
            selected_save_type = st.selectbox("Save Type:", ["None", "Random"] + possible_save_types)
            selected_spell_area = st.selectbox("Spell Area:", ["None", "Random"] + possible_spell_area_types)

        with cols[2]:
            selected_requires_concentration = st.selectbox("Requires Concentration:", ["Random", "Yes", "No"])
            selected_damage_type = st.selectbox("Damage Type:", ["None", "Random"] + possible_damage_types)
            selected_condition = st.selectbox("Condition:", ["None", "Random"] + possible_conditions)

        with cols[3]:
            selected_ritual = st.selectbox("Ritual:", ["Random", "Yes", "No"], index=2)
            selected_casting_time = st.selectbox("Casting Time:", ["Random"] + possible_spell_casting_time)
            selected_spell_duration = st.selectbox("Spell Duration:", ["Random"] + possible_spell_durations)

        description_text = st.text_input("Enter prompt:", "", placeholder="A Spell that Gandalf the White would cast")

        submitted = st.form_submit_button("Submit")
        if submitted:
            with st.spinner('Creating your Spell...'):
                generated_spell = generate_spell(description_text, selected_level, selected_school, selected_range,
                                                 selected_components, selected_spell_type, selected_save_type,
                                                 selected_spell_area, selected_requires_concentration,
                                                 selected_damage_type, selected_condition, selected_ritual,
                                                 selected_casting_time, selected_spell_duration)
            if generated_spell is not None:
                display_spell(generated_spell)
            else:
                st.error("Something went wrong while parsing the response.")

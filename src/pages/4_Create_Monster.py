import streamlit as st

from Generator.MonsterGenerator import generate_monster
from Printer.MonsterPrinter import display_monster
from Printer.NPCPrinter import display_npc
from Utility.MonsterHelper import possible_environments, possible_monster_types, possible_size
from Utility.NPCHelper import possible_challenge_ratings

# set wide layout
st.set_page_config(layout="wide")
_, main, _ = st.columns([1, 3, 1])

with main:
    st.title("Create A Monster")
    st.write("This tool helps you to create memorable monsters on the fly.")

    with st.form("Monster Generator"):
        cols = st.columns(4)

        with cols[0]:
            selected_monster_type = st.selectbox("Monster Type:", ["Random"] + possible_monster_types)
            selected_legendary = st.selectbox("Legendary:", ["Random", "Yes", "No"], index=2)

        with cols[1]:
            selected_challenge_rating = st.selectbox("Challenge Rating:", ["Random"] + possible_challenge_ratings)
            selected_lair = st.selectbox("Lair:", ["Random", "Yes", "No"], index=2)

        with cols[2]:
            selected_size = st.selectbox("Size:", ["Random"] + possible_size, index=3)

        with cols[3]:
            selected_environment = st.selectbox("Environment:", ["Random"] + possible_environments)

        example_request = "The Dementors from Harry Potter, but they suck out your memories instead of your soul."
        description_text = st.text_input("Enter prompt:", "", placeholder=example_request)
        submitted = st.form_submit_button("Submit")
        if submitted:
            with st.spinner('Creating your Monster...'):
                generated_monster = generate_monster(description_text, selected_monster_type, selected_challenge_rating,
                                                     selected_size, selected_environment, selected_legendary,
                                                     selected_lair)

            if generated_monster is not None:
                display_monster(generated_monster)
            else:
                st.error("Something went wrong while parsing the response.")

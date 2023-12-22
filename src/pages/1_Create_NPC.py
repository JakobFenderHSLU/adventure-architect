import random

import streamlit as st

from Generator.NPCGenerator import generate_npc
from Printer.NPCPrinter import display_npc
from Utility.NPCHelper import possible_alignments, possible_races, possible_npc_types, possible_challenge_ratings

# set wide layout
st.set_page_config(layout="wide")
_, main, _ = st.columns([1, 3, 1])

with main:
    st.title("Create NPC")
    st.write("This tool helps you to generate NPCs on the fly. Especially useful if you have players that are "
             "easily distracted.")

    with st.form("NPC Generator"):
        cols = st.columns(4)

        with cols[0]:
            selected_race = st.selectbox("Race:", ["Random (Core)", "Random (All)"] + possible_races)

        with cols[1]:
            selected_alignment = st.selectbox("Alignment:", ["Random"] + possible_alignments)

        with cols[2]:
            selected_npc_type = st.selectbox("Type of NPC:", ["Random"] + possible_npc_types)

        with cols[3]:
            selected_challenge_rating = st.selectbox("Challenge Rating:", ["Random"] + possible_challenge_ratings)

        example_request = "A goblin with an extraordinary talent for cooking, running a cozy tavern that serves " \
                          "exotic and delicious dishes."
        description_text = st.text_input("Enter prompt:", "", placeholder=example_request)
        create_image = st.checkbox("I want an image of my NPC", value=False)
        # st.write("*Note: Images are expensive to generate and will take longer to load costing an average of "
        #          "0.04 cents per request*")
        submitted = st.form_submit_button("Submit")
        if submitted:
            with st.spinner('Creating your NPC...'):
                generated_npc = generate_npc(description_text, selected_race, selected_alignment, selected_npc_type,
                                             selected_challenge_rating, create_image)

            if generated_npc is not None:
                display_npc(generated_npc)
            else:
                st.error("Something went wrong while parsing the response.")


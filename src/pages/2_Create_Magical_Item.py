import streamlit as st

from Generator.MagicItemGenerator import generate_magic_item
from Printer.MagicItemPrinter import display_item
from Utility.ItemHelper import possible_item_rarities, possible_item_types

st.set_page_config(layout="wide")
_, main, _ = st.columns([1, 3, 1])

with main:
    st.title("Create a Magic Item")
    st.write("This tool is a resource for crafting captivating and immersive magic items to enrich your Dungeons " +
             "& Dragons campaign. Keep in mind that while these items are designed to add flavor and intrigue, " +
             "they may not always adhere to strict game balance. It's advisable to cross-reference them with " +
             "comparable spells and apply a touch of practicality when introducing them into your game world.")

    with st.form("Create Magic Item"):
        cols = st.columns(4)
        with cols[0]:
            selected_rarity = st.selectbox("Rarity:", ["Random"] + possible_item_rarities)

        with cols[1]:
            selected_type = st.selectbox("Item Type:", ["Random"] + possible_item_types)

        with cols[2]:
            requires_attunement = st.selectbox("Attunement:", ["Random", "Yes", "No"])

        with cols[3]:
            cursed = st.selectbox("Cursed:", ["Random", "Yes", "No"])

        example_prompt = "An item that can only be carried by the pure of heart"

        description_text = st.text_input("Enter prompt:", "", placeholder=example_prompt)
        submitted = st.form_submit_button("Submit")
        if submitted:
            with st.spinner('Creating your Magic Item...'):
                generated_item = generate_magic_item(description_text, selected_rarity, selected_type,
                                                     requires_attunement, cursed)
            if generated_item is not None:
                display_item(generated_item)
            else:
                st.error("Something went wrong while parsing the response.")

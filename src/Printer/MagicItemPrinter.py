import streamlit as st

from Printer.GenericPrinter import display_text_list
from Utility.Utils import check_attribute, check_attributes


def display_item(generated_magic_item):
    if check_attribute("Name", generated_magic_item):
        st.write(f"## {generated_magic_item['Name']}")

    if check_attributes(["Type", "Rarity", "Attunement", "Price"], generated_magic_item):
        attunement_text = ""
        if generated_magic_item["Attunement"] == "Yes":
            attunement_text = " (requires attunement)"
        subtype = ""
        if check_attribute("Subtype", generated_magic_item):
            subtype = f" ({generated_magic_item['Subtype']})"
        st.write(f"*{generated_magic_item['Type']}{subtype}, {generated_magic_item['Rarity']}{attunement_text}*")
        st.write(f"**{generated_magic_item['Price']} gp**")
    st.write("___")

    display_text_list(["Mechanical Description", "Visual Description", "Story", "Curse"], generated_magic_item)

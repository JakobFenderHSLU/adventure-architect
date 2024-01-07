import json
import random
import pandas as pd
import Utility.OpenAIConnection as OpenAIConnection
from Utility.NPCHelper import npc_template, possible_alignments, possible_challenge_ratings, possible_core_races, \
    possible_npc_types, possible_races
from Utility.Utils import check_attribute

balance_data = pd.read_csv("assets/balance_stats.csv")


def generate_npc(description, selected_race, selected_alignment, selected_npc_type, selected_challenge_rating,
                 create_image):
    chatgpt_messages = generate_npc_prompt(description, selected_alignment, selected_challenge_rating,
                                           selected_npc_type, selected_race)

    generated_npc = OpenAIConnection.generate_text(chatgpt_messages)
    if create_image:
        generated_npc["Image URL"] = generate_npc_portrait(generated_npc)
    return generated_npc


def generate_npc_prompt(description, selected_alignment, selected_challenge_rating, selected_npc_type,
                        selected_race):
    return_format = f"""
    THE RETURN FORMAT SHOULD ALWAYS BE PARSABLE TO JSON. 
    DO NOT USE LINE BREAKS. START WITH "{{" AND END WITH "}}". \n
    Return the NPC in the following format: \n
    {npc_template}
    """

    race_for_request = selected_race
    npc_type_for_request = selected_npc_type
    alignment_for_request = selected_alignment
    challenge_rating_for_request = selected_challenge_rating

    if selected_race == "Random (Core)":
        race_for_request = random.choice(possible_core_races)
    elif selected_race == "Random (All)":
        race_for_request = random.choice(possible_races)
    if selected_alignment == "Random":
        alignment_for_request = random.choice(possible_alignments)
    if selected_npc_type == "Random":
        npc_type_for_request = random.choice(possible_npc_types)
    if selected_challenge_rating == "Random":
        challenge_rating_for_request = random.choice(possible_challenge_ratings[:10])

    average_stats = balance_data[balance_data['CR'] == challenge_rating_for_request].iloc[0]

    attribute_explanation = f"""
    "Type of NPCs": Choose between {", ".join(possible_npc_types)} \n
    "Information related to Type of NPC": If "Type of NPC" is "Quest Giver" write Quest here, 
    if "Type of NPC" is "Shopkeeper" write Information on the Shop here,
    if "Type of NPC" is "Service Provider" write the provided Service here,
    if "Type of NPC" is "Sources of Information" write Information that the PCs can get here,
    if "Type of NPC" is "Worldbuilding" write Details on the World here \n
    "Legendary Action Description": Only fill out, if "Legendary Actions" is not empty \n
    "Image generation prompt": A prompt used to create an image with dall-e 3. This field needs to be filled out! 
     Add the Race, gender, racial features, and other optical features. Be descriptive and use adjectives.
    "Armor Class": The average Armor Class for your Challenge Rating is {average_stats["Armor Class"]}. You can 
    choose a different score!\n
    "Hit Points": The average Hit Points for your Challenge Rating is {average_stats["Hit Points"]}. You can
    choose a different amount, if it makes sense!\n
    "Actions": Add actions that your NPC can take. The average Variables for your Challenge Rating is as follows: \n
    Hit Bonus: {average_stats["Attack Bonus"]} \n
    Damage per Round: {average_stats["Average DPR"]} \n
    Save DC: {average_stats["Save DC"]} \n
    You can choose different values, if it makes sense!
    """

    prompt = f"""
    Create an NPC for Dungeons and Dragons. According to the previous format. Here is what I had in mind: \n
    Race: {race_for_request} \n
    Alignment: {alignment_for_request} \n
    Type of NPC: {npc_type_for_request} \n
    Challenge Rating: {challenge_rating_for_request} \n

    Description always has priority over the other attributes. \n
    Description: {description}
    """

    chatgpt_messages = [
        {"role": "system", "content": "Create an Non Player Character for Dungeons and Dragons."},
        {"role": "system", "content": return_format},
        {"role": "system", "content": attribute_explanation},
        {"role": "user", "content": prompt}
    ]

    return chatgpt_messages


def generate_npc_portrait(generated_npc):
    image_prompt = ""

    if check_attribute("Image generation prompt", generated_npc):
        image_prompt = generated_npc["Image generation prompt"]
    elif check_attribute("Visual Description", generated_npc):
        print("ERROR: No image generation prompt - falling back to Visual Description")
        image_prompt = generated_npc["Visual Description"]
    else:
        print("ERROR: No image generation prompt - skipping image generation")

    if image_prompt:
        image_url = OpenAIConnection.generate_image(image_prompt)
        return image_url
    else:
        return None

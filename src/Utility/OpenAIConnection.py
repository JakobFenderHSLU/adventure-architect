import json
from openai import OpenAI
import streamlit as st

saved_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=saved_key)


def generate_text(messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response_text = response.choices[0].message.content
    return parse_to_json(response_text)


def generate_text_raw(messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content


def generate_image(image_prompt):
    image_response = client.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return image_response.data[0].url


def parse_to_json(response_text: str, fix_using_chatgpt: bool = True):
    try:
        # Auto repair the response to be parsable json
        response_text = response_text.replace("\n", "")
        if not response_text.startswith("{"):
            response_text = "{" + response_text
        elif response_text.startswith("{{"):
            response_text = response_text[1:]

        if not response_text.endswith("}"):
            response_text = response_text + "}"
        elif response_text.endswith("}}"):
            response_text = response_text[:-1] + "}"

        response_json: dict = json.loads(response_text)
        return response_json

    except json.JSONDecodeError:
        if fix_using_chatgpt:
            print("ERROR: Could not parse response. Will try to fix it using chatGPT")
            messages = [
                {"role": "system", "content": "Repair this response so it can be parsed as JSON:"},
                {"role": "user", "content": response_text}
            ]
            # Try to fix the response using chatGPT
            response_text = generate_text_raw(messages)
            response_json = parse_to_json(response_text, fix_using_chatgpt=False)
            if response_json is not None:
                return response_json
            else:
                print("ERROR: Could not fix response using chatGPT")
        else:
            return None

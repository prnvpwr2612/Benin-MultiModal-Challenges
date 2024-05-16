import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from googletrans import LANGUAGES, Translator


# Function to translate text
def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)
    return translated_text.text


# Function to generate image from text
def generate_image_from_text(text):
    # Use the text-to-image model to generate the image
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": "Bearer your_huggingface_key"}

    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        image_bytes = response.content
        image = Image.open(BytesIO(image_bytes))
        return image
    else:
        return None


def main():
    st.title("Text to Image Generation")

    # Get all available languages supported by Google Translate
    available_languages = list(LANGUAGES.values())

    # Sidebar for language selection
    source_lang = st.sidebar.selectbox("Select Source Language", available_languages)
    target_lang = "en"  # Fixed target language as English for Stable Diffusion

    # Text input
    text_input = st.text_area("Enter text in the source language")

    # Generate image from text
    if st.button("Generate Image from Text"):
        if text_input:
            translated_text = translate_text(text_input, source_lang, target_lang)
            image = generate_image_from_text(translated_text)
            if image:
                st.image(image, caption="Generated Image", use_column_width=True)
                st.write("English Translated Prompt: ", translated_text)
            else:
                st.error("Failed to generate image. Please try again.")


if __name__ == "__main__":
    main()

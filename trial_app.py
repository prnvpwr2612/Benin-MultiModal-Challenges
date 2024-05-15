
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from googletrans import Translator
from transformers import CLIPProcessor, CLIPModel
import torch

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)
    return translated_text.text

# Function to transcribe and translate audio
def transcribe_and_translate_audio(audio_file, source_lang, target_lang):
    # Use the speech recognition model to transcribe the audio
    transcribed_text = speech_recognition_model.transcribe(audio_file, source_lang)
    
    # Translate the transcribed text
    translated_text = translate_text(transcribed_text, source_lang, target_lang)
    return translated_text

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
def generate_image_from_text(text):
    inputs = processor(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(inputs.input_ids)
    image = outputs[0].numpy()
    return image

def main():
    st.title("Text and Audio to Image Generation")

    # Sidebar for language selection
    source_lang = st.sidebar.selectbox("Select Source Language", ["English", "Fon", "Yoruba", "Dendi"])
    target_lang = st.sidebar.selectbox("Select Target Language", ["English", "French"])

    # Text input
    text_input = st.text_area("Enter text in the source language")

    # Audio input
    audio_file = st.file_uploader("Upload an audio file in the source language", type=["wav", "mp3"])

    # Generate image from text
    if st.button("Generate Image from Text"):
        if text_input:
            translated_text = translate_text(text_input, source_lang, target_lang)
            image = generate_image_from_text(translated_text)
            st.image(image, caption="Generated Image", use_column_width=True)

    # Generate image from audio
    if st.button("Generate Image from Audio"):
        if audio_file is not None:
            audio_bytes = audio_file.read()
            translated_text = transcribe_and_translate_audio(audio_bytes, source_lang, target_lang)
            image = generate_image_from_text(translated_text)
            st.image(image, caption="Generated Image", use_column_width=True)

if __name__ == "__main__":
    main()
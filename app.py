
import streamlit as st
import openai
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

# OpenAI API anahtarını buraya girin
openai.api_key = "YOUR_OPENAI_API_KEY"

st.title("📷 Metinden Görsel Üreten Yapay Zeka")
text = st.text_area("Metni girin:")

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512",
        model="dall-e-3"
    )
    return response['data'][0]['url']

def create_prompt(sentence):
    return f"photo-realistic image illustrating: {sentence.strip()}"

if st.button("Görselleri Üret"):
    if text.strip():
        sentences = sent_tokenize(text)
        for i, sentence in enumerate(sentences):
            with st.spinner(f"Görsel üretiliyor: {sentence}"):
                prompt = create_prompt(sentence)
                image_url = generate_image(prompt)
                st.image(image_url, caption=sentence)
    else:
        st.warning("Lütfen metin girin.")

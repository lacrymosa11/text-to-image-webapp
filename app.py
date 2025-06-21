
import streamlit as st
import openai

st.set_page_config(page_title="Metinden Görsel Üret", layout="wide")
st.title("📷 Metin Anlatımından Görsel Üretme")

openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_image(prompt):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    return response.data[0].url

text = st.text_area("Metni girin", height=200)
if st.button("Görselleri Üret") and text:
    with st.spinner("Görseller üretiliyor..."):
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        for i, sentence in enumerate(sentences, 1):
            image_prompt = sentence
            try:
                image_url = generate_image(image_prompt)
                st.image(image_url, caption=f"{i}. Görsel: {sentence}", use_column_width=True)
            except Exception as e:
                st.error(f"Görsel oluşturulamadı: {e}")

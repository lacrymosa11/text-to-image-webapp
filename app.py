import streamlit as st
import openai

st.set_page_config(page_title="Metinden Görsel Üret", layout="wide")

st.title("🖼️ Metinden Foto-Gerçekçi Görseller")

# API anahtarını al
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Kullanıcıdan metin girişi
text = st.text_area("Metin girin:", height=200, placeholder="Örnek: John Amerikalı bir deniz subayıydı. Tehlikeli bir göreve atanmıştı.")

if st.button("Görselleri Oluştur"):
    if not text.strip():
        st.warning("Lütfen bir metin girin.")
    else:
        # Noktaya göre böl (basit cümle ayrımı)
        sentences = [s.strip() for s in text.split('.') if s.strip()]

        for i, sentence in enumerate(sentences):
            st.markdown(f"### {i+1}. Cümle: {sentence}")
            try:
                with st.spinner("Görsel üretiliyor..."):
                    response = openai.images.generate(
                        model="dall-e-3",
                        prompt=sentence,
                        size="1024x1024",
                        quality="standard",
                        n=1,
                    )
                    image_url = response.data[0].url
                    st.image(image_url, caption=sentence, use_column_width=True)
            except Exception as e:
                st.error(f"Görsel oluşturulamadı: {e}")
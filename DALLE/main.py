from openai import OpenAI
import streamlit as st

client = OpenAI(api_key="***Your OpenAI API key***")

st.title("DALL-E Image Generator")

prompt = st.text_input("Enter your prompt to generate an image:", value="")

if st.button("Generate Image"):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        
        st.image(image_url, caption=f"Generated Image for: '{prompt}'", use_column_width=True)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

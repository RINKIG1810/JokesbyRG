import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'  # Replace 'your_openai_api_key' with your actual key

def get_joke_from_openai(word):
    try:
        # Generate a joke using OpenAI's completion API
        prompt = f"Tell me a joke about {word}."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=60
        )
        # Extract and return the joke text
        joke = response.choices[0].text.strip()
        return joke
    except Exception as e:
        # If there's an error, return a message with the error details
        return f"An error occurred while generating the joke: {e}"

# Streamlit UI
st.set_page_config(page_title="Joke Generator", page_icon="😂")
st.title("Word-Based Joke Generator")

st.write("Enter any word to get a joke:")

# Input field for the word
word = st.text_input("Enter a word:")

if st.button("Get a Joke"):
    if word:
        # Fetch and display a joke from OpenAI
        joke = get_joke_from_openai(word)
        st.write(joke)
    else:
        st.write("Please enter a word to get a joke.")

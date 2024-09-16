import streamlit as st
import random

# Predefined dictionary of jokes based on keywords
jokes_dict = {
    "dog": [
        "Why did the dog sit in the shade? Because it didn't want to be a hot dog!",
        "What do you call a dog magician? A labracadabrador."
    ],
    "cat": [
        "Why was the cat sitting on the computer? Because it wanted to keep an eye on the mouse!",
        "Why don't cats play poker in the jungle? Too many cheetahs!"
    ],
    "computer": [
        "Why did the computer show up at work late? It had a hard drive.",
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    ],
    # Add more keywords and jokes here
}

def get_joke(word):
    # Find jokes associated with the given word
    jokes = jokes_dict.get(word.lower(), ["Sorry, I don't have a joke for that word."])
    return random.choice(jokes)

# Streamlit UI
st.title("Word-Based Joke Generator")

# Input field for the word
word = st.text_input("Enter a word:")

if st.button("Get a Joke"):
    # Fetch and display a joke
    joke = get_joke(word)
    st.write(joke)


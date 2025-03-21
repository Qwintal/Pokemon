import streamlit as st
import random 
import pandas as pd

st.title("who's the pokemon??")
st.logo("Sprits/pokeball.png")

df = pd.read_csv('pokemon.csv')

# Function to get Pokémon name by Pokédex number
def get_pokemon_name(pokedex_num):
    pokemon = df[df['pokedex_number'] == pokedex_num]
    if not pokemon.empty:
        return pokemon['name'].values[0].lower()  # Case-insensitive comparison
    return None


# Use session state to persist the random Pokémon across reruns
if 'pokemon_id' not in st.session_state:
    st.session_state.pokemon_id = random.randint(1, 721)
    st.session_state.correct_answer = get_pokemon_name(st.session_state.pokemon_id)
    st.session_state.guess_submitted = False

# Display the Pokémon image
image_path = f"C:/Users/Mrank/Python/Sprits/{st.session_state.pokemon_id}.png"
try:
    st.image(image_path, caption="Who’s this Pokémon?", width=200)
except:
    st.write("Image not available for this Pokémon.")

# User input for guessing the name
user_guess = st.text_input("Enter the Pokémon’s name:", key="guess_input").lower()

# Button to submit the guess
if st.button("Submit Guess", key="submit_guess"):
    st.session_state.guess_submitted = True

# Check the guess and provide feedback
if st.session_state.guess_submitted:
    if user_guess == st.session_state.correct_answer:
        st.success(f"Correct! This is {st.session_state.correct_answer.capitalize()}!")
    else:
        st.error(f"Wrong! The correct answer was {st.session_state.correct_answer.capitalize()}.")

# Button to try a new Pokémon
if st.button("Try Another Pokémon", key="new_pokemon"):
    st.session_state.pokemon_id = random.randint(1, 721)
    st.session_state.correct_answer = get_pokemon_name(st.session_state.pokemon_id)
    st.session_state.guess_submitted = False
    st.rerun()



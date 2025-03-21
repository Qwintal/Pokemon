# loading data frame 
import pandas as pd
import os
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("pokemon.csv")

# checking the working directory
# manually move file to the working directory 
os.getcwd()

# checking if the file loaded properly
df.head() # first 5 rows 
df.tail() # last 5 columns 
df.info() # no:of columns, their type

# how many columns has missing values 
# manually go and correct them 
print(df.isnull().sum())
# values like - type2, percentage_male
# will have null values
# (some pokemon don't have second type)
# (some pokemon species are genderless)

# checking for duplication rows 
print(df.duplicated().sum())

# converting all text in lower
# .lower() - work on single column at a time 
df["name"] = df["name"].str.lower()
df["type1"] = df["type1"].str.lower()
df["type2"] = df["type2"].str.lower()
df["japanese_name"] = df["japanese_name"].str.lower()
df["classfication"] = df["classfication"].str.lower()
df["abilities"] = df["abilities"].str.lower()

# Basic Analysis
print(df.describe())

# Streamlit app
# How to run - on command type "streamlit run pokemon.py"
# page 1

# Load the dataset (replace with your dataset path)
df = pd.read_csv('pokemon.csv')
st.logo("Sprits/pokeball.png")
col1, col2 = st.columns([3,2])
with col1:
    st.title("Pokémon Pokedex") 
with col2:
    st.image("Sprits/pokedex.png", width=230)

# page 2
# Dropdown to select a Pokémon
pokemon_names = df['name'].tolist()
selected_pokemon = st.selectbox("Choose a Pokémon", pokemon_names)

# Button to view details
if st.button("View Details"):
    # Set the query parameter to the selected Pokémon and rerun
    st.query_params["pokemon"] = selected_pokemon
    st.rerun()

# Get the selected Pokémon from query parameters
selected_pokemon = st.query_params.get("pokemon", None)

if selected_pokemon:
    # Filter the dataset for the selected Pokémon
    pokemon_data = df[df['name'] == selected_pokemon]
    
    if not pokemon_data.empty:
        st.subheader(f"Details for {selected_pokemon}")
        
        col1, col2 = st.columns([1,2])

        with col1:
            pokedex_num = pokemon_data['pokedex_number'].values[0]
            image_path = f"Sprits/{pokedex_num}.png"

            try:
                st.image(image_path, caption=selected_pokemon)
            except:
                st.write("Image not available")

        with col2:
             # Display basic information
            st.write("**Pokédex Number:**", pokemon_data['pokedex_number'].values[0])
            st.write("**Type:**", pokemon_data['type1'].values[0], "/", pokemon_data['type2'].values[0] if 'type2' in df.columns else "")
            st.write("**Generation:**",pokemon_data["generation"].values[0])
            legendary_value = pokemon_data["is_legendary"].values[0]
            legendary_text = "Yes" if legendary_value == 1 else "No"
            st.write("**Legendary:**", legendary_text)
            st.write("**Height (meters):**",pokemon_data["height_m"].values[0])
            st.write("**Weight (kg):**",pokemon_data["weight_kg"].values[0])
            st.write("**Abilities:**",pokemon_data["abilities"].values[0])
            st.write("**Total Base Stat:**",pokemon_data["base_total"].values[0])

        # Display stats
        st.subheader("Stats")
        stats = ['attack', 'defense', 'sp_attack', 'sp_defense', 'speed',"hp"]
        stats_data = pokemon_data[stats].iloc[0]

        
        # Create a bar chart for stats
        fig, ax = plt.subplots(facecolor="black")
        ax.set_facecolor('black')
        stats_data.plot(kind='barh', ax=ax, color="lightblue")
        ax.set_title(f"{selected_pokemon}'s Stats",color='white')
        ax.set_ylabel("Value",color='white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        st.pyplot(fig)
        
        # Back button to return to the main page
        if st.button("Back to List"):
            st.query_params.clear()
            st.rerun()
    else:
        st.error("Pokémon not found.")
else:
    st.write("No Pokémon selected. Please go back to the main page.")

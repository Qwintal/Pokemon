import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Load the dataset (replace with your dataset path)
df = pd.read_csv('pokemon.csv')
st.logo("Sprits/pokeball.png",)

# Create two columns for layout
col1, col2 = st.columns([3, 3])

with col1:
    # Dropdown to select a Pokémon (with unique key)
    pokemon_names = df['name'].tolist()
    selected_pokemon_1 = st.selectbox("Choose a Pokémon", pokemon_names, key="pokemon_selector_1")

    # Button to view details
    if st.button("View Details", key="view_button_1"):
        # Set the query parameter to the selected Pokémon and rerun
        st.query_params["pokemon_1"] = selected_pokemon_1
        st.rerun()

    # Get the selected Pokémon from query parameters
    selected_pokemon_1 = st.query_params.get("pokemon_1", None)

    if selected_pokemon_1:
        # Filter the dataset for the selected Pokémon
        pokemon_data = df[df['name'] == selected_pokemon_1]
    
        if not pokemon_data.empty:
            st.subheader(f"Details for {selected_pokemon_1}")
        
            col1_inner, col2_inner = st.columns([1, 2])

            with col1_inner:
                pokedex_num = pokemon_data['pokedex_number'].values[0]
                image_path = f"Sprits/{pokedex_num}.png"
                try:
                    st.image(image_path, caption=selected_pokemon_1)
                except:
                    st.write("Image not available")

            with col2_inner:
                # Display basic information
                st.write("**Pokédex Number:**", pokemon_data['pokedex_number'].values[0])
                st.write("**Type:**", pokemon_data['type1'].values[0], "/", pokemon_data['type2'].values[0] if 'type2' in df.columns else "")
                st.write("**Generation:**", pokemon_data["generation"].values[0])
                legendary_value = pokemon_data["is_legendary"].values[0]
                legendary_text = "Yes" if legendary_value == 1 else "No"
                st.write("**Legendary:**", legendary_text)
                st.write("**Height (meters):**", pokemon_data["height_m"].values[0])
                st.write("**Weight (kg):**", pokemon_data["weight_kg"].values[0])
                st.write("**Abilities:**", pokemon_data["abilities"].values[0])
                st.write("**Total Base Stat:**", pokemon_data["base_total"].values[0])

            # Display stats
            st.subheader("Stats")
            stats = ['attack', 'defense', 'sp_attack', 'sp_defense', 'speed', "hp"]
            stats_data = pokemon_data[stats].iloc[0]

            # Create a bar chart for stats
            fig, ax = plt.subplots(facecolor="black")
            ax.set_facecolor('black')
            stats_data.plot(kind='barh', ax=ax, color="lightblue")
            ax.set_title(f"{selected_pokemon_1}'s Stats", color='white')
            ax.set_ylabel("Value", color='white')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            st.pyplot(fig)
        
            # Back button to return to the main page
            if st.button("Back to List", key="back_button_1"):
                st.query_params.clear()
                st.rerun()
        else:
            st.error("Pokémon not found.")
    else:
        st.write("No Pokémon selected. Please choose a Pokémon above.")

with col2:
    # Dropdown to select a Pokémon (with unique key)
    pokemon_names = df['name'].tolist()
    selected_pokemon_2 = st.selectbox("Choose a Pokémon", pokemon_names, key="pokemon_selector_2")

    # Button to view details
    if st.button("View Details", key="view_button_2"):
        # Set the query parameter to the selected Pokémon and rerun
        st.query_params["pokemon_2"] = selected_pokemon_2
        st.rerun()

    # Get the selected Pokémon from query parameters
    selected_pokemon_2 = st.query_params.get("pokemon_2", None)

    if selected_pokemon_2:
        # Filter the dataset for the selected Pokémon
        pokemon_data = df[df['name'] == selected_pokemon_2]
    
        if not pokemon_data.empty:
            st.subheader(f"Details for {selected_pokemon_2}")
        
            col1_inner, col2_inner = st.columns([1, 2])

            with col1_inner:
                pokedex_num = pokemon_data['pokedex_number'].values[0]
                image_path = f"Sprits/{pokedex_num}.png"
                try:
                    st.image(image_path, caption=selected_pokemon_2)
                except:
                    st.write("Image not available")

            with col2_inner:
                # Display basic information
                st.write("**Pokédex Number:**", pokemon_data['pokedex_number'].values[0])
                st.write("**Type:**", pokemon_data['type1'].values[0], "/", pokemon_data['type2'].values[0] if 'type2' in df.columns else "")
                st.write("**Generation:**", pokemon_data["generation"].values[0])
                legendary_value = pokemon_data["is_legendary"].values[0]
                legendary_text = "Yes" if legendary_value == 1 else "No"
                st.write("**Legendary:**", legendary_text)
                st.write("**Height (meters):**", pokemon_data["height_m"].values[0])
                st.write("**Weight (kg):**", pokemon_data["weight_kg"].values[0])
                st.write("**Abilities:**", pokemon_data["abilities"].values[0])
                st.write("**Total Base Stat:**", pokemon_data["base_total"].values[0])

            # Display stats
            st.subheader("Stats")
            stats = ['attack', 'defense', 'sp_attack', 'sp_defense', 'speed', "hp"]
            stats_data = pokemon_data[stats].iloc[0]

            # Create a bar chart for stats
            fig, ax = plt.subplots(facecolor="black")
            ax.set_facecolor('black')
            stats_data.plot(kind='barh', ax=ax, color="lightblue")
            ax.set_title(f"{selected_pokemon_2}'s Stats", color='white')
            ax.set_ylabel("Value", color='white')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            st.pyplot(fig)
        
            # Back button to return to the main page
            if st.button("Back to List", key="back_button_2"):
                st.query_params.clear()
                st.rerun()
        else:
            st.error("Pokémon not found.")
    else:
        st.write("No Pokémon selected. Please choose a Pokémon above.")

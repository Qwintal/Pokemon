import streamlit as st
import pandas as pd

# Set page title and logo
st.title("Advanced Pokémon Search")
st.logo("C:/Users/Mrank/Python/Sprits/pokeball.png")

# Load the dataset
df = pd.read_csv("pokemon.csv")

# Sidebar for filters
st.sidebar.header("Filter Pokémon")

# Type filter
type_selected = st.sidebar.selectbox('Choose a Type', ['All'] + sorted(df['type1'].unique().tolist()), key="type_filter")
filtered_df = df if type_selected == 'All' else df[df['type1'] == type_selected]

# Height filter (less than or greater than)
height_option = st.sidebar.selectbox("Height Filter", ["Any", "Less Than", "Greater Than"], key="height_option")
if height_option != "Any":
    height_value = st.sidebar.slider("Height (meters)", 0.0, float(df['height_m'].max()), 1.0, step=0.1, key="height_value")
    if height_option == "Less Than":
        filtered_df = filtered_df[filtered_df['height_m'] <= height_value]
    elif height_option == "Greater Than":
        filtered_df = filtered_df[filtered_df['height_m'] >= height_value]

# Weight filter (less than or greater than)
weight_option = st.sidebar.selectbox("Weight Filter", ["Any", "Less Than", "Greater Than"], key="weight_option")
if weight_option != "Any":
    weight_value = st.sidebar.slider("Weight (kg)", 0.0, float(df['weight_kg'].max()), 10.0, step=1.0, key="weight_value")
    if weight_option == "Less Than":
        filtered_df = filtered_df[filtered_df['weight_kg'] <= weight_value]
    elif weight_option == "Greater Than":
        filtered_df = filtered_df[filtered_df['weight_kg'] >= weight_value]

# Generation filter
generation_selected = st.sidebar.selectbox("Choose a Generation", ['All'] + sorted(df['generation'].unique().tolist()), key="gen_filter")
filtered_df = filtered_df if generation_selected == 'All' else filtered_df[filtered_df['generation'] == generation_selected]

# Ability filter (Note: This can be tricky if abilities are stored as lists or strings)
# Assuming 'abilities' column contains comma-separated strings or single values
ability_list = sorted(set([ability.strip("[]'") for sublist in df['abilities'].str.split(', ') for ability in sublist]))
ability_selected = st.sidebar.selectbox("Choose an Ability", ['All'] + ability_list, key="ability_filter")
if ability_selected != 'All':
    filtered_df = filtered_df[filtered_df['abilities'].str.contains(ability_selected, case=False, na=False)]

# Stat filters (using sliders for ranges)
attack_range = st.sidebar.slider("Attack Range", 0, int(df['attack'].max()), (0, int(df['attack'].max())), key="attack_range")
filtered_df = filtered_df[(filtered_df['attack'] >= attack_range[0]) & (filtered_df['attack'] <= attack_range[1])]

hp_range = st.sidebar.slider("HP Range", 0, int(df['hp'].max()), (0, int(df['hp'].max())), key="hp_range")
filtered_df = filtered_df[(filtered_df['hp'] >= hp_range[0]) & (filtered_df['hp'] <= hp_range[1])]

defense_range = st.sidebar.slider("Defense Range", 0, int(df['defense'].max()), (0, int(df['defense'].max())), key="defense_range")
filtered_df = filtered_df[(filtered_df['defense'] >= defense_range[0]) & (filtered_df['defense'] <= defense_range[1])]

sp_defense_range = st.sidebar.slider("Special Defense Range", 0, int(df['sp_defense'].max()), (0, int(df['sp_defense'].max())), key="sp_defense_range")
filtered_df = filtered_df[(filtered_df['sp_defense'] >= sp_defense_range[0]) & (filtered_df['sp_defense'] <= sp_defense_range[1])]

sp_attack_range = st.sidebar.slider("Special Attack Range", 0, int(df['sp_attack'].max()), (0, int(df['sp_attack'].max())), key="sp_attack_range")
filtered_df = filtered_df[(filtered_df['sp_attack'] >= sp_attack_range[0]) & (filtered_df['sp_attack'] <= sp_attack_range[1])]

speed_range = st.sidebar.slider("Speed Range", 0, int(df['speed'].max()), (0, int(df['speed'].max())), key="speed_range")
filtered_df = filtered_df[(filtered_df['speed'] >= speed_range[0]) & (filtered_df['speed'] <= speed_range[1])]

# Total Base Stat filter
base_total_range = st.sidebar.slider("Total Base Stat Range", 0, int(df['base_total'].max()), (0, int(df['base_total'].max())), key="base_total_range")
filtered_df = filtered_df[(filtered_df['base_total'] >= base_total_range[0]) & (filtered_df['base_total'] <= base_total_range[1])]

# Legendary filter
legendary_filter = st.sidebar.checkbox("Show Only Legendary", key="legendary_filter")
if legendary_filter:
    filtered_df = filtered_df[filtered_df['is_legendary'] == 1]

# Display the filtered dataframe
st.write(f"Showing {len(filtered_df)} Pokémon matching your criteria:")
st.dataframe(filtered_df)

# Optional: Reset filters button
if st.sidebar.button("Reset Filters", key="reset_filters"):
    st.rerun()

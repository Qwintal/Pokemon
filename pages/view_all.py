import streamlit as st
import pandas as pd

st.logo("C:/Users/Mrank/Python/Sprits/pokeball.png",)
df = pd.read_csv("pokemon.csv")
st.title("All Pokemon in Database \n (till Gen 7)")
selected_columns = ["pokedex_number","name","type1","type2","base_total","classfication","height_m","weight_kg","percentage_male","generation","is_legendary"]
df_selected = df[selected_columns]
st.dataframe(df_selected)

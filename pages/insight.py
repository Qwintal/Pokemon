import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.title("Graphs and insight")
st.logo("Sprits/pokeball.png")

df =pd.read_csv("pokemon.csv")

# Set a title for the Streamlit page
st.subheader("Pokémon HP Distribution")

# Create the histogram
fig, ax = plt.subplots()  # Create a figure and axis object
df["hp"].hist(ax=ax)      # Plot the histogram on the axis
ax.set_title("HP Distribution")  # Set the title
ax.set_xlabel("HP")       # Optional: Add x-axis label
ax.set_ylabel("Count")    # Optional: Add y-axis label

# Display the plot in Streamlit
st.pyplot(fig)
st.write("This majority of pokemons hp stats lies between 50 - 70")


# No:of pokemon of different types
st.subheader("Number of Pokémon by Type Combination")
df['type_combo'] = df['type1'] + " / " + df['type2'].fillna("")
type_counts = df["type_combo"].value_counts()
st.write(type_counts)
st.write("Major pokemon are of water or normal types, and many pokemon types are still unexplored.")

# Top 10 pokemon with higest base stats total
st.subheader("Top 10 Pokémon with Highest Base Stats Total")
top_10 = df.nlargest(10, "base_total")[["name", "base_total"]]
st.write("Here are the top 10 Pokémon based on their total base stats:")
st.dataframe(top_10)

# Pokemon type which have highest average attack stats
st.subheader("Pokémon Types by Average Attack Stat")
avg_attack = df.groupby('type1')['attack'].mean().sort_values(ascending=False)
st.write("Average attack stats by Pokémon type (highest to lowest):")
st.dataframe(avg_attack.rename("Average Attack").to_frame())  
top_type = avg_attack.index[0]
top_value = avg_attack.iloc[0]
st.write(f"The type with the highest average attack is **{top_type}** with an average of **{top_value:.2f}**.")

# Pokemon type which have highest average special attack stats
st.subheader("Pokémon Types by Average Special Attack Stat")
avg_special_attack = df.groupby('type1')['sp_attack'].mean().sort_values(ascending=False)
st.write("Average special attack stats by Pokémon type (highest to lowest):")
st.dataframe(avg_special_attack.rename("Average Special Attack").to_frame())
top_type = avg_special_attack.index[0]
top_value = avg_special_attack.iloc[0]
st.write(f"The type with the highest average special attack is **{top_type}** with an average of **{top_value:.2f}**.")

# Pokemon type which have highest average HP stats
st.subheader("Pokémon Types by Average HP Stat")
avg_hp = df.groupby('type1')['hp'].mean().sort_values(ascending=False)
st.write("Average HP stats by Pokémon type (highest to lowest):")
st.dataframe(avg_hp.rename("Average HP").to_frame())
top_type = avg_hp.index[0]
top_value = avg_hp.iloc[0]
st.write(f"The type with the highest average HP is **{top_type}** with an average of **{top_value:.2f}**.")

# Pokemon type which have highest average Defense stats
st.subheader("Pokémon Types by Average Defense Stat")
avg_defence = df.groupby('type1')['defense'].mean().sort_values(ascending=False)
st.write("Average defence stats by Pokémon type (highest to lowest):")
st.dataframe(avg_defence.rename("Average Defense").to_frame())
top_type = avg_defence.index[0]
top_value = avg_defence.iloc[0]
st.write(f"The type with the highest average defence is **{top_type}** with an average of **{top_value:.2f}**.")

# Pokemon type which have highest average Special defence  stats
st.subheader("Pokémon Types by Average Special Defence Stat")
avg_sp_defence = df.groupby('type1')['sp_defense'].mean().sort_values(ascending=False)
st.write("Average special defence stats by Pokémon type (highest to lowest):")
st.dataframe(avg_sp_defence.rename("Average Special Defence").to_frame())
top_type = avg_sp_defence.index[0]
top_value = avg_sp_defence.iloc[0]
st.write(f"The type with the highest average special defense is **{top_type}** with an average of **{top_value:.2f}**.")

# Pokemon type which have highest average speed stats
st.subheader("Pokémon Types by Average Speed Stat")
avg_speed = df.groupby('type1')['speed'].mean().sort_values(ascending=False)
st.write("Average speed stats by Pokémon type (highest to lowest):")
st.dataframe(avg_speed.rename("Average Speed").to_frame())
top_type = avg_speed.index[0]
top_value = avg_speed.iloc[0]
st.write(f"The type with the highest average speed is **{top_type}** with an average of **{top_value:.2f}**.")

# Pokemon type which have highest base stat total
st.subheader("Pokémon Types by Average Total Base Stat")
avg_base_total = df.groupby('type1')['base_total'].mean().sort_values(ascending=False)
st.write("Average total base stats by Pokémon type (highest to lowest):")
st.dataframe(avg_base_total.rename("Average Base Total").to_frame())
top_type = avg_base_total.index[0]
top_value = avg_base_total.iloc[0]
st.write(f"The type with the highest average base total is **{top_type}** with an average of **{top_value:.2f}**.")

# Legendary vs Non-Legendary
st.subheader("Average Base Total: Legendary vs. Non-Legendary Pokémon")
legendary_avg = df[df['is_legendary'] == 1]['base_total'].mean()
non_legendary_avg = df[df['is_legendary'] == 0]['base_total'].mean()
st.write(f"**Legendary Average Base Total:** {legendary_avg:.2f}")
st.write(f"**Non-Legendary Average Base Total:** {non_legendary_avg:.2f}")



# Piechart of pokemon types
st.subheader("Frequency of Pokémon Types")
type_counts = df['type1'].value_counts()
st.write("Frequency of each Pokémon type (based on Type 1):")
st.dataframe(type_counts.rename("Count").to_frame())
st.write("### Pie Chart of Pokémon Type Distribution")
fig1, ax1 = plt.subplots(figsize=(8, 8))
ax1.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
ax1.axis('equal')  # Equal aspect ratio ensures pie is a circle
st.pyplot(fig1)

# Comparing between different generations
st.subheader("Pokémon Stat Distribution Comparison")
st.write("Compare the distribution of each stat across Pokémon types or generations.")
comparison_mode = st.selectbox("Compare by:", ["Type", "Generation"], key="comparison_mode")
stats = ['hp', 'speed', 'attack', 'sp_attack', 'defense', 'sp_defense', 'base_total']
if comparison_mode == "Type":
    filter_key = 'type1'
    filter_options = df['type1'].unique().tolist()
    filter_label = "Select Types to Compare"
else:
    filter_key = 'generation'
    filter_options = sorted(df['generation'].unique().tolist())
    filter_label = "Select Generations to Compare"
selected_filters = st.multiselect(filter_label, filter_options, default=filter_options[:3], key="filter_select")
filtered_df = df[df[filter_key].isin(selected_filters)]
for stat in stats:
    st.subheader(f"Distribution of {stat.capitalize()} by {comparison_mode}")
    fig, ax = plt.subplots(figsize=(10, 6))
    data_to_plot = [filtered_df[filtered_df[filter_key] == f][stat].dropna() for f in selected_filters]
    ax.boxplot(data_to_plot, labels=selected_filters)
    ax.set_title(f"{stat.capitalize()} Distribution by {comparison_mode}", fontsize=16)
    ax.set_xlabel(comparison_mode, fontsize=12)
    ax.set_ylabel(stat.capitalize(), fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    if len(selected_filters) > 5:
        ax.tick_params(axis='x', rotation=45) 
    st.pyplot(fig)

# How many new pokemon are add each generation
st.subheader("Percentage of New Pokémon Added per Generation")
st.write("This app shows the percentage of new Pokémon introduced in each generation relative to the total Pokémon up to that point.")
gen_data = {'Generation': [1, 2, 3, 4, 5, 6, 7],'New_Pokemon': [151, 100, 135, 107, 156, 72, 88]  }
df = pd.DataFrame(gen_data)
df['Cumulative_Total'] = df['New_Pokemon'].cumsum()
df['Percentage_New'] = (df['New_Pokemon'] / df['Cumulative_Total']) * 100
st.subheader("New Pokémon by Generation")
st.dataframe(df)
st.write(f"**Generation 1** starts with {df['New_Pokemon'][0]} Pokémon (100% of the total at that point).")
st.write(f"**Generation 5** added the most new Pokémon: {df['New_Pokemon'][4]}.")
st.write(f"**Generation 6** added the fewest: {df['New_Pokemon'][5]}.")
st.subheader("Percentage of New Pokémon per Generation (Bar Chart)")
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(df['Generation'], df['Percentage_New'], color='skyblue')
ax1.set_title("Percentage of New Pokémon Added per Generation", fontsize=16)
ax1.set_xlabel("Generation", fontsize=12)
ax1.set_ylabel("Percentage of Total (%)", fontsize=12)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(df['Percentage_New']):
    ax1.text(i + 1, v + 1, f"{v:.1f}%", ha='center', fontsize=10)
st.pyplot(fig1)

# Gender 
st.subheader("Pokemon Gender")
df=pd.read_csv("pokemon.csv")
male_prob = (df['percentage_male'].fillna(0) / 100).mean()
female_prob = ((100 - df['percentage_male']).fillna(0) / 100).mean()
genderless_prob = df['percentage_male'].isna().mean()
male_percentage = male_prob * 100
female_percentage = female_prob * 100
genderless_percentage = genderless_prob * 100
st.write(f"**Male:** {male_percentage:.2f}%")
st.write(f"**Female:** {female_percentage:.2f}%")
st.write(f"**Genderless:** {genderless_percentage:.2f}%")
labels = ['Male', 'Female', 'Genderless']
sizes = [male_percentage, female_percentage, genderless_percentage]
colors = ['lightblue', 'lightpink', 'lightgray']
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax.set_title("Pokémon Gender Distribution")
ax.axis('equal') 
st.pyplot(fig)

# Level up (Experience)
def categorize_growth(exp):
    if pd.isna(exp):
        return "Unknown"  # Handle missing values
    elif exp <= 800000:
        return "Fast"      # Up to 800,000 XP
    elif exp <= 1059860:
        return "Medium"    # 800,001 to 1,059,860 XP
    else:
        return "Slow"      # Above 1,059,860 XP

df['growth_category'] = df['experience_growth'].apply(categorize_growth)
growth_counts = df['growth_category'].value_counts()
st.title("Pokémon Experience Growth Categories")
st.write("Distribution of Pokémon by experience needed to reach max level (Fast, Medium, Slow).")
st.subheader("Number of Pokémon by Growth Category")
st.dataframe(growth_counts.rename("Count").to_frame())
st.subheader("Bar Chart of Experience Growth Distribution")
fig, ax = plt.subplots(figsize=(8, 5))
growth_counts.plot(kind='bar', ax=ax, color=['skyblue', 'lightgreen', 'lightcoral', 'gray'])
ax.set_title("Pokémon by Experience Growth Category", fontsize=16)
ax.set_xlabel("Growth Category", fontsize=12)
ax.set_ylabel("Number of Pokémon", fontsize=12)
ax.tick_params(axis='x', rotation=0)  # No rotation needed for few categories
ax.grid(axis='y', linestyle='--', alpha=0.7)
for i, v in enumerate(growth_counts):
    ax.text(i, v + 1, str(v), ha='center', fontsize=12)
st.pyplot(fig)

# Finding Correlations
# Between ( stats, physical attributes, egg steps and stretght, legendary and non legendary capture rate)
st.subheader("Correlation Between Pokémon Stats")
st.write("This app calculates and visualizes the correlation between selected stat pairs.")
stat_pairs = [('hp', 'defense', 'HP vs. Defense'),('speed', 'attack', 'Speed vs. Attack'),('sp_attack', 'sp_defense', 'Special Attack vs. Special Defence')]
for stat1, stat2, title in stat_pairs:
    correlation = df[stat1].corr(df[stat2])
    st.subheader(f"Correlation: {title}")
    st.write(f"The Pearson correlation between {stat1.capitalize()} and {stat2.capitalize()} is **{correlation:.2f}**.")
    if correlation > 0.5:
        st.write("This indicates a moderate to strong positive correlation.")
    elif correlation < -0.5:
        st.write("This indicates a moderate to strong negative correlation.")
    elif abs(correlation) < 0.3:
        st.write("This indicates little to no linear correlation.")
    else:
        st.write("This indicates a weak correlation.")

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df[stat1], df[stat2], alpha=0.5, color='skyblue')
    ax.set_title(f"{title} (Correlation: {correlation:.2f})", fontsize=16)
    ax.set_xlabel(stat1.capitalize(), fontsize=12)
    ax.set_ylabel(stat2.capitalize(), fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    st.pyplot(fig)

# Correlation between height and wieght 
st.subheader("Correlation Between Height and Weight")
correlation = df['height_m'].corr(df['weight_kg'])
st.subheader("Correlation Coefficient")
st.write(f"The Pearson correlation between Height and Weight is **{correlation:.2f}**.")
if correlation > 0.5:
    st.write("This indicates a moderate to strong positive correlation, suggesting taller Pokémon tend to be heavier.")
elif correlation < -0.5:
    st.write("This indicates a moderate to strong negative correlation, which would be unusual here.")
elif abs(correlation) < 0.3:
    st.write("This indicates little to no linear correlation between height and weight.")
else:
    st.write("This indicates a weak correlation.")
st.subheader("Scatter Plot: Height vs. Weight")
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['height_m'], df['weight_kg'], alpha=0.5, color='skyblue')
ax.set_title(f"Height vs. Weight (Correlation: {correlation:.2f})", fontsize=16)
ax.set_xlabel("Height (meters)", fontsize=12)
ax.set_ylabel("Weight (kg)", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
st.pyplot(fig)
st.write("A positive correlation here would align with real-world expectations: larger (taller) Pokémon are likely heavier due to increased mass. Outliers might include lightweight tall Pokémon (e.g., flying types) or heavy short ones (e.g., rock types).")

# Correlation between Egg_step and base total.
st.subheader("Correlation Between Egg Steps and Base Total")
st.write("Does Pokémon requiring more egg steps to hatch tend to have higher base total stats.")
correlation = df['base_egg_steps'].corr(df['base_total'])
st.subheader("Correlation Coefficient")
st.write(f"The Pearson correlation between Egg Steps and Base Total is **{correlation:.2f}**.")
if correlation > 0.5:
    st.write("This indicates a moderate to strong positive correlation, suggesting Pokémon with more egg steps tend to have higher base totals.")
elif correlation < -0.5:
    st.write("This indicates a moderate to strong negative correlation, which would be unexpected here.")
elif abs(correlation) < 0.3:
    st.write("This indicates little to no linear correlation between egg steps and base total.")
else:
    st.write("This indicates a weak correlation.")
st.subheader("Scatter Plot: Egg Steps vs. Base Total")
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['base_egg_steps'], df['base_total'], alpha=0.5, color='lightcoral')
ax.set_title(f"Egg Steps vs. Base Total (Correlation: {correlation:.2f})", fontsize=16)
ax.set_xlabel("Base Egg Steps", fontsize=12)
ax.set_ylabel("Base Total", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
st.pyplot(fig)
st.subheader("Interpretation")
st.write("In Pokémon games, egg steps often reflect a Pokémon’s rarity or power. A positive correlation would suggest that stronger Pokémon (higher base total) take longer to hatch, aligning with species like legendaries or pseudo-legendaries (e.g., Dratini with 10,240 steps and 600 base total). A low or negative correlation might indicate design balance or exceptions like weak Pokémon with long hatch times.")

# Correlation between legendary and non legendary catch rate
st.subheader("Correlation Between Catch Rate and Legendary Status")
st.write("Does legendary Pokémon tend to have different catch rates compared to non-legendary Pokémon.")
correlation = df['is_legendary'].corr(df['capture_rate'])
st.subheader("Correlation Coefficient")
st.write(f"The Pearson correlation between Legendary Status (0 or 1) and Catch Rate is **{correlation:.2f}**.")
if correlation > 0.5:
    st.write("This indicates a moderate to strong positive correlation, which would be unexpected here (higher catch rates for legendaries?).")
elif correlation < -0.5:
    st.write("This indicates a moderate to strong negative correlation, suggesting legendaries have lower catch rates.")
elif abs(correlation) < 0.3:
    st.write("This indicates little to no linear correlation between legendary status and catch rate.")
else:
    st.write("This indicates a weak correlation.")
st.subheader("Scatter Plot: Catch Rate vs. Legendary Status")
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['is_legendary'], df['capture_rate'], alpha=0.5, color='skyblue')
ax.set_title(f"Catch Rate vs. Legendary Status (Correlation: {correlation:.2f})", fontsize=16)
ax.set_xlabel("Legendary Status (0 = Non-Legendary, 1 = Legendary)", fontsize=12)
ax.set_ylabel("Catch Rate", fontsize=12)
ax.set_xticks([0, 1])
ax.set_xticklabels(['Non-Legendary', 'Legendary'])
ax.grid(True, linestyle='--', alpha=0.7)
st.pyplot(fig)
st.write("In Pokémon games, legendaries typically have very low catch rates (e.g., 3) due to their rarity, while non-legendaries vary widely (e.g., 45 to 255). A negative correlation is expected, as being legendary (1) should correlate with lower catch rates. The box plot helps show the distribution difference more clearly.")

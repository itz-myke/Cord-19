# app.py
# CORD-19 Data Explorer
# Full project: Data Loading, Cleaning, Analysis, and Visualization with Streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import io

st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")

# ---------------------------
# PART 1: Load and Explore Data
# ---------------------------
st.title("📊 CORD-19 Data Explorer")
st.write("Exploration of the COVID-19 research metadata dataset")

@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv", low_memory=False)
    return df

df = load_data()

st.subheader("🔍 Sample of the Data")
st.write(df.head())

st.subheader("📐 Shape of the Data")
st.write(df.shape)

st.subheader("ℹ️ Data Info")
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

st.subheader("❗ Missing Values (Top 10)")
st.write(df.isnull().sum().sort_values(ascending=False).head(10))

st.subheader("📊 Basic Statistics")
st.write(df.describe())

# ---------------------------
# PART 2: Data Cleaning & Preparation
# ---------------------------
st.header("🧹 Data Cleaning & Preparation")

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year
df['year'] = df['publish_time'].dt.year

# Create abstract word count
df['abstract_word_count'] = df['abstract'].dropna().apply(lambda x: len(str(x).split()))

st.write("✅ Added 'year' and 'abstract_word_count' columns")

# Drop columns with too many missing values (example: mag_id)
df_clean = df.drop(columns=['mag_id'])

st.write("✅ Cleaned dataset shape:", df_clean.shape)

# ---------------------------
# PART 3: Data Analysis & Visualization
# ---------------------------
st.header("📈 Data Analysis & Visualization")

# Publications over time
st.subheader("Publications Over Time")
year_counts = df['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.plot(year_counts.index, year_counts.values, marker='o')
ax1.set_title("Publications by Year")
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Papers")
st.pyplot(fig1)

# Top Journals
st.subheader("Top Journals Publishing COVID-19 Research")
top_journals = df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2)
ax2.set_title("Top 10 Journals")
ax2.set_xlabel("Paper Count")
st.pyplot(fig2)

# Word Cloud of Titles
st.subheader("Word Cloud of Paper Titles")
titles = " ".join(df['title'].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.imshow(wordcloud, interpolation="bilinear")
ax3.axis("off")
st.pyplot(fig3)

# Distribution by Source
st.subheader("Distribution of Paper Counts by Source")
source_counts = df['source_x'].value_counts().head(10)
fig4, ax4 = plt.subplots()
sns.barplot(x=source_counts.values, y=source_counts.index, ax=ax4)
ax4.set_title("Top Sources")
ax4.set_xlabel("Paper Count")
st.pyplot(fig4)

# ---------------------------
# PART 4: Interactive Streamlit App Features
# ---------------------------
st.header("🎮 Interactive Exploration")

# Year filter
year_range = st.slider("Select Year Range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
st.write(f"Showing papers from {year_range[0]} to {year_range[1]}: {filtered.shape[0]} papers")

st.write(filtered[['title', 'authors', 'journal', 'year']].head(20))

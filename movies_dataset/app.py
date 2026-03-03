import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------
# Page Config
# --------------------------------
st.set_page_config(page_title="Telugu Movie Recommender 🎬", layout="wide")

st.title("🎬 Telugu Movie Recommendation System")
st.write("Content-Based Recommendation using TF-IDF & Cosine Similarity")

# --------------------------------
# Load Dataset
# --------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("Movies.csv")

    # Clean Data
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    df['Genre'] = df['Genre'].fillna('')
    df['Overview'] = df['Overview'].fillna('')

    # Clean Year Column
    if 'Year' in df.columns:
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    else:
        st.error("Year column not found in dataset!")

    df = df.dropna(subset=['Rating'])

    return df

df = load_data()

# --------------------------------
# Combine Features (Genre + Overview + Year)
# --------------------------------
df['combined_features'] = (
    df['Genre'] + " " +
    df['Overview'] + " " +
    df['Year'].astype(str)
)

# --------------------------------
# TF-IDF
# --------------------------------
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined_features'])

# --------------------------------
# Cosine Similarity
# --------------------------------
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# --------------------------------
# Extract Unique Genres
# --------------------------------
all_genres = set()

for genres in df['Genre']:
    for g in genres.split(','):
        all_genres.add(g.strip())

all_genres = sorted(list(all_genres))

# --------------------------------
# Sidebar
# --------------------------------
st.sidebar.header("Select Options")

selected_genre = st.sidebar.selectbox("Choose Genre:", all_genres)

num_movies = st.sidebar.number_input(
    "Number of Movies:",
    min_value=1,
    max_value=20,
    value=5
)

# Year Range Filter
min_year = int(df['Year'].min())
max_year = int(df['Year'].max())

selected_year_range = st.sidebar.slider(
    "Select Year Range:",
    min_year,
    max_year,
    (min_year, max_year)
)

# --------------------------------
# Filter Movies Based on Genre & Year
# --------------------------------
filtered_df = df[
    (df['Genre'].str.contains(selected_genre, case=False, na=False)) &
    (df['Year'] >= selected_year_range[0]) &
    (df['Year'] <= selected_year_range[1])
]

if filtered_df.empty:
    st.write("No movies found for this selection.")
else:
    filtered_df = filtered_df.sort_values(by='Rating', ascending=False)
    top_movies = filtered_df.head(num_movies)

    st.subheader(f"Top {num_movies} {selected_genre} Movies")

    for index, row in top_movies.iterrows():
        st.markdown(f"### 🎬 {row['Movie']}")
        st.write(f"⭐ Rating: {row['Rating']}")
        st.write(f"📅 Year: {int(row['Year']) if pd.notnull(row['Year']) else 'N/A'}")
        st.write(f"📖 Overview: {row['Overview']}")
        st.markdown("---")
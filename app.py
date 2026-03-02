import pickle
import streamlit as st
import requests
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# -------------------------
# Load Data
# -------------------------
movies = pickle.load(open('movie_list.pkl', 'rb'))
vector = pickle.load(open('vector.pkl', 'rb'))

# -------------------------
# TMDB API KEY
# -------------------------
API_KEY = "01474f8c670139b74a1950aa67990d3f&language=en-US"   # 🔥 Replace with your actual API key

# -------------------------
# Fetch Poster Function
# -------------------------
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=No+Image"

        data = response.json()
        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
        if not selected_movie:
            st.warning("Please select a movie.")
    except Exception:
        return "https://via.placeholder.com/500x750?text=Error"

# -------------------------
# Recommendation Function
# -------------------------
def recommend(movie):

    index_list = movies[movies['title'] == movie].index

    if len(index_list) == 0:
        return [], []

    index = index_list[0]

    similarity_scores = cosine_similarity(
        [vector[index]], vector
    )[0]

    movie_indices = np.argsort(similarity_scores)[-6:-1][::-1]

    recommended_names = []
    recommended_posters = []

    for i in movie_indices:
        movie_id = movies.iloc[i].movie_id
        recommended_names.append(movies.iloc[i].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_names, recommended_posters

# -------------------------
# UI
# -------------------------

st.title("🎬 Movie Recommender System")
st.markdown("Discover movies similar to your favorites 🍿")
st.markdown("---")

# -------------------------
# Trending Section
# -------------------------
st.subheader("🔥 Top Trending Movies")

trending = ["Inception", "Oppenheimer", "Avengers", "Interstellar"]
cols_trending = st.columns(4)

for i in range(4):
    with cols_trending[i]:
        st.write(trending[i])

st.markdown("---")

# -------------------------
# Genre Filter
# -------------------------
possible_genres = [
    "Action", "Adventure", "Comedy", "Drama",
    "Romance", "Thriller", "Horror",
    "Sci-Fi", "Fantasy", "Crime", "Animation"
]

selected_genre = st.selectbox(
    "🎭 Filter by Genre",
    ["All"] + possible_genres
)

if selected_genre != "All":
    filtered_movies = movies[
        movies['tags'].str.contains(selected_genre.lower(), na=False)
    ]
else:
    filtered_movies = movies

movie_list = filtered_movies['title'].values

# -------------------------
# Movie Selection
# -------------------------
selected_movie = st.selectbox(
    "🎥 Select a Movie",
    movie_list
)

# -------------------------
# Recommendation Button
# -------------------------
if st.button("Show Recommendation"):

    with st.spinner("Finding best recommendations... 🍿"):
        names, posters = recommend(selected_movie)

    if len(names) == 0:
        st.error("No recommendations found.")
    else:
        st.subheader("🎯 Recommended Movies")

        cols = st.columns(5)

        for i in range(len(names)):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])

import pickle
import streamlit as st
import requests
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------
# Load Data
# -------------------------
movies = pickle.load(open('movie_list.pkl','rb'))
vector = pickle.load(open('vector.pkl','rb'))   # changed to vector

# -------------------------
# TMDB API KEY
# -------------------------
API_KEY = "YOUR_NEW_API_KEY_HERE"   # replace with your key

st.subheader("🔥 Top Trending Movies")

trending = ["Inception", "Oppenheimer", "Avengers", "Interstellar"]

for movie in trending:
    st.write(movie)

# -------------------------
# Fetch Poster
# -------------------------
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=01474f8c670139b74a1950aa67990d3f&language=en-US"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=No+Image"

        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"

    except:
        return "https://via.placeholder.com/500x750?text=Error"


# -------------------------
# Recommend Function
# -------------------------
def recommend(movie):

    index_list = movies[movies['title'] == movie].index
    if len(index_list) == 0:
        return [], []

    index = index_list[0]

    # Dynamic cosine similarity
    similarity_scores = cosine_similarity(
        [vector[index]], vector
    )[0]

    distances = sorted(
        list(enumerate(similarity_scores)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_names = []
    recommended_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_names.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_names, recommended_posters


# -------------------------
# Streamlit UI
# -------------------------
st.title("🎬 Movie Recommender System")

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list,
    key="movie_selectbox"
)

if st.button("Show Recommendation", key="recommend_btn"):

    names, posters = recommend(selected_movie)

    if len(names) == 0:
        st.error("No recommendations found.")
    else:
        cols = st.columns(5)

        for i in range(5):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])

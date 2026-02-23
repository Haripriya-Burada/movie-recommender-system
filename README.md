# 🎬 Movie Recommender System

A Content-Based Movie Recommendation System built using Python, Machine Learning, and Streamlit.  
This application recommends top 5 similar movies based on the selected movie.

---

## 🚀 Features

- Select a movie from dropdown
- Get top 5 similar movie recommendations
- Fetches movie posters using TMDB API
- Fast similarity search using Cosine Similarity
- Clean Streamlit UI

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
- TMDB API

---

## 📂 Project Structure

movie-recommender-system/
│
├── app.py
├── movies_list.pkl
├── vector.pkl
├── requirements.txt
├── Procfile
├── setup.sh
└── .gitignore

---

## 🧠 How It Works

1. Dataset is preprocessed.
2. Important features (genres, keywords, cast, crew, overview) are combined.
3. Text data is vectorized using CountVectorizer.
4. Cosine similarity is calculated.
5. Top 5 similar movies are recommended based on similarity score.

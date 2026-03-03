# 🎬 Movie Recommender System

A Content-Based Movie Recommendation System built using Python, Machine Learning, and Streamlit.  
This application recommends top 5 similar movies based on the selected movie.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 🚀 Live Demo

https://movie-recommender-system-cedeuqbqvndfm8g2t53mnh.streamlit.app/

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Features

- Select a movie from dropdown
- Get top 5 similar movie recommendations
- Fetches movie posters using TMDB API
- Fast similarity search using Cosine Similarity
- Clean Streamlit UI

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
- TMDB API

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Project Structure

```
movie-recommender-system/
│
├── app.py
├── .gitignore
├── movie-recommender.ipynb
├── movies_list.pkl
├── requirements.txt
├── runtime.txt
├── Procfile
├── setup.sh
└── vector.pkl
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧠 How It Works

1. Dataset is preprocessed.
2. Important features (genres, keywords, cast, crew, overview) are combined.
3. Text data is vectorized using CountVectorizer.
4. Cosine similarity is calculated.
5. Top 5 similar movies are recommended based on similarity score.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## ⚙️ Installation (Run Locally)

### 1️⃣ Clone Repository

git clone https://github.com/Haripriya-Burada/movie-recommender-system
cd movie-recommender-system

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Run Application

streamlit run app.py

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🔑 TMDB API Setup

1. Create an account at https://www.themoviedb.org/
2. Generate API key
3. Replace in app.py:

api_key = "YOUR_TMDB_API_KEY"

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📦 Requirements

streamlit  
pandas  
numpy  
scikit-learn  
requests  

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🔥 Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Select app.py
4. Deploy

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 👨‍💻 Author

Developed by Hari Priya Burada

import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os

# Google Drive file links
MOVIE_DICT_URL = "https://drive.google.com/uc?id=1f5MU9CF4QfygDaJ-8pCH6xhc3BCE3u7C"
SIMILARITY_URL = "https://drive.google.com/uc?id=18BFstRRPLHeHe3X8X_FdY2ZQMIwRaqM2"

# Download function
def download_file(url, output):
    if not os.path.exists(output):  # Avoid redownloading
        gdown.download(url, output, quiet=False)

# Download necessary files
download_file(MOVIE_DICT_URL, "movie_dict.pkl")
download_file(SIMILARITY_URL, "similarity.pkl")

# Load movie data
movies = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies)
similarity = pickle.load(open("similarity.pkl", "rb"))

# API Key for movie posters
API_KEY = "b0ebcb3fd0039057c47307ebd8e2300a"

def fetch_poster(movie_id):
    """Fetch movie poster URL from TMDB API"""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    try:
        response = requests.get(url)
        data = response.json()

        if "poster_path" in data and data["poster_path"]:
            return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error"

def recommend(movie):
    """Recommend 5 similar movies based on similarity scores"""
    try:
        index = movies[movies["title"] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []

        for i in distances[1:6]:  # Get top 5 recommendations
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_names.append(movies.iloc[i[0]].title)
            recommended_movie_posters.append(fetch_poster(movie_id))

        return recommended_movie_names, recommended_movie_posters
    except IndexError:
        return [], []

# Streamlit UI
st.title("Movie Recommender System 🎬")

selected_movie_name = st.selectbox("Type or select a movie from the dropdown", movies["title"].values)

if st.button("Show Recommendation"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

    if recommended_movie_names:
        cols = st.columns(5)

        for i in range(5):
            with cols[i]:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
    else:
        st.warning("No recommendations found. Please try another movie.")

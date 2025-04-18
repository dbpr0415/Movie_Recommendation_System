import streamlit as st
import os
import pickle
import requests

# Get the current working directory
base_path = os.path.dirname(__file__)

# Construct the absolute path to your pickle files
movies_file_path = os.path.join(base_path, 'movies_list.pkl')
similarity_file_path = os.path.join(base_path, 'similarity.pkl')

# Check if the files exist
if not os.path.exists(movies_file_path):
    st.error(f"Error: {movies_file_path} does not exist.")
    st.stop()

if not os.path.exists(similarity_file_path):
    st.error(f"Error: {similarity_file_path} does not exist.")
    st.stop()

# Load the pickle files
try:
    with open(movies_file_path, 'rb') as file:
        movies_data = pickle.load(file)
        movies_list = movies_data['title'].values  # Assuming 'title' is the correct column
    with open(similarity_file_path, 'rb') as file:
        similarity = pickle.load(file)
except FileNotFoundError as e:
    st.error(f"File not found: {e.filename}")
    st.stop()
except Exception as e:
    st.error(f"Error loading pickle files: {e}")
    st.stop()

st.header("🎬 Movie Recommender System")
selectValue = st.selectbox("Select a movie:", movies_list)

def fetch_poster(movie_id):
    """Fetch movie poster from The Movie DB API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=33c924339c54a6880c6484fcabed9490"
    data = requests.get(url).json()
    if 'poster_path' in data and data['poster_path']:
        poster_path = data['poster_path']
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    else:
        return "https://via.placeholder.com/500x750?text=No+Image+Available"

def recommend(movie):
    """Recommend similar movies based on the selected movie."""
    index = movies_data[movies_data['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    recommended_posters = []

    # Get top 5 recommended movies
    for i in distances[1:6]:  # top 5 recommendations
        movie_id = movies_data.iloc[i[0]].id
        recommended_movies.append(movies_data.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

if st.button("Show Recommendation"):
    movie_names, movie_posters = recommend(selectValue)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(movie_names[idx])
            st.image(movie_posters[idx])

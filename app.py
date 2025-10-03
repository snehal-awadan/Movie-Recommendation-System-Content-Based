import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Cache poster fetching so we don’t hit the API repeatedly
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=[add your TMDB API kEY ]&language=en-US'

    # Session with retry logic
    session = requests.Session()
    retry = Retry(
        total=3,                # retry 3 times
        backoff_factor=1,       # 1s, 2s, 4s delay
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')  # safe access

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "Poster Not Found"
    except Exception as e:
        print(f" Error fetching poster for movie {movie_id}: {e}")
        return "Poster Not Found"

# Function to recommend movies:
def recommned(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)), reverse=True,
                        key=lambda x: x[1])[1:6]

    recommneded_movies = []
    recommneded_movies_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id  # movie id
        recommneded_movies.append(movies.iloc[i[0]].title)

        # fetch poster from API with retry + caching
        recommneded_movies_posters.append(fetch_poster(movie_id))

    return recommneded_movies, recommneded_movies_posters


movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    'Select a movie', movies['title'].values)

# To display the movies and posters:
if st.button('Recommend'):
    names, posters = recommned(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])        

    with col3:
        st.text(names[2])
        st.image(posters[2])        

    with col4:
        st.text(names[3])
        st.image(posters[3])        
        
    with col5:
        st.text(names[4])
        st.image(posters[4])

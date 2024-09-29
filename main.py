import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=514b4f822fe7a1246b098948facf844a'.format(movie_id))
    data =response.json()
    return 'http://image.tmdb.org/t/p/w500/' + data['poster_path']

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # Find the index of the selected movie
    distances = similarity[movie_index]  # Get similarity distances for the selected movie
    # Sort the movies based on similarity scores, ignore the first (itself), and take the top 5
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters=[]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        # fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)  # Append the title of the recommended movie
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI for the movie recommender system
st.title('Movie Recommender System')

# Dropdown menu to select a movie
selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values)

# Display recommendations when the button is clicked
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5=st.columns(5)
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




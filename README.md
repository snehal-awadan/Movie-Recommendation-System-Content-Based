🎬 Movie Recommendation System:

A simple Content-Based Movie Recommendation System built with Python, Streamlit, and TMDb API.
The app suggests movies similar to the one selected by the user and fetches their posters dynamically from TMDb.

✨ Features:

1) Recommends top 5 similar movies based on content similarity.
2) Fetches movie posters using TMDb API.
3) Interactive Streamlit web interface.
4) Includes retry logic + caching to handle API connection issues.


📦 Requirements:

1) Python 3.8+
2) streamlit
3) pandas
4) scikit-learn
5) requests

⚡ How It Works:

1) movies.pkl → contains metadata of movies.
2) similarity.pkl → precomputed cosine similarity matrix.
3) User selects a movie → find its index in the dataset.
4) Retrieve top 5 most similar movies.
5) Fetch posters using TMDb API.

🙌 Acknowledgments:

1) TMDb: For movie data and poster
2) streamlit: For an easy web app framework.
3) Tutorial inspiration & guidance: Campux Channel → https://www.youtube.com/watch?v=1xtrIEwY_zY&t=7806s 

How to run : streamlit run app.py

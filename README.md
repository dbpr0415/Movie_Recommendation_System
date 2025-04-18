Movie Recommender System
A simple movie recommendation system built using Streamlit. It suggests movies based on the movie selected by the user.

Features
Select a movie from the list.

Get 5 similar movie recommendations.

Displays movie posters fetched from The Movie Database (TMDb).

Requirements
You need the following libraries:

bash
Copy
Edit
pip install pandas streamlit requests
How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/dbpr0415/Movie_Recommendation_System.git
cd Movie_Recommendation_System
Run the app:

bash
Copy
Edit
streamlit run app.py
Open your browser and go to http://localhost:8501 to see the app.

Files
app.py: Main code to run the Streamlit app.

main.py: Loads the dataset.

dataset.csv: Movie dataset.

movies_list.pkl: Pickle file with movie data.

similarity.pkl: Pickle file with movie similarity data.

License
Open-source project under the MIT License.


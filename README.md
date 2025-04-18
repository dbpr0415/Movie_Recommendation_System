Movie Recommender System
A simple movie recommendation system built using Streamlit that suggests movies based on the one selected by the user.

Features
Select a movie from a dropdown list.

Get 5 similar movie recommendations.

Display movie posters fetched from The Movie Database (TMDb).

Requirements
Make sure to install the following libraries:

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
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open your browser and go to http://localhost:8501 to view the app.

Files
app.py: Main file that runs the Streamlit app.

main.py: Script to load the dataset and display it.

dataset.csv: Movie dataset (CSV file).

movies_list.pkl: Pickle file containing movie data.

similarity.pkl: Pickle file containing movie similarity data.

License
This is an open-source project under the MIT License.

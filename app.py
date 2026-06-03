from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load saved files
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movies_list]

# Home route
@app.route("/")
def home():
    return "🎬 Movie Recommendation System is Running"

# API route
@app.route("/recommend")
def recommend_api():
    movie = request.args.get("movie")
    return jsonify(recommend(movie))

# Run app (IMPORTANT for Render)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

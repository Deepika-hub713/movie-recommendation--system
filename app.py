from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load files
movies = pickle.load(open("movies.pkl", "rb"))
recommendations = pickle.load(open("recommendations.pkl", "rb"))

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    return recommendations[index]

# Home route
@app.route("/")
def home():
    return "🎬 Movie Recommendation System is Running"

# API route
@app.route("/recommend")
def recommend_api():
    movie = request.args.get("movie")

    if movie is None:
        return jsonify({"error": "Please provide a movie name"}), 400

    try:
        result = recommend(movie)
        return jsonify(result)
    except:
        return jsonify({"error": "Movie not found"}), 404

# Run app (IMPORTANT for Render)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

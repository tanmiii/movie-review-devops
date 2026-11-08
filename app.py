from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

# In-memory database
movies = [
    {"id": "1", "title": "Inception", "genre": "Sci-Fi", "rating": 9},
    {"id": "2", "title": "The Dark Knight", "genre": "Action", "rating": 10}
]

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        title = request.form.get("title")
        genre = request.form.get("genre")
        rating = request.form.get("rating")
        if title and genre and rating:
            movies.append({"id": str(uuid.uuid4()), "title": title, "genre": genre, "rating": int(rating)})
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/rankings")
def rankings():
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return render_template("rankings.html", movies=sorted_movies)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

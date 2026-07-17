from flask import Flask, render_template, request
from recommend_book import recommend

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    if request.method == "POST":
        book_name = request.form.get("book_name")

        try:
            recommendations = recommend(book_name)
            error = None
        except IndexError:
            recommendations = []
            error = "Sorry, that book wasn't found in our database."

    return render_template(
        "index.html",
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)
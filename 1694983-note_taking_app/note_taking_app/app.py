from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for notes (resets whenever the server restarts)
notes: list[str] = []


@app.route('/', methods=["GET", "POST"])
def index():
    """Home page: add a note and display all notes."""

    if request.method == "POST":
        # Form uses POST body -> request.form, not request.args
        note = (request.form.get("note") or "").strip()

        # Avoid adding empty notes
        if note:
            notes.append(note)

        # Post/Redirect/Get to prevent duplicates on refresh
        return redirect(url_for("index"))

    # GET request -> render the page
    return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)

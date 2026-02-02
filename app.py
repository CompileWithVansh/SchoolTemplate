from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/classes")
def classes():
    return render_template("classes.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/appointment")
def appointment():
    return render_template("appointment.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/call-to-action")
def call_to_action():
    return render_template("call-to-action.html")


if __name__ == "__main__":
    app.run(debug=True)

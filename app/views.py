from app import app

@app.route("/")
def hello():
    return "Halo, Bandung!"

from microflask import app

@app.route("/")
def hello():
    return "Halo, Bandung!"


if __name__ == '__main__':
    app.run()

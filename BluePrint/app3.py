import app

@app.app("/home")
def home():
    return "<h1>Home 3<h3>"

app.app.run()
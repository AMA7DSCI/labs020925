from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello working, World today again will this work or not but I made it work!</p>"


if __name__ == '__main__':
    app.run()

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask from Docker!"

if __name__ == "__main__":
    # host="0.0.0.0" important hai taki container ke bahar se access ho sake
    app.run(host="0.0.0.0", port=5000)

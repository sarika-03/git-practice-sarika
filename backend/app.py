from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS allow for frontend to call backend

@app.route('/')
def hello():
    return "Hello from Backend!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



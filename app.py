# app/app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Secure Cloud!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

# app/requirements.txt
Flask==2.3.3

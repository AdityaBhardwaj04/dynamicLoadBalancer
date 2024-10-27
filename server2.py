from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/")
def home():
    time.sleep(random.uniform(0.2, 0.6))
    return "Server 2 response"

if __name__ == "__main__":
    app.run(port=5002)
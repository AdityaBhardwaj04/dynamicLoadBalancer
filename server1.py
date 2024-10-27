from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/")
def home():
    # Simulate different response times
    time.sleep(random.uniform(0.1, 0.5))
    return "Server 1 response"

if __name__ == "__main__":
    app.run(port=5001)
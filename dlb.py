import requests
import time
from flask import Flask, redirect
from threading import Lock

app = Flask(__name__)

# List of server endpoints
servers = ["http://127.0.0.1:5001", "http://127.0.0.1:5002"]
server_response_times = {server: float('inf') for server in servers}
lock = Lock()  # Ensures thread-safe operations
request_count = 0  # To track how many requests have been made


def get_response_time(server):
    """Measure response time for a given server."""
    start = time.time()
    try:
        requests.get(server, timeout=2)
        return time.time() - start
    except requests.exceptions.RequestException:
        return float('inf')


def update_response_times():
    """Update the response times for each server."""
    global server_response_times
    with lock:
        for server in servers:
            response_time = get_response_time(server)
            server_response_times[server] = response_time
        print("Updated response times:", server_response_times)


def least_response_time_server():
    """Find the server with the least response time."""
    with lock:
        return min(server_response_times, key=server_response_times.get)


@app.route("/")
def load_balance():
    """Route incoming requests to the server with the least response time."""
    global request_count
    request_count += 1

    # Update response times every 4th request
    if request_count % 1 == 0:
        update_response_times()

    # Find the best server based on response time
    best_server = least_response_time_server()

    # Redirect to the selected server
    print(f"Redirecting to {best_server}")
    return redirect(best_server, code=302)


if __name__ == "__main__":
    # Initial update of response times
    update_response_times()

    # Run the load balancer on port 5000
    app.run(port=5000)

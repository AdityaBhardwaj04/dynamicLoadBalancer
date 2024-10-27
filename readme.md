# Least Response Time Load Balancer

A simple HTTP load balancer using Flask to distribute requests across multiple backend servers based on the least response time. The load balancer listens on port `5000` and redirects requests to the backend server with the fastest response time.


## Prerequisite

* Python 3.x
* pip (Python Package Installer)

## Installation

1. Clone the repository
   ```
   git clone https://github.com/AdityaBhardwaj04/dynamicLoadBalancer.git
   cd dynamicLoadBalancer
   ```
2. Install dependencies
   * ```
     pip install -r requirements.txt
     ```

## Running the project

1. Start Backend servers

   Open separate terminal windows for each server.

   * Server 1 : In the root folder, run:
     * `python server1.py`
   * Server 2 : In the root folder, run:
     * `python server2.py`
2. Start load balancer

   * In a new terminal window, run the load balancer:
     * `python load_balancer.py`
   * The load balancer will start on `http://127.0.0.1:5000`.
3. Access the Load Balancer

   * Open a web browser and go to `http://127.0.0.1:5000`.
   * The load balancer will check response times for each backend server and redirect you to the one with the least response time (either `http://127.0.0.1:5001` or `http://127.0.0.1:5002`).

## How it works

1. Load Balancing Logic
   * The load balancer checks the response times of all backend servers every 4th request.
   * It stores the response times and selects the server with the shortest response time for each request.
2. Redirection
   * When a request is made to `http://127.0.0.1:5000`, the load balancer redirects the user to the backend server with the fastest response time.

## Project Customization

* **Adding More Servers** : You can add more backend servers by adding additional server files and updating the `servers` list in `load_balancer.py`.
* **Adjusting Update Frequency** : The frequency of response time updates (currently every 4 requests) can be modified in `load_balancer.py` by changing `if request_count % 4 == 0`.

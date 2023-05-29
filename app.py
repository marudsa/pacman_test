from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)
counter = Counter('pacman_moves_total', 'Total number of Pac-Man moves')

@app.route('/')
def home():
    counter.inc()
    return "Welcome to Pac-Man!"

if __name__ == '__main__':
    start_http_server(8000)
    app.run(debug=True, host='0.0.0.0')

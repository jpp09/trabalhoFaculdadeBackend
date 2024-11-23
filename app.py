from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/home')
def home():

    url = "https://api.themoviedb.org/3/trending/all/day?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODZmNmQ2YzZkNTVhODJiNmY5MmU4NWE0ODc0MTljYyIsIm5iZiI6MTczMjM2MDAzMC45ODI5NjcsInN1YiI6IjY3MmU5M2U4N2ZkNzI0MzQyYTkwMDNhNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.qIYC-ShZPXNXYcJLc6dQZ_ohzXkscej-3yQterP3GZ0"
    }

    response = requests.get(url, headers=headers)

    return jsonify(response.json())

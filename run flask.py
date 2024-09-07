import random
import time
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Simulate telescope data (could be connected to real sensors in the future)
def get_telescope_data():
    return {
        "temperature": round(random.uniform(15, 30), 2),  # Simulated temperature in Celsius
        "alignment": random.choice(["Aligned", "Misaligned"]),  # Simulated alignment status
        "status": random.choice(["Operational", "Error"])  # Simulated telescope status
    }

# Route to serve telescope data as JSON
@app.route('/api/telescope_data')
def telescope_data():
    data = get_telescope_data()
    return jsonify(data)

# Route to serve the dashboard
@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

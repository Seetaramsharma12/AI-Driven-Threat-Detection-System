from flask import Flask, render_template, jsonify
from flask_cors import CORS
from threat_engine import ThreatEngine
import time

app = Flask(__name__)
CORS(app)

engine = ThreatEngine()

# In-memory storage for simple demo
threat_log = []

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/stats')
def stats():
    return jsonify(engine.get_system_stats())

@app.route('/api/threats')
def threats():
    new_threat = engine.generate_threat()
    if new_threat:
        threat_log.insert(0, new_threat)
        # Keep only last 50 threats
        if len(threat_log) > 50:
            threat_log.pop()
    
    return jsonify({
        'latest_threat': new_threat,
        'log': threat_log[:10] # Return top 10
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

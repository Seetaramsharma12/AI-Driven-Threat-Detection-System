import random
import time
from datetime import datetime

class ThreatEngine:
    def __init__(self):
        self.threat_types = [
            'DDoS Attack', 'SQL Injection', 'Malware Detected', 
            'Phishing Attempt', 'Brute Force', 'Anomalous Traffic'
        ]
        self.severities = ['Low', 'Medium', 'High', 'Critical']
        self.sources = ['192.168.1.10', '10.0.0.5', 'External IP: 45.33.22.11', 'Gateway', 'Firewall']

    def generate_threat(self):
        """Simulates an AI detection event."""
        is_threat = random.random() < 0.3  # 30% chance of a threat being detected in a poll
        
        if is_threat:
            return {
                'id': int(time.time() * 1000),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'type': random.choice(self.threat_types),
                'severity': random.choice(self.severities),
                'source': random.choice(self.sources),
                'confidence': round(random.uniform(0.75, 0.99), 2),
                'status': 'Active'
            }
        return None

    def get_system_stats(self):
        """Returns dummy system stats mimicking AI monitoring."""
        return {
            'cpu_usage': random.randint(10, 90),
            'memory_usage': random.randint(20, 80),
            'network_traffic': random.randint(100, 10000), # KB/s
            'active_threats': random.randint(0, 5)
        }

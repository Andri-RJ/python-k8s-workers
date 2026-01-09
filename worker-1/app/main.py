#!/usr/bin/env python3
from flask import Flask, render_template_string
import os
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Worker 1 - andrirj</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .container {
            text-align: center;
            padding: 3rem;
            background: rgba(255,255,255,0.1);
            border-radius: 20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            max-width: 600px;
        }
        h1 { font-size: 3rem; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        .subtitle { font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.9; }
        .info-box {
            background: rgba(255,255,255,0.2);
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
        .info-box p { margin: 0.5rem 0; font-size: 1.1rem; }
        .badge {
            display: inline-block;
            background: #4CAF50;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-weight: bold;
            margin-top: 1rem;
        }
        .api-link {
            margin-top: 2rem;
            padding: 1rem;
            background: rgba(255,255,255,0.15);
            border-radius: 10px;
        }
        .api-link a {
            color: #fff;
            text-decoration: none;
            font-weight: bold;
            border-bottom: 2px solid #fff;
        }
        .api-link a:hover { opacity: 0.8; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Worker 1</h1>
        <p class="subtitle">Site Vitrine - CI/CD avec Kubernetes</p>
        
        <div class="info-box">
            <p><strong>Version:</strong> {{ version }}</p>
            <p><strong>Pod:</strong> {{ hostname }}</p>
            <p><strong>Timestamp:</strong> {{ timestamp }}</p>
            <p><strong>Déployé par:</strong> andrirj</p>
        </div>
        
        <div class="badge">✅ Déployé via GitHub Actions</div>
        
        <div class="api-link">
            <p>API : <a href="/api/status">/api/status</a></p>
            <p>Health : <a href="/api/health">/api/health</a></p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        version=os.getenv('VERSION', '1.0.0'),
        hostname=os.getenv('HOSTNAME', 'unknown'),
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

@app.route('/api/status')
def status():
    return {
        'status': 'healthy',
        'worker': 'worker-1',
        'version': os.getenv('VERSION', '1.0.0'),
        'timestamp': datetime.now().isoformat(),
        'deployed_by': 'andrirj'
    }

@app.route('/api/health')
def health():
    return {'status': 'ok', 'worker': 'worker-1'}

if __name__ == '__main__':
    logger.info("Worker 1 starting on port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=False)

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps CI/CD Pipeline</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
                color: #333;
            }
            .container {
                background: rgba(255, 255, 255, 0.95);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 600px;
            }
            h1 {
                color: #2c3e50;
                margin-bottom: 20px;
                font-size: 2.5em;
            }
            .badge {
                display: inline-block;
                background: #4CAF50;
                color: white;
                padding: 10px 20px;
                border-radius: 25px;
                margin: 10px;
                font-weight: bold;
            }
            .info {
                background: #f8f9fa;
                border-left: 4px solid #3498db;
                padding: 15px;
                margin: 20px 0;
                text-align: left;
                border-radius: 0 8px 8px 0;
            }
            .url {
                color: #2980b9;
                font-weight: bold;
                word-break: break-all;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 DevOps CI/CD Automatizado</h1>
            
            <div class="badge">GitHub Actions ✅</div>
            <div class="badge">Docker Hub ✅</div>
            <div class="badge">Render.com ✅</div>
            
            <div class="info">
                <strong>Estado:</strong> <span style="color:#27ae60;">● EN PRODUCCIÓN</span><br>
                <strong>Desplegado automáticamente desde:</strong> GitHub<br>
                <strong>Imagen Docker:</strong> brayant002/devops-cicd-app:latest
            </div>
            
            <p>Esta aplicación fue desplegada automáticamente por GitHub Actions.</p>
            
            <div class="info">
                <strong>Endpoints:</strong><br>
                • <a href="/health" class="url">/health</a> - Health check<br>
                • <a href="/" class="url">/</a> - Página principal
            </div>
            
            <p><small>Pipeline CI/CD completo • Brayan Payan</small></p>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'devops-cicd-app',
        'version': '1.0.0',
        'environment': 'production',
        'deployed_with': 'github-actions'
    })

@app.route('/info')
def info():
    return jsonify({
        'docker_image': 'brayant002/devops-cicd-app:latest',
        'deployment': 'render.com',
        'ci_cd': 'github-actions'
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
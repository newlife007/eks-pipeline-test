from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f'''
    <h1>Hello from EKS!</h1>
    <p>Version: {os.environ.get('APP_VERSION', '1.0')}</p>
    <p>Environment: {os.environ.get('ENVIRONMENT', 'development')}</p>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


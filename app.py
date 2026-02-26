from flask import Flask

app = Flask(__name__)

@app.route('/app1')
def hello():
    return 'Hello from EKS and Jenkins, by Swanand S. Joshi! 🚀'

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

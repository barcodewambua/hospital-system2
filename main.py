from flask import Flask, render_template
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/health-assistant')
def health_assistant():
    return render_template('health_assistant.html')

@app.route('/health-guide')
def health_guide():
    return render_template('health_guide.html')

@app.route('/family-health')
def family_health():
    return render_template('family_health.html')

@app.route('/mental-health')
def mental_health():
    return render_template('mental_health.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
import os
import logging
from flask import Flask, render_template

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "mysecret")

# Route definitions
@app.route('/')
def index():
    """Render the homepage."""
    logger.debug("Rendering index page")
    return render_template('index.html')

@app.route('/services')
def services():
    """Render the services page."""
    logger.debug("Rendering services page")
    return render_template('services.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    logger.debug("Rendering contact page")
    return render_template('contact.html')

@app.route('/health-assistant')
def health_assistant():
    """Render the health assistant page with chatbot."""
    logger.debug("Rendering health assistant page")
    return render_template('health_assistant.html')

@app.route('/health-guide')
def health_guide():
    """Render the health guide page."""
    logger.debug("Rendering health guide page")
    return render_template('health_guide.html')

@app.route('/family-health')
def family_health():
    """Render the family health page."""
    logger.debug("Rendering family health page")
    return render_template('family_health.html')

@app.route('/mental-health')
def mental_health():
    """Render the mental health page."""
    logger.debug("Rendering mental health page")
    return render_template('mental_health.html')

if __name__ == '__main__':
    # Use Waitress on Windows, Gunicorn on Linux
    if os.name == 'nt':  # Windows
        from waitress import serve
        serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:  # Linux (like Vercel or Cloud servers)
        app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)

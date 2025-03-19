# HealthCare Connect Website

A professional medical services website built with Flask, featuring a clean and modern interface designed to showcase healthcare services and facilitate patient engagement.

## Project Overview

HealthCare Connect is a comprehensive medical services website that provides information about various medical services, laboratory tests, and consultation options. The website features a responsive design with a professional medical theme and clear service categorization.

## Features

- Professional medical interface with blue color scheme
- Responsive design for all devices
- Service showcase with detailed descriptions
- Interactive health assistant chatbot
- Mental health counseling services
- Family planning and HIV/AIDS information
- Contact form for appointments and inquiries
- Modern navigation system
- Comprehensive service categorization
- Integration with medical imagery and icons

## Technologies Used

- Flask (Python web framework)
- HTML5 & CSS3
- Bootstrap 5
- JavaScript (Vanilla)
- Bootstrap Icons
- Professional medical imagery

## Project Structure
```
healthcare-connect/
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── services.html
│   ├── contact.html
│   ├── health_assistant.html
│   ├── health_guide.html
│   ├── family_health.html
│   └── mental_health.html
├── main.py
└── README.md
```

## Setup and Installation

1. Ensure Python 3.11 or higher is installed
2. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy gunicorn email-validator
   ```

3. Run the application:
   ```bash
   python main.py
   ```

The application will be available at `http://localhost:5000`

## Features Overview

### Health Assistant
- AI-powered health guidance
- Pre-defined responses for common health queries
- Clear medical disclaimers

### Mental Health Support
- Professional counseling information
- Interactive mental health chatbot
- Comprehensive resources

### Health Information
- Detailed guides on common conditions
- Family planning services
- HIV/AIDS information and support

## Contributing

Contributions are welcome! Please read our contributing guidelines before submitting pull requests.

## License

© 2025 HealthCare Connect. All rights reserved.
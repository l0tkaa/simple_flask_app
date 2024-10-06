# Simple Flask App Tutorial

This is a basic Flask web application that demonstrates setting up routes, rendering HTML templates, and handling form submissions.

## Features
- Simple "Hello, World!" route
- HTML templates using Jinja2
- Basic form handling with POST requests

## Prerequisites
- Python 3.x
- Flask (install via `pip install Flask`)

## Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/l0tkaa/simple_flask_app.git
    cd simple_flask_app
    ```

2. **Create a Virtual Environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the App:**

    ```bash
    python app.py
    ```

    You can now access the app at `http://localhost:5000/`.

## Project Structure

```plaintext
basic-flask-app/
│
├── app.py                  # Main Flask app file
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── LICENSE                  # License file
└── templates/               # HTML templates
    ├── index.html           # Home page template
    └── form.html            # Form page template

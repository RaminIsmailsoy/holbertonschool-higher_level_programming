#!/usr/bin/python3
''' Creating a Basic HTML Template in Flask '''


from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# --- Routes ---

@app.route('/')
def home():
    """Renders the index.html template."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about.html template."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Renders the contact.html template."""
    return render_template('contact.html')

# --- Server Execution ---

if __name__ == '__main__':
    # Run the application on port 5000 with debug mode enabled
    app.run(debug=True, port=5000)

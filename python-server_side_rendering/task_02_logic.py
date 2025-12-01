#!/usr/bin/python3
''' Creating a Dynamic Template with Loops and Conditions in Flask '''

from flask import Flask, render_template
import json
import os

# Initialize the Flask application
app = Flask(__name__)

# Helper function to load data from items.json
def load_items_from_json(filename='items.json'):
    """
    Reads the list of items from the specified JSON file.
    Includes robust error handling for file not found or invalid JSON format.
    """
    # Determine the correct file path relative to the script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            # Safely get the "items" list, defaulting to an empty list if key is missing
            return data.get("items", [])
    except FileNotFoundError:
        print(f"Error: {filename} not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filename}. Check file format.")
        return []

@app.route('/items')
def items():
    """
    Loads data from items.json and renders items.html with the list.
    """
    item_list = load_items_from_json()

    # Pass the list to the template using the variable name 'items'
    return render_template('items.html', items=item_list)

# --- Server Execution ---

if __name__ == '__main__':
    # Run the application on port 5000 with debug mode enabled
    app.run(debug=True, port=5000)

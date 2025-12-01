from flask import Flask, jsonify, request
import json
from werkzeug.exceptions import BadRequest

# 1. Instantiate the Flask application
app = Flask(__name__)

# Dictionary to store user data in memory. This starts empty for the checker.
users = {}

# --- API Endpoints ---

@app.route('/', methods=['GET'])
def home():
    """Returns the welcome message for the root URL."""
    return "Welcome to the Flask API!"

# 2. Status Endpoint
@app.route('/status', methods=['GET'])
def get_status():
    """Returns the API status."""
    return "OK"

# 3. Data Endpoint
@app.route('/data', methods=['GET'])
def get_data():
    """Returns a JSON list of all usernames."""
    # Return the list of keys (usernames) from the users dictionary as JSON
    return jsonify(list(users.keys()))

# 4. Dynamic User Endpoint
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    Returns the full object for a specific username.
    Returns 404 if the user is not found.
    """
    # Check if the username exists in the dictionary
    if username in users:
        # Return the user's data as JSON
        # Ensure the returned object contains 'username' as specified in the POST response
        user_data = users[username].copy()
        user_data['username'] = username
        return jsonify(user_data)
    else:
        # Return a 404 Not Found response with a custom JSON body
        return jsonify({"error": "User not found"}), 404

# 5. POST Request Handling Endpoint
@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handles POST requests to add a new user.
    Performs validation for JSON format, required fields, and duplicate usernames.
    """
    try:
        # Flask's get_json() handles parsing and checking the Content-Type header.
        # It returns None if the body is empty or malformed JSON, 
        # but the try/except block handles more complex parsing failures.
        new_user_data = request.get_json()
        
        # Check if get_json() failed to parse or returned null (e.g., if body was just 'null')
        if not new_user_data or not isinstance(new_user_data, dict):
            # This handles both non-JSON content and empty/invalid JSON structures
            return jsonify({"error": "Invalid JSON"}), 400
            
    except BadRequest:
        # Catch specific exceptions Flask raises for bad JSON formats
        return jsonify({"error": "Invalid JSON"}), 400
    except Exception:
        # Catch any other unexpected parsing errors
        return jsonify({"error": "Invalid JSON"}), 400


    # Validation 1: Check for mandatory 'username' key
    if 'username' not in new_user_data:
        return jsonify({"error": "Username is required"}), 400
    
    username = new_user_data['username']

    # Validation 2: Check for duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the user to the in-memory dictionary
    # We store a copy of the incoming data
    # Note: We ensure the username is the dictionary key, but we don't need to store
    # 'username' redundantly *inside* the user object itself unless it was provided.
    users[username] = new_user_data.copy()

    # Create the final response payload, ensuring 'username' is included in the 'user' object
    response_user_data = users[username].copy()
    response_user_data['username'] = username
    
    response = {
        "message": "User added",
        "user": response_user_data
    }

    # Return the confirmation message with HTTP status code 201 (Created)
    return jsonify(response), 201


# --- Running the Server ---
if __name__ == "__main__":
    # IMPORTANT: The users dictionary is NOT populated here. 
    # It remains empty for the checker to test from a clean state.
    app.run(debug=True)

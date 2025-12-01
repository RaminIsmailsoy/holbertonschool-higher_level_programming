from flask import Flask, jsonify, request, abort

# 1. Instantiate the Flask application
app = Flask(__name__)

# Dictionary to store user data in memory
# The key is the username, and the value is the user object (dictionary)
users = {}

# --- Helper function for response consistency ---
def _create_user_response(user_data):
    """
    Ensures the user object always includes the 'username' key for consistent API output.
    This is useful for the POST response structure.
    """
    if 'username' not in user_data:
        # If the data came without a 'username' key but was added using the dictionary key,
        # we'll ensure it's present in the object returned to the user.
        user_data['username'] = next((k for k, v in users.items() if v == user_data), None)
    return user_data

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
        return jsonify(_create_user_response(users[username]))
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
    # Get JSON data from the request body
    try:
        new_user_data = request.get_json()
    except Exception:
        # Handle case where request body is not valid JSON
        return jsonify({"error": "Invalid JSON"}), 400

    if not new_user_data:
        # Handle case where request body is empty or null JSON
        return jsonify({"error": "Invalid JSON"}), 400

    # Validation 1: Check for mandatory 'username' key
    if 'username' not in new_user_data:
        return jsonify({"error": "Username is required"}), 400
    
    username = new_user_data['username']

    # Validation 2: Check for duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the user to the in-memory dictionary
    # The dictionary key is the username, and the value is the user object
    users[username] = new_user_data

    # Create the final response payload, ensuring 'username' is included in the 'user' object
    response = {
        "message": "User added",
        "user": _create_user_response(new_user_data)
    }

    # Return the confirmation message with HTTP status code 201 (Created)
    return jsonify(response), 201


# --- Running the Server ---
if __name__ == "__main__":
    # NOTE: Add a sample user for local testing, but remember to remove/comment
    # this out before pushing the code as instructed.
    users['jane'] = {"name": "Jane", "age": 28, "city": "Los Angeles"}
    users['john'] = {"name": "John", "age": 30, "city": "New York"}
    
    # Run the application (default port is 5000)
    app.run(debug=True)

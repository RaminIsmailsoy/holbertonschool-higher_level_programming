from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity, get_jwt

# --- Configuration ---
app = Flask(__name__)
# Set a strong secret key for JWT (required for production)
app.config["JWT_SECRET_KEY"] = "super-secret-key-do-not-share-in-production"  
jwt = JWTManager(app)
basic_auth = HTTPBasicAuth()

# --- User Data Store ---
# NOTE: Passwords are hashed before being stored.
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# --- JWT Error Handlers (Ensuring 401 response for all auth failures) ---

@jwt.unauthorized_loader
@jwt.invalid_token_loader
@jwt.expired_token_loader
@jwt.revoked_token_loader
@jwt.needs_fresh_token_loader
def handle_auth_errors(err):
    """
    Handles all JWT authentication errors by returning a 401 Unauthorized response.
    """
    return jsonify({"error": "Unauthorized"}), 401

# --- Basic Authentication Implementation ---

@basic_auth.verify_password
def verify_password(username, password):
    """
    Callback function used by Flask-HTTPAuth to verify credentials.
    """
    if username in users and check_password_hash(users[username]["password"], password):
        # Return the user object (or just username) to be stored in the current_user
        return users[username]
    return None

# --- Basic Auth Protected Route ---

@app.route('/basic-protected', methods=['GET'])
@basic_auth.login_required
def basic_protected():
    """Route protected by Basic HTTP Authentication."""
    # current_user is set by the verify_password function
    return "Basic Auth: Access Granted"

# --- JWT Authentication Implementation ---

@app.route('/login', methods=['POST'])
def login():
    """
    Accepts credentials and returns a JWT access token upon successful authentication.
    """
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        # Check for missing data
        return jsonify({"error": "Missing username or password"}), 400

    username = data.get('username')
    password = data.get('password')

    user_info = users.get(username)

    if user_info and check_password_hash(user_info["password"], password):
        # Create token, embedding the user's role and username into the payload 
        # using the 'additional_claims' argument.
        access_token = create_access_token(identity=username, 
                                           additional_claims={"role": user_info["role"]})
        return jsonify(access_token=access_token), 200
    else:
        # Return 401 for bad credentials (as per standard security practice)
        return jsonify({"error": "Invalid username or password"}), 401

# --- JWT Protected Route ---

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    # get_jwt_identity() retrieves the identity set during token creation (the username)
    # current_user = get_jwt_identity() 
    return "JWT Auth: Access Granted"

# --- Role-based Access Control (RBAC) Protected Route ---

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Route that requires a valid JWT and an 'admin' role.
    """
    # 1. Retrieve the entire JWT payload (claims)
    claims = get_jwt()
    
    # 2. Check the 'role' claim
    if claims.get("role") == "admin":
        return "Admin Access: Granted"
    else:
        # Return 403 Forbidden if the user is not an admin
        return jsonify({"error": "Admin access required"}), 403

# --- Running the Server ---
if __name__ == '__main__':
    # Running in debug mode for development

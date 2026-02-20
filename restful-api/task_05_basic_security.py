#!/usr/bin/python3
"""
API Security and Authentication Techniques
Implements:
- Basic Authentication using Flask-HTTPAuth
- JWT Authentication using Flask-JWT-Extended
- Role-based access control
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# JWT Configuration
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# User database
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# ---------------------------------------------------------------------
# BASIC AUTHENTICATION
# ---------------------------------------------------------------------
@auth.verify_password
def verify_password(username, password):
    """Verify basic auth credentials."""
    if username in users:
        user = users[username]
        if check_password_hash(user["password"], password):
            return username
    return None


@auth.error_handler
def auth_error(status):
    """Handle basic auth errors."""
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication."""
    return "Basic Auth: Access Granted"


# ---------------------------------------------------------------------
# JWT AUTHENTICATION
# ---------------------------------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return a JWT token."""
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Missing username or password"}), 401
    
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 401
    
    user = users.get(username)
    
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Create access token with role in claims
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )
    
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protected route using JWT token."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Route accessible only to admin users."""
    claims = get_jwt()
    role = claims.get("role")
    
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"


# ---------------------------------------------------------------------
# JWT ERROR HANDLERS
# ---------------------------------------------------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle unauthorized error (missing token)."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token error."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token error."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token error."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle needs fresh token error."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
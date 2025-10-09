#!/usr/bin/python3
"""
Flask API module for user management.
This module provides a simple REST API with endpoints to manage users,
check status, and retrieve user data.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint - returns a welcome message.

    Returns:
        str: Welcome message for the API
    """
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """
    Status endpoint - returns OK.

    Returns:
        str: Status message indicating the API is running
    """
    return "OK"


@app.route("/data", methods=["GET"])
def get_usernames():
    """
    Returns a list of all usernames stored in the API.

    Returns:
        json: List of all usernames
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Returns full user data for a given username.

    Args:
        username (str): The username to retrieve

    Returns:
        json: User data if found, error message otherwise
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user via POST request.

    Expects JSON data with at least a 'username' field.

    Returns:
        json: Confirmation message with user data and 201 status code,
              or error message with 400 status code if username is missing
    """
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
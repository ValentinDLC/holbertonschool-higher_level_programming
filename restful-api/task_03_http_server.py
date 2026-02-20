#!/usr/bin/python3
"""
Simple HTTP API server module.
This module provides a basic HTTP server with multiple endpoints
for testing and demonstration purposes.
"""
import http.server
import json
from http import HTTPStatus


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP request handler for the simple API server.

    Handles GET requests for multiple endpoints:
    - /: Returns a welcome message
    - /data: Returns sample JSON data
    - /status: Returns API status
    - /info: Returns API information
    """

    def do_GET(self):
        """
        Handle GET requests to different endpoints.

        Routes requests to appropriate handlers based on the path
        and returns JSON or plain text responses.
        """
        if self.path == "/":
            # Root endpoint - welcome message
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            # Data endpoint - sample user data
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            # Status endpoint - API health check
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            # Info endpoint - API version and description
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            # 404 - Endpoint not found
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    PORT = 8000
    server_address = ("", PORT)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running on http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    httpd.serve_forever()
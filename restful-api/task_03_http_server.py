import http.server
import socketserver
import json

# Define the port the server will listen on
PORT = 8000

# Sample JSON data to be served on the /data endpoint
SAMPLE_DATA = {"name": "John", "age": 30, "city": "New York"}

# Additional data for the /info endpoint (as mentioned in the expected output)
INFO_DATA = {"version": "1.0", "description": "A simple API built with http.server"}

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    A custom request handler for our simple API.
    It overrides the do_GET method to handle GET requests.
    """

    def _set_headers(self, status_code=200, content_type='text/html'):
        """Sets the common response headers."""
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        """
        Handles GET requests and routes them based on the request path (self.path).
        """
        # 1. Root path: http://localhost:8000/
        if self.path == '/':
            message = "Hello, this is a simple API!"
            self._set_headers(content_type='text/plain')
            self.wfile.write(message.encode('utf-8'))
        
        # 2. Data path: http://localhost:8000/data
        elif self.path == '/data':
            # Convert Python dictionary to a JSON string
            response_data = json.dumps(SAMPLE_DATA)
            
            # Set headers for JSON response
            self._set_headers(content_type='application/json')
            
            # Write the JSON string as bytes to the response body
            self.wfile.write(response_data.encode('utf-8'))

        # 3. Status path: http://localhost:8000/status
        elif self.path == '/status':
            message = "OK"
            self._set_headers(content_type='text/plain')
            self.wfile.write(message.encode('utf-8'))

        # 4. Info path: http://localhost:8000/info
        # Added to match the expected output requirements
        elif self.path == '/info':
            response_data = json.dumps(INFO_DATA)
            self._set_headers(content_type='application/json')
            self.wfile.write(response_data.encode('utf-8'))

        # 5. Error handling: Undefined endpoints
        else:
            message = "Endpoint not found"
            # Set a 404 Not Found status code
            self._set_headers(status_code=404, content_type='text/plain')
            self.wfile.write(message.encode('utf-8'))

# --- Server Setup ---

def run_server():
    """
    Sets up and starts the HTTP server.
    """
    # socketserver.TCPServer handles socket creation and binds to address/port
    # SimpleAPIHandler is passed to handle all incoming requests
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"✅ Serving on port {PORT}")
        print(f"Try: http://localhost:{PORT}")
        print(f"Try: http://localhost:{PORT}/data")
        print(f"Try: http://localhost:{PORT}/status")
        print(f"Try: http://localhost:{PORT}/info")
        print(f"Try: http://localhost:{PORT}/nonexistent")
        
        try:
            # Start the server and keep it running indefinitely
            httpd.serve_forever()
        except KeyboardInterrupt:
            # Handle graceful shutdown on Ctrl+C
            print("\n🛑 Server stopped by user.")
            httpd.shutdown()

if __name__ == "__main__":
    # Ensure the script runs the server when executed directly
    run_server()

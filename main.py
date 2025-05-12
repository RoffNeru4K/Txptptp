import http.server
import socketserver
import webbrowser
import os

PORT = 5000
DIRECTORY = os.path.abspath(".")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Buka browser secara otomatis
webbrowser.open(f'http://localhost:{PORT}/index.html')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
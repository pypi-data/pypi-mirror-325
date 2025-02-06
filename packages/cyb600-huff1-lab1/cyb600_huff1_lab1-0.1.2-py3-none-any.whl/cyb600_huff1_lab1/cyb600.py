import http.server
import socketserver
from datetime import datetime

def start_server(port=8000):
    class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(now.encode())

    with socketserver.TCPServer(("", port), MyRequestHandler) as httpd:
        print(f"Server started at port {port}...")
        httpd.serve_forever()

start_server()

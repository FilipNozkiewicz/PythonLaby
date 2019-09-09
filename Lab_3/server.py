from time import gmtime, strftime
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = strftime("Server date: %Y-%m-%d %H:%M:%S", gmtime())
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(type(post_data))
        print(post_data.decode("utf-8").split(':'))
        message = "Post send successfully."
        self.wfile.write(bytes(message, "utf8"))


print('starting server...')
server_address = ('127.0.0.1', 8095)
httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
print('running server...')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.shutdown()
print('server stopped.')
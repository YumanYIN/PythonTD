from http.server import CGIHTTPRequestHandler, HTTPServer

def createServer():
    """
    Create a server: localhost, port: 8080
    Handled by CGHTTPRequestHandler
    :return:
    """
    handler = CGIHTTPRequestHandler
    handler.cgi_directories = ['/cgi-bin']  # Default directory
    server = HTTPServer(('localhost', 8888), handler)
    # Launch the server
    server.serve_forever()

if __name__ == '__main__':
    createServer()

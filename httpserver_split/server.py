# source from https://pythonbasics.org/webserver/
# Python 3 server example
from http.server import HTTPServer, SimpleHTTPRequestHandler
import cgi
import router

hostName = "localhost"
serverPort = 8080


class MyServer(SimpleHTTPRequestHandler):

    def do_GET(self):

        output, responsecode, contenttype = router.Get(self.path)

        if responsecode == 404:
            self.Send404()
        else:
            self.Send200(output, contenttype)

    def do_POST(self):

        output, responsecode = router.Post(self.path, self.rfile, self.headers)

        if responsecode == 404:
            self.Send404()
        else:
            self.Send200(output)


    def Send200(self, output, contenttype = "text/html"):
        self.send_response(200)
        self.send_header("Content-type", contenttype)
        self.end_headers()

        self.wfile.write(bytes(output, "utf-8"))

    def Send404(self):
        self.send_response(404)
        self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

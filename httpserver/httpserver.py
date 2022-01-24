# source from https://pythonbasics.org/webserver/

# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from lib import db

hostName = "localhost"
serverPort = 8087


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/index2.html":
            filename = "templates/index2.html"
        elif self.path == "/index.html" or self.path == "/":
            filename = "templates/index.html"

        # added separate stylesheet logic
        elif self.path[-4:] == ".css":

            # print(self.path[-4:])
            stylesheet = self.path[1:]
            # print(stylesheet)
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()

            # open stylesheet in css subfolder
            f = open( f"css/{stylesheet}", "r")
            output = ""
            for line in f:
                output += (line.strip())
            self.wfile.write(bytes(output, "utf-8"))
            return

        else:
            filename = ""

        if filename == "":
            self.send_response(404)
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # open template
            f = open( filename, "r")
            output = ""
            for line in f:
                output += (line.strip())

            # lijst van gemeenten
            data = db.GetData("select * from gemeente")

            html_table = ''
            for row in data:
                id = row['det_id']
                gemeente = row['det_txt_nl']
                commune = row['det_txt_fr']

                rij = f"<tr><td class=mytype>{id}</td><td class=mytype>{gemeente}</td><td class=mytype>{commune}</td></tr>"
                html_table += rij

            title = "Gemeenten van België"
            output = output.replace("@@DE_TITLE@@", title)
            output = output.replace("@@LIJST_VAN_GEMEENTEN@@", html_table)

            self.wfile.write(bytes(output, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

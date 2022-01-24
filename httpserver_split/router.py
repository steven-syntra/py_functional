import form1
import index
import index2
from lib import helpers


def Get(path):
    output = ""
    responscode = 200
    contenttype = "text/html"

    if path == "/index2.html":
        output = index2.get()
    elif path == "/index.html" or path == "/":
        output = index.get()
    elif path == "/form1.html":
        output = form1.get()
    # stylesheets are supposed to live in css folder
    elif path[-4:] == ".css":
        output = helpers.GetStyleSheet(path[1:])
        contenttype = "text/css"
    else:
        responscode = 404

    return output, responscode, contenttype


def Post(path, rfile, headers):
    output = ""
    responscode = 200

    if path == "/form1.html":
        output = form1.post(rfile, headers)
    else:
        responscode = 404

    return output, responscode

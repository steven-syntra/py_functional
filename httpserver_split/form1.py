from lib import db, helpers
import cgi


def get():
    output = helpers.OpenTemplate('templates/form1.html')
    return output


def post(rfile, headers):

    # get POST variables with cgi.FieldStorage
    form = cgi.FieldStorage(
        fp=rfile,
        headers=headers,
        environ={'REQUEST_METHOD': 'POST'}
    )
    print(f"The posted id was {form['id'].value}")
    print(f"The posted name was {form['name'].value}")

    output = "i received a POST fo form1"
    return output
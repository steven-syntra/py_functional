from lib import db, helpers


def get():
    output = helpers.OpenTemplate('templates/index2.html')
    return output

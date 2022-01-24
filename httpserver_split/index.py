from lib import db, helpers


def get():
    output = helpers.OpenTemplate('templates/index.html')

    # get list of countries from the database
    data = db.GetData("select * from country")

    # merge template with data
    table = ""
    for row in data:
        table += "<tr><td class=mytype>" + row['country'] + "</td><td class=mytype>" + str(row['last_update']) + "</td></tr>"
    output = output.replace("@@LIST_OF_COUNTRIES@@", table)

    # return output
    return output

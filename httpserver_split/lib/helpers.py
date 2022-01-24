def OpenTemplate(filename):
    output = ""
    with open(filename) as f:
        output = f.read()
    return output


def GetStyleSheet(stylesheet):
    output = ""
    with open( f"{stylesheet}" ) as f:
        output = f.read()
    return output

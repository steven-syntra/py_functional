def headline(text, align=True):
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "*")


print(headline("python type checking", False))

quality = "awesome"
print( f"Python3 formatting is {quality}!" )
print( f"Python3 formatting is {quality.title()}!" )
print( f"__name__ is {__name__}")

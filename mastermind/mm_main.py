from mm_functions import *

# main code
if __name__ == "__main__":
    kleuren = ("R", "G", "B", "O", "P", "W")
    antwoord, gameid = Choose4Colors(kleuren)
    PlayGame(antwoord, gameid)


# What does if __name__ == "__main__": do?
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
#
# Short Answer
# It's boilerplate code that protects users from accidentally
# invoking the script when they didn't intend to. Here are some
# common problems when the guard is omitted from a script:
#
# If you import the guardless script in another script
# (e.g. import my_script_without_a_name_eq_main_guard),
# then the second script will trigger the first to run
# at import time and using the second script's command
# line arguments. This is almost always a mistake.
#
# ...



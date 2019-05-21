# This is the start of the main program
# As said in PoC/Notes.txt I am going to be building this off of the flask framework.
# This is a project that I work on when I have the time as I am involved in school

from flask import Flask

app = Flask(__name__)  # create a new app with the name in parren


@app.route('/')  # tells flask what URL will trigger this function
def hello_world():
    return "Hello World"


@app.route('/beta')
def baoon_1():
    return "I am bacon"


@app.route('/omega/')
def omega():
    return "I am Steve"


@app.route('/eng/<engineer>')
def show_eng_page(engineer):
    # If checking for engineer in the database of engineers
    return "Projects for Engineer %s" % engineer  # ask nick about the percent sign


"""Here would be a if else to check if the Engineer listed is valid. i"""

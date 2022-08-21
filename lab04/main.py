"""
The code is written for COMPSCI235 Lab 4 Flask and Jinja. 


Author: Luke Change (xcha011@aucklanduni.ac.nz) 
Date: 23/07/2022
"""

from markupsafe import escape
from flask import Flask, render_template



app = Flask(__name__)


@app.route('/')
def show_main():
    return render_template('plain.html')


@app.route('/user/<username>')
def show_user_profile(username):
    '''Beware URL encoding. E.g., "Hello world" becomes "Hello%20world"'''
    return f'Hello {escape(username)}! Welcome to COMPSCI235 Lab 3'





if __name__ == '__main__':
    app.run(debug=True, port=8000)

'''
Created on Sep 15, 2017

@author: egikmnq
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
  

if __name__ == '__main__':
    app.run()
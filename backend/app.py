from flask import Flask, request
import datetime
import requests
import os
  
# x = datetime.datetime.now()
# inp = input("name:")
# response = requests.get("http://openlibrary.org/search.json?q="+inp)
# data = (response.json())
  
# Initializing flask app
app = Flask(__name__)
  
inp = "Cracking the Coding Interview"
# inp = input("name:")
response = requests.get("http://openlibrary.org/search.json?q="+inp)
data = (response.json())


@app.route('/book')
def display_book():

    res = {'status': 'success',
            'data': data["docs"]}

    return res
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)
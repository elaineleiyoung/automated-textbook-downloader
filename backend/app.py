from flask import Flask, request
import datetime
import requests
import os
from download import book_info_getter
  
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

@app.route('/download/<keyword>')
def download(keyword):
    return download.book_info_getter(keyword)


# Running app
if __name__ == '__main__':
    app.run(debug=True)
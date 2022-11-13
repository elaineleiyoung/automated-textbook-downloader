from flask import Flask, request
import datetime
import requests
  
# x = datetime.datetime.now()
# inp = input("name:")
# response = requests.get("http://openlibrary.org/search.json?q="+inp)
# data = (response.json())
  
# Initializing flask app
app = Flask(__name__)
  
  
# # Route for seeing a data
# @app.route('/data')
# def get_time():
#     # Returning an api for showing in  reactjs
#     return {
#         'Name':"geek", 
#         "Age":"22",
#         "Date":x, 
#         "programming":"python"
#         }
  
@app.route('/book')
def display_book():
    # x = datetime.datetime.now()
    inp = "cracking the coding interview"
    # inp = input("name:")
    response = requests.get("http://openlibrary.org/search.json?q="+inp)
    data = (response.json())
  
    res = {'status': 'success',
            'data': data["docs"]}

    return res
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)
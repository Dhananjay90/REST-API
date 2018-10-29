#Importing necessary modules
from flask import Flask,jsonify
from bs4 import BeautifulSoup
from flask_jwt import JWT, jwt_required
from security import authenticate,identity

#Creating Flask App instance
app = Flask(__name__)

#Setting Secret key to App instance
app.secret_key = 'secret'

#Creating JWT token
jwt = JWT(app, authenticate,identity)

#Reading dataset from reut2-001.sgm file
file = open('reut2-001.sgm', 'r')
file_data = file.read()

#Parsing sgml data using BeautifulSoup library
parsed_data = BeautifulSoup(file_data,"lxml")

#Identifing the contents using reuters tag
file_contents = parsed_data.findAll("reuters")

#Creating /contents GET endpoint to list all the contents in the dataset
@app.route("/contents")
@jwt_required()   #Appling JWT Authentication functionality to the endpoint
def list_contents():
    result = []
    for content in file_contents:

        result.append(content.text)
    return jsonify(result)



#Creating /contents/places/<string:place> GET endpoint to search contents by country
@app.route("/contents/places/<string:place>")
@jwt_required()   #Appling JWT Authentication functionality to the endpoint
def search_content(place):
    print("Searched place is " + place)
    result = []
    for content in file_contents:
        l=content.text.split("\n")
        place_name = l[3]
        if place==place_name:
            result.append(content.text)
    if result:
        return jsonify(result)
    return jsonify({'message': 'content not found for the searched word'})



#Creating /contents/ids/<string:searched_id> GET endpoint to return contents by NEWID
@app.route('/contents/ids/<string:searched_id>')
@jwt_required()   #Appling JWT Authentication functionality to the endpoint
def findContent(searched_id):
  print("Searched ID is " + searched_id)
  content = parsed_data.find("reuters", newid=searched_id)
  if content:
      return jsonify(content.text)
  return jsonify({'message': 'content not found for the searched id'})

if __name__=="__main__":
    #Run server at port 5000
    app.run(port=5000, debug = True)

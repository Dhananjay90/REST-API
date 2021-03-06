### Objective:
To create 3 REST API's from the given dataset.
1) REST API 1: Rest API to list all the contents from the dataset.
2) REST API 2: Rest API to search the contents.
3) REST API 3: REST API to list the contents by id.

### Given Dataset:
reut2-001.sgm

Contents in the dataset are specified using the SGML tags. Each item in the dataset starts and ends with sgml tags.
The items in the dataset can be identified using the following categories:
1) Places 
2) Orgs
3) Topics 
4) people
5) exchanges

Except places, values for other categories aren't present in all the items.
So, places category was chosen for search REST API. 

### Design considerations:
1) REST API's are designed by following Microsoft REST API Guidelines.
2) Python naming conventions are designed by following PEP-8

### Steps:
1) Install Python3

2) Install the following libraries
	
	pip install beautifulsoup4
	
	pip install bs4
	
	pip install Flask
	
	pip install Flask-JWT
	
	pip install lxml
	
	pip install Werkzeug
	
3) Download the files and go to REST-API folder

4) Run  python app.py. Server runs in port 5000.

	Output should be like below

	C:\Users\dhana\Desktop\h2o challenge\challenge>python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 161-762-270
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
 5) Generate the JWT token using Postman.
		
	HTTP method:POST
	
	url: http://127.0.0.1:5000/auth
	
	Headers: 
	
		Authorization = application/json
		
		Content-Type = application/json
	
	Body (Raw):
		
		{
	"username": "admin",
	"password": "admin"

		}
		
	This will return the access_token
	
	eg) 
	
	{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDA3NzcwODQsImlhdCI6MTU0MDc3Njc4NCwibmJmIjoxNTQwNzc2Nzg0LCJpZGVudGl0eSI6MX0.QuiNkHXzVu5wn9OzwbwIP1fPTOQrdXyeykL1l6P04SI"
	}
	
	JWT token = value of access_token without strings
	
	eg:
	
	JWT token = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NDA3NzcwODQsImlhdCI6MTU0MDc3Njc4NCwibmJmIjoxNTQwNzc2Nzg0LCJpZGVudGl0eSI6MX0.QuiNkHXzVu5wn9OzwbwIP1fPTOQrdXyeykL1l6P04SI
 
 6) Test the REST api's using Postman or curl.
 
	a) Rest Api to list all the contents from the dataset. REST Api returns a list of contents. Users can then customize the data retrieved data according to their requirements
	
		HTTP method:GET
		
		url: http://127.0.0.1:5000/contents   
		
		(or)
		
		curl -X GET --header "Authorization: jwt <jwt token>" http://127.0.0.1:5000/contents
		
		Ouput: List of all the contents will be returned.
		
	b) Rest API to search the contents based on the country. This Api returns the contents matching the input (place name).
	
		HTTP method:GET
		url: http://127.0.0.1:5000/contents/places/<place name>

		eg)  http://127.0.0.1:5000/contents/places/usa
		
		Headers:
			 Authorization = jwt "<JWT token>"
			 
		(or)
		
		curl -X GET --header "Authorization: jwt <jwt token>" http://127.0.0.1:5000/contents/places/usa
		
		Ouput:
		Country name is searched and the the contents for the country category is returned
			 
	c) Rest Api to list the contents based on the unique id.
		
		HTTP method: GET
		url: http://127.0.0.1:5000/contents/ids/<newid>
		
		eg)  http://127.0.0.1:5000/contents/ids/1001
		
		Headers:
			 Authorization = jwt "<JWT token>"
		
		(or)
		
		
		curl -X GET --header "Authorization: jwt <jwt token>" http://127.0.0.1:5000/contents/ids/1001
			 
		Output:
		Content matching the input NEWID is returned
			 
	
		
		
		
		


	



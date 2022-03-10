# Python microservice

## Set Up Virtual Environment in Powershell
1) Upgrade pip to latest version `python -m pip install --upgrade pip`
2) Install virtualenv `pip install virtualenv`
3) Now navigate to location of the folder i.e desktop, documents, etc. `cd .\Desktop`
4) Create a new directory example: `mkdir project-39`
5) Change directory to `cd .\project-39`
6) Now we can create a virtual environment called 'venv', name it anything you like. `virtualenv venv -p (file name)`
7) Activate the virtual environment `.\venv\Scripts\activate`
8) Check the python version. `python -version`
9) Check the list of all packages. `pip list`
10) To deactivate the virtual enviroment. `deactivate`

## Set Up Flask in Powershell 
1) Type `$env:FLASK_APP = "hello"`
2) Then run `flask run` or `python (file).py)` either works 

## To Run Development Server 
1) Run `flask run` 
2) Server should run on port `127.0.0.1:500` or default on PC

## Check for JSON Format Ad, Advertisment and Sponsored table Data
1) Type server port in browser followed by: `/api`

## To See Sponsored, Advertisement or ad JSON in specific collection with a specific member (GET Request)
1) Type server port in browser followed by: `/api/sponsored/ex`, ex in the JSON stands for ExpressVPN. This is to see the specific member of what is being sponsored.
2) For advertisement, type server port in browser follwed by: `/api/advertisement/ty`, ty in the JSON stands for ToysRus. This is to see the specific member of what is being advertised.

## To POST a method to a collection (POST Request)
1) Type server port in browser followed by: `/api/prediction`, enter new `post_text` and `sponsored` and it should be in the collection 
2) Run server port follower by: `/api` to see updated JSON 

## Sources
Articles, Sources and cited: 
https://sonusharma-mnnit.medium.com/building-a-microservice-in-python-ff009da83dac (used some references here as well)
https://dev.to/swarnimwalavalkar/build-and-deploy-a-rest-api-microservice-with-python-flask-and-docker-5c2d (used references here)

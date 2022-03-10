# Set Up Virtual Environment in Powershell
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

# Set Up Flask in Powershell 
1) Type `$env:FLASK_APP = "hello"`
2) Then run `flask run` or `python (file).py) either works 

# To Run Development Server 
1) Run `flask run` 
2) Server should run on port `127.0.0.1`

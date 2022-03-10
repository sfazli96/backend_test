from gc import collect
from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)

INFO = {
    "ad": {
        "st":"Starbucks",
        "pb":"Panera",
        "bp":"Bubble Pop",
    },
    "sponsored": {
        "ex":"ExpressVPN",
        "bk":"Burger King",
        "rd":"Raid Shadow Legends",
    },
    "advertisement": {
        "ty":"ToysRus",
        "tg":"Target",
        "wm":"Walmart",
    }
}

# GET METHOD 
@app.route("/")
def home():
    return "<h1 style='color:blue'>This is home!!</h1>"
    
@app.route("/temp")
def template():
    return render_template('index.html')

@app.route("/vocab")  ## Return the Query String, return the response with 200
def query_string():
    if request.args:
        req=request.args
        res = {}
        for key, value in req.items():
            res[key] = value
        res = make_response(jsonify(res), 200)
        return res
    res = make_response(jsonify({"error":"No query string"}),400)
    return res

@app.route("/api") ## Returns the JSON format only
def get_api():
    res = make_response(jsonify(INFO), 200)
    return res

@app.route("/api/<collection>/<member>") ## Returns the JSON But a specific collection with a specific member 
def get_data(collection, member):
    if collection in INFO:
        member = INFO[collection].get(member)
        if member:
            res = make_response(jsonify({"res":member}),200)
            return res

        res = make_response(jsonify({"error":"Member Not Found"}), 400)
        return res

    res = make_response(jsonify({"error":"Collection Not Found"}), 400)
    return res

# POST METHOD 

@app.route("/api/<collection>", methods=["POST", "GET"])
def create_collection(collection):
    req = request.get_json()

    if collection in INFO:
        res = make_response(jsonify({"error":"post_text already exists"}))
        return res
    
    INFO.update({collection: req})

    res = make_response(jsonify({"message":"post_text created"}), 200)
    return res


    
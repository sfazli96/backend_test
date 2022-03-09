from flask import Flask

app = Flask(__name__)

items_table = [
    {"id": 1, "vocab": "Love these cool toys at #ToysRUs. Go Check Them out", "sponsored": "ToysRUs", "advertisement": "PizzaHut"},
    {"id": 2, "vocab": "Love these cool toys at #Walmart. Go Check Them out", "sponsored": "Walmart", "advertisement": "Mcdonald"},
    {"id": 3, "vocab": "Love these cool toys at #Target. Go Check Them out", "sponsored": "Target", "advertisement": "Starbucks"},
    {"id": 4, "vocab": "Love these cool toys at #BarnesNoble. Go Check Them out", "sponsored": "BarnesNoble", "advertisement": "LittleCaesars"},
]

@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = items_table[id]
    return "{} with an Ad by {} sponsored by {}".format(product["vocab"],product["advertisement"], product["sponsored"])

    
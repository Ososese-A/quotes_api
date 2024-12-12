from flask import Flask, jsonify, render_template, request
from change import change
from courage import courage
from education import education
from friendship import friendship
from happiness import happiness
from leadership import leadership
from life import life
from love import love
from motivation import motivation
from success import success
from wisdom import wisdom
import random 
import json

app = Flask(__name__)
app.register_blueprint(change, url_prefix="/change")
app.register_blueprint(courage, url_prefix="/courage")
app.register_blueprint(education, url_prefix="/education")
app.register_blueprint(friendship, url_prefix="/friendship")
app.register_blueprint(happiness, url_prefix="/happiness")
app.register_blueprint(leadership, url_prefix="/leadership")
app.register_blueprint(life, url_prefix="/life")
app.register_blueprint(love, url_prefix="/love")
app.register_blueprint(motivation, url_prefix="/motivation")
app.register_blueprint(success, url_prefix="/success")
app.register_blueprint(wisdom, url_prefix="/wisdom")

with open("quotes.json") as f:
    json_data = json.load(f)

all_quotes = json_data[0]["quotes"]

category_list = list(all_quotes)

prev_category = []
prev_quote = []

def generate_random_quote():
    while True:
        new_category = random.randint(0, (len(category_list) - 1))
        quote_length = len(json_data[0]["quotes"][category_list[new_category]])
        new_quote = random.randint(0, (quote_length - 1))
        if new_category not in prev_category:
            if new_quote not in prev_quote:
                break
    prev_category.append(new_category)
    prev_quote.append(new_quote)
    if len(prev_category) > 3:
        prev_category.pop(0)
        if len(prev_quote) > 3:
            prev_quote.pop(0)
    return new_category, new_quote

@app.route("/")
def home ():
    return jsonify(all_quotes), 200

@app.route("/random-quote")
def random_quote ():
    random_category, random_quote = generate_random_quote()
    random_quote_res = all_quotes[category_list[random_category]][random_quote]
    return jsonify(random_quote_res), 200

if __name__ == "__main__":
    app.run(debug=True)
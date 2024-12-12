from flask import Blueprint, jsonify
import random
import json

courage = Blueprint("courage", __name__)

with open("quotes.json") as f:
    json_data = json.load(f)

all_quotes = json_data[0]["quotes"]

category = "courage"

prev_quote = []

def generate_random_quote():
    while True:
        quote_length = len(json_data[0]["quotes"][category])
        new_quote = random.randint(0, (quote_length - 1))
        if new_quote not in prev_quote:
            break
    prev_quote.append(new_quote)
    if len(prev_quote) > 3:
        prev_quote.pop(0)
    return new_quote

@courage.route("/")
def get_all_quotes():
    return jsonify(all_quotes[category])

@courage.route("/random-quote")
def get_random_quote():
    random_quote = generate_random_quote()
    print(all_quotes[category][random_quote])
    return jsonify(all_quotes[category][random_quote])
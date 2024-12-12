from flask import Blueprint, jsonify
import json
import random

love = Blueprint("love", __name__)

with open("quotes.json") as f:
    json_data = json.load(f)

all_quotes = json_data[0]["quotes"]

category = "love"

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

@love.route("/")
def get_all_quotes():
    return jsonify(all_quotes[category])

@love.route("/random-quote")
def get_random_quote():
    random_quote =generate_random_quote()
    random_quote_res = all_quotes[category][random_quote]
    return jsonify(random_quote_res), 200
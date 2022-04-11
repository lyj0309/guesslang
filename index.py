from flask import Flask, render_template, request, jsonify

from guesslang import Guess


app = Flask(__name__)

guess = Guess()


@app.route('/', methods=['GET'])
def language():
    source_code = request.args.get['code']
    return guess.language_name(source_code) or 'Text'


def main():
    app.run(host="0.0.0.0",port="9000")
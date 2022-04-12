from flask import Flask, render_template, request, jsonify

from guesslang import Guess


app = Flask(__name__)

guess = Guess()


@app.route('/', methods=["GET", "POST"])
def language():
    source_code = request.args.get('code')
    print("source_code", source_code)
    if source_code == None:
        return ""

    return guess.language_name(source_code) or 'Text'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="9000")

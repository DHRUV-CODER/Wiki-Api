import wikipedia as wp
from flask import Flask, jsonify, render_template
app = Flask(__name__)


@app.route('/')
def sup():
    return "Hi"

@app.route("/wiki/query=<string:a>")
def wiki(a):
    try:
        result_summary = wp.summary(a)
        result = {
            "Result": result_summary
        }
        return jsonify(result)
    except:
        result = {
            "Result": "Not Found"
        }
        return jsonify(result)
        
if __name__ == "__main__":
    app.run(debug=True)

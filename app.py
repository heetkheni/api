import json

from flask import Flask,jsonify

app = Flask(__name__)

places=[
    {
        'places':'surat',
        'id':'1'
    }
]

@app.route('/')
def index():
    return json.dumps(places[0])

if __name__=="__main__":
    app.run(debug=True)


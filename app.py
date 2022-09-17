from flask import Flask,jsonify

app = Flask(__name__)

places=[
    {
        'places':'surat',
        'id':'1'
    }
]

@app.route('/',methods=['GET'])
def get():
    return jsonify({'places':places})

if __name__=="__main__":
    app.run(debug=True)


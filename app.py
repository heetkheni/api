from flask import Flask,jsonify

app = Flask(__name__)

place = [
    {
        'palace':"surat",
    }
]
@app.route('/')
def hello_world():
    return 'hello'

if __name__=="__main__":
    app.run(debug=True)


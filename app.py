from flask import Flask,jsonify
from flask import request

app = Flask(__name__)

places=[
    {
        'places':'surat',
        'id':'1'
    }
]

@app.route('/',methods=['GET','POST'])
def get():
 if request.method=="POST":
    return jsonify({'places': places})
 else :
    return "no error here"

if __name__=="__main__":
    app.run(debug=True)
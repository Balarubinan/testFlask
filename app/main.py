
from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
api = Api(app)
todos = {}

serverVariables={
    "I":0,
    "V":0,
    "P":0,
}

@app.route('/saveStats',methods=["POST"])
def setStat():
    global serverVariables
    print(request.form.keys())
    respObj=request.form
    curVal=float(respObj['I'])
    volVal=float(respObj['V'])
    serverVariables['I']=curVal
    serverVariables['V']=volVal
    serverVariables['P']=curVal*volVal
    return {'power':serverVariables['P']}

@app.route('/getPower')
def getStat():
    return {"power":serverVariables['P']}

# if __name__ == '__main__':
#     app.run(host=os.getenv('IP', '0.0.0.0'),
#             port=int(os.getenv('PORT', 4444)))
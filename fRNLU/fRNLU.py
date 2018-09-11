from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu.config import RasaNLUConfig
import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)
metadata = Metadata.load('/home/sikim/RNLU/models/model_20170403-084112')
interpreter = Interpreter.load(metadata, RasaNLUConfig('/home/sikim/RNLU/config.json'))

@app.route("/index", methods =['GET'])
def index():
	return render_template("index.html")

@app.route("/fetchentityintent/<text>", methods = ['GET'])
def fetchentityintent(text):
	resp = interpreter.parse(unicode(text))
    	return jsonify(resp)

if __name__ == "__main__":
    	app.run(host='0.0.0.0')

from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu.config import RasaNLUConfig
import json

metadata = Metadata.load('./models/model_20170403-084112')
interpreter = Interpreter.load(metadata, RasaNLUConfig("config.json"))

with open("test_data.txt","r") as f:
	t_data = f.readlines()

t_data =[x.strip() for x in t_data]
output = []
for st in t_data:
	resp = interpreter.parse(unicode(st))
       	output.append(resp)

f1 = open('test_output.txt', 'w')
f1.write(json.dumps(output, indent=4))
f1.close()

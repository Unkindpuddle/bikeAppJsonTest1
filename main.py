from flask import Flask
from flask import request
from flask import jsonify
import math
from datetime import *

app = Flask(__name__)

@app.route('/')
def hello_world():
  taco = 'Hello, World!'
  return request.query_string

@app.route('/json_test/')
def json_test(interface=None):

    Lat_S = request.args.get('Lat', '')
    if Lat_S:
      Lat = float(Lat_S)

    Long_S = request.args.get('Long', '')
    if (Long_S):
      Long = float(Long_S)
      
    Bear_S = request.args.get('Bear', '')
    if (Bear_S):
      Bear = float(Bear_S)

    if ( (Long) and (Lat)):
      XMeters = Lat*111111
      YMeters = 111111*Long*math.cos(math.radians(Lat))
      distance = 30
      XMeters += distance*math.sin(math.radians(Bear))
      YMeters += distance*math.cos(math.radians(Bear))

      Lat = XMeters/111111
      Long = (YMeters/111111)/math.cos(math.radians(Lat))
      now = datetime.now();
      d = timedelta(seconds = 60)
      arive1 = now + 1.5*d
      s_arive1 = arive1.isoformat()

      arive2 = now + 2.5*d
      s_arive2 = arive2.isoformat()
      
    mydict = dict({"Lat" : Lat, "Long" : Long, "Times": [s_arive1, s_arive2]})
    return jsonify(mydict)

@app.route('/adhoc_test/')
def adhoc_test():

    Lat_S = request.args.get('Lat', '')
    if Lat_S:
      Lat = float(Lat_S)

    Long_S = request.args.get('Long', '')
    if (Long_S):
      Long = float(Long_S)
      
    Bear_S = request.args.get('Bear', '')
    if (Bear_S):
      Bear = float(Bear_S)

    if ( (Long) and (Lat)):
      XMeters = Lat*111111
      YMeters = 111111*Long*math.cos(math.radians(Lat))
      distance = 30
      XMeters += distance*math.sin(math.radians(Bear))
      YMeters += distance*math.cos(math.radians(Bear))

      Lat = XMeters/111111
      Long = (YMeters/111111)/math.cos(math.radians(Lat))
      now = datetime.now();
      d = timedelta(seconds = 60)
      arive1 = now + 1.5*d
      s_arive1 = arive1.isoformat()

      arive2 = now + 2.5*d
      s_arive2 = arive2.isoformat()
      
    
    mydict = dict({"Lat" : Lat, "Long" : Lng, "Times": [s_arive1, s_arive2]})
    return jsonify(mydict)
  
if __name__ == '__main__':
  app.run()

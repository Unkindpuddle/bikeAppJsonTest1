from flask import Flask
from flask import request
from flask import jsonify
import math

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
      
    mydict = {"Lat" : Lat, "Long" : Long}
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
      
    mydict = {"Lat" : Lat, "Long" : Long}
    return jsonify(mydict)
  
if __name__ == '__main__':
  app.run()

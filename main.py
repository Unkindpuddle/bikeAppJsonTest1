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

    distance = 0
    Dist_S = request.args.get('Dist', '')
    if (Dist_S):
      distance = float(Dist_S)    

    if ( (Long) and (Lat)):
      if(not distance):
        distance = 30
      YOffset = round(distance*math.sin(math.radians(BearingToDegrees(Bear)))/111111,8)
      Lat = YOffset + Lat
      XScale  = (math.cos(math.radians(BearingToDegrees(Bear))))
      XMeters = distance*XScale
      LongScale = math.cos(math.radians(Lat))
      #Lat = Lat + YOffest
      Lat = round(Lat,5) #meter scale accuracy
      XOffset = round((XMeters/111111)/LongScale,8) #preliminary rounding
      Long = round(XOffset + Long,5) # meter scale accuracy
	
	
    now = datetime.now();
    d = timedelta(seconds = 60)
    arive1 = now + 1.5*d
    s_arive1 = arive1.isoformat()

    arive2 = now + 2.5*d
    s_arive2 = arive2.isoformat()
      
    mydict = dict({"Lat" : Lat, "Lng" : Long, "Times": [s_arive1, s_arive2]})
    return jsonify(mydict)

def BearingToDegrees(y): # took an embarisingly long time to figure this out
	return (-y+90)%360
  
if __name__ == '__main__':
  app.run()

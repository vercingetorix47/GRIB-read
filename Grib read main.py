from wwstread import wwst 
import time
from flask import Flask
import json
 
app = Flask(__name__)
gfswave_path = [r"/climatedata/gfs0.grb",r"/climatedata/gfs1.grb",r"/climatedata/gfs2.grb",r"/climatedata/gfs3.grb",r"/climatedata/gfs4.grb",r"/climatedata/gfs5.grb"]
gdas_path = [r"/climatedata/gdas0.grb",r"/climatedata/gdas1.grb",r"/climatedata/gdas2.grb",r"/climatedata/gdas3.grb",r"/climatedata/gdas4.grb",r"/climatedata/gdas5.grb"]

     
@app.get('/')
def home():
    return "Data already loaded.<br> Pass lat and lon as parameters to server address like so - <a href='http://127.0.0.1:5000/single/0/0/0'>http://127.0.0.1:5000/single/[fhr]/[lat]/[lon]</a> <br> Partial data retrieval can also be done in the following format with 0s or 1s for parameters other than lat or lon - <a href='http://127.0.0.1:5000/partial/0/0/0/1/1/1/1/1/1/1/1/1'>http://127.0.0.1:5000/partial/[fhr]/[lat]/[lon]/[wdir]/[ws]/[wvdir]/[wvht]/[wpd]/[swdir]/[swht]/[swpd]/[temp]</a>"

@app.get('/multi/<lat>/<lon>')
def multigrib(lat,lon):
     multi_payload = {}
     for i in range (0,6):
         multi_payload[i]=json.loads(test_object[i].return_json_payload(float(lat),float(lon)))
     json_obj = json.dumps(multi_payload)
     return json_obj
 
@app.get('/single/<fhr>/<lat>/<lon>')
def single_payload(fhr,lat, lon):
    fhr = int(fhr)
    retrieve_time_start = time.perf_counter()
    json_obj = test_object[fhr].return_json_payload(float(lat),float(lon))
    retrieve_time_end = time.perf_counter()
    print(f"Retrieved data in {retrieve_time_end - retrieve_time_start:0.4f} seconds")
    return json_obj

@app.get('/partial/<fhr>/<lat>/<lon>/<wdir>/<ws>/<wvdir>/<shww>/<mpww>/<swdir>/<swell>/<swper>/<t>')
def partial_payload(fhr,lat, lon, wdir=None, ws=None, wvdir=None, shww=None, mpww=None, swdir=None, swell=None, swper=None, t=None):
    dict = {}
    fhr = int(fhr)
    lat = float(lat)
    lon = float(lon)
    if wdir=='1':
        dict['wind_direction']=str(test_object[fhr].wind_direction(lat, lon))
    if ws=='1':
        dict['wind_speed']=str(test_object[fhr].wind_speed(lat, lon))
    if wvdir=='1':
        dict['wave_direction']=str(test_object[fhr].wave_direction(lat, lon))
    if shww=='1':
        dict['wave_height']=str(test_object[fhr].wave_height(lat, lon))
    if mpww=='1':
        dict['wave_period']=str(test_object[fhr].wave_period(lat, lon))
    if swdir=='1':
        dict['swell_direction']=str(test_object[fhr].swell_direction(lat, lon))
    if swell=='1':
        dict['swell_height']=str(test_object[fhr].swell_height(lat, lon))
    if swper=='1':
        dict['swell_period']=str(test_object[fhr].swell_period(lat, lon))
    if t=='1':
        dict['air_temperature']=str(test_object[fhr].air_temperature(lat, lon))
    json_obj = json.dumps(dict)
    return json_obj
 
if __name__ == '__main__':
    load_time_start = time.perf_counter()
    global test_object
    test_object=[]
    for i in range(0,6):
        test_object.append(wwst(gfswave_path[i],gdas_path[i]))
    load_time_end = time.perf_counter()
    print(f"Loaded data in {load_time_end - load_time_start:0.4f} seconds")
    app.run(debug=True,host='0.0.0.0',use_reloader=False)

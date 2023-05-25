from wwstread import wwst 
import time
from flask import Flask
import json
 
app = Flask(__name__)
gfswave_path = r"./gfswave.t18z.global.0p16.f000.grib2"
gdas_path = r"./gdas.t18z.pgrb2.1p00.f000"

@app.get('/')
def home():
    return "Data already loaded.<br> Pass lat and lon as parameters to server address like so - <a href='http://127.0.0.1:5000/full/0/0'>http://127.0.0.1:5000/full/[lat]/[lon]</a> <br> Partial data retrieval can also be done in the following format with 0s or 1s for parameters other than lat or lon - <a href='http://127.0.0.1:5000/partial/0/0/1/1/1/1/1/1/1/1/1'>http://127.0.0.1:5000/partial/[lat]/[lon]/[wdir]/[ws]/[wvdir]/[wvht]/[wpd]/[swdir]/[swht]/[swpd]/[temp]</a>"

@app.get('/full/<lat>/<lon>')
def full_payload(lat, lon):
    retrieve_time_start = time.perf_counter()
    json_obj = test_object.return_json_payload(float(lat),float(lon))
    retrieve_time_end = time.perf_counter()
    print(f"Retrieved data in {retrieve_time_end - retrieve_time_start:0.4f} seconds")
    return json_obj

@app.get('/partial/<lat>/<lon>/<wdir>/<ws>/<wvdir>/<shww>/<mpww>/<swdir>/<swell>/<swper>/<t>')
def partial_payload(lat, lon, wdir=None, ws=None, wvdir=None, shww=None, mpww=None, swdir=None, swell=None, swper=None, t=None):
    dict = {}
    lat = float(lat)
    lon = float(lon)
    if wdir=='1':
        dict['wind_direction']=str(test_object.wind_direction(lat, lon))
    if ws=='1':
        dict['wind_speed']=str(test_object.wind_speed(lat, lon))
    if wvdir=='1':
        dict['wave_direction']=str(test_object.wave_direction(lat, lon))
    if shww=='1':
        dict['wave_height']=str(test_object.wave_height(lat, lon))
    if mpww=='1':
        dict['wave_period']=str(test_object.wave_period(lat, lon))
    if swdir=='1':
        dict['swell_direction']=str(test_object.swell_direction(lat, lon))
    if swell=='1':
        dict['swell_height']=str(test_object.swell_height(lat, lon))
    if swper=='1':
        dict['swell_period']=str(test_object.swell_period(lat, lon))
    if t=='1':
        dict['air_temperature']=str(test_object.air_temperature(lat, lon))
    json_obj = json.dumps(dict)
    return json_obj
 
if __name__ == '__main__':
    load_time_start = time.perf_counter()
    global test_object
    test_object = wwst(gfswave_path,gdas_path)
    load_time_end = time.perf_counter()
    print(f"Loaded data in {load_time_end - load_time_start:0.4f} seconds")
    app.run(debug=True,host='0.0.0.0')
    

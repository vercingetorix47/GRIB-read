# GRIB-read
## DOCKER IMAGE USAGE
All dependencies are already installed onto docker image, as well a copy of this repo (sans the image obviously). Run 'Grib read main.py' to start flask server at http://127.0.0.1:5000/  <br>
The following data parameters can be retrieved from the API - 
- Wind direction - wdir
- Wind speed - ws
- Wave direction - wvdir
- Wave height - wvht
- Wave period - wpd
- Swell direction - swdir
- Swell height - swht
- Swell period - swpd
- Air temperature - temp

<br>These can either be retrieved as a full json payload, or a partial json payload.<br>
For a full payload, pass lat and lon as parameters to server address like so - <a href='http://127.0.0.1:5000/full/0/0'>http://127.0.0.1:5000/full/[lat]/[lon]</a> <br>
For partial data retrieval use the following format with 0s or 1s for parameters other than lat or lon - <a href='http://127.0.0.1:5000/partial/0/0/1/1/1/1/1/1/1/1/1'>http://127.0.0.1:5000/partial/[lat]/[lon]/[wdir]/[ws]/[wvdir]/[wvht]/[wpd]/[swdir]/[swht]/[swpd]/[temp]</a> <br>

## Dependencies
- xarray
- scipy
- ecCodes - https://confluence.ecmwf.int/display/ECC/ecCodes+installation
- cfgrib

## Other details
The data files used are ```gfswave.t18z.global.0p16.f000.grib2``` and ```gdas.t18z.pgrb2.1p00.f000```, which are obtained from NOAA's NOMADS website.
The Python API itself can be used by-
 ```python
 from wwstread import wwst
 ```

Then create a wwst class object to access the functions. wwst can be initialized with filepaths to GFSwave file and GDAS file like -
 ```python
 wwst(gfswave_path,gdas_path)
 ```
Functions included in the class are-
  - ``` load_gfswave(self,gfswave_path) ``` - Takes directory path as input, and loads GFSWave file as a dataframe
  - ``` return_gfswave(self) ``` - Returns dataframe of GFSWave data
  - ``` load_gdas(self,gdas_path) ``` - Takes directory path as input, and loads GDAS file as a dataframe
  - ``` return_gdas(self) ``` - Returns dataframe of GDAS data
  - ``` closest_point(self,point, points) ``` - Function takes target coords as well as list of all coords in dataset as input to return closest point to the input coords
  - ``` wind_direction(self,lat,long) ``` - Returns wind direction value
  - ``` wind_speed(self,lat,long) ``` - Returns wind speed value
  - ``` wave_direction(self,lat,long) ``` - Returns wave direction value
  - ``` wave_height(self,lat,long) ``` - Returns wave height value
  - ``` wave_period(self,lat,long) ``` - Returns wave period value
  - ``` swell_direction(self,lat,long) ``` - Returns swell direction value
  - ``` swell_height(self,lat,long) ``` - Returns swell height value
  - ``` swell_period(self,lat,long) ``` - Returns swell period value
  - ``` air_temperature(self,lat,long) ``` - Returns air temperature value
  - ``` return_json_payload(self,lat,long) ``` - Returns all the parameters in a json payload

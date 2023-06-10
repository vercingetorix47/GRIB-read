# GRIB-read
## DOCKER IMAGE USAGE
BUILD DOCKER IMAGE USING THE FOLLOWING COMMAND IN THE ```docker``` FOLDER - ```docker compose build``` <br>
(The flag ```--no-cache``` can be added if the image needs to be rebuilt (to re-clone git, for example)). <br>
OR DOWNLOAD DOCKER IMAGE USING - ```docker pull vercingetorix47/grib_read``` <br> 
OR DOWNLOAD FROM https://hub.docker.com/r/vercingetorix47/grib_read <br>
All dependencies are already installed onto docker image, as well a copy of this repo.
<br>
Create a docker container from the image using the following command in the ```docker```folder - ```docker compose up```<br>
The container can be stopped and cleaned using ```docker compose down```<br>
<br>
The flask server starts at http://127.0.0.1:5000/  <br>
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

<br>These can either be retrieved as a full json payload of forecast of 6 hours, or a payload of forecast for a single specific hour, or a partial json payload of specific parameters and hour.<br>
For full payload of 6 hours forecast, pass lat and lon as parameters to server address like so - <a href='http://127.0.0.1:5000/multi/0/0'>http://127.0.0.1:5000/multi/[lat]/[lon]</a> <br>
Information for each specific hour can also be fulled by setting fhr value from 0 to 5 like so - <a href='http://127.0.0.1:5000/single/0/0/0'>http://127.0.0.1:5000/single/[fhr]/[lat]/[lon]</a> <br>
Further partial data retrieval can also be done in the following format with 0s or 1s for parameters other than lat or lon - <a href='http://127.0.0.1:5000/partial/0/0/0/1/1/1/1/1/1/1/1/1'>http://127.0.0.1:5000/partial/[fhr]/[lat]/[lon]/[wdir]/[ws]/[wvdir]/[wvht]/[wpd]/[swdir]/[swht]/[swpd]/[temp]</a><br>

## Dependencies
- xarray
- scipy
- ecCodes - https://confluence.ecmwf.int/display/ECC/ecCodes+installation
- cfgrib

## Other details
The data files used are GFSWave and GDAS models at a resolution of 0.25 degrees, which are obtained from NOAA's NOMADS website.<br>
The model files for the current date are automatically downloaded, with forecast data for upto 6 hours ahead. These files are refreshed 4 times a day at 00:30, 06:30,12:30 and 18:30 PT.<br>
The flask service will restart itself shortly after the data files are refreshed with a downtime about 1-2 minutes.

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

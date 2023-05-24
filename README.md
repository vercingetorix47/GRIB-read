# GRIB-read
wwstread.py has an API that can be used to load GFS Wave and GDAS grib files to retrieve the following parameters:
- Wind direction - wdir
- Wind speed - ws
- Wave direction - wvdir
- Wave height - shww
- Wave period - mpww
- Swell direction - swdir
- Swell height - swell
- Swell period - swper
- Air temperature - t

## Dependencies
- xarray
- scipy
- ecCodes - https://confluence.ecmwf.int/display/ECC/ecCodes+installation
- cfgrib

## Usage
'Grib read main.py' can be used to specify the location of your files (either by setting the default location within the file or through the input prompt at runtime) and try out the basic functionailty of this API. Right now, it will call the API, load the data, retrieve the parameters mentioned above, package it into a json payload and print it.
![image](https://github.com/vercingetorix47/GRIB-read/assets/57217002/3e0e5d26-851e-453f-ba7f-7ab2a7c09768)

The API itself can be used by-
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

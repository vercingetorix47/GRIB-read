import xarray as xr
from scipy.spatial.distance import cdist
import json

class wwst:
    gfswave_points=[]
    gdas_points=[]
    closest_gfswave_points=None
    closest_gdas_points=None
    current_point=None
    def __init__(self, gfswave_path = None, gdas_path = None):
        if gfswave_path!=None:
            self.load_gfswave(gfswave_path)
        if gdas_path!=None:
            self.load_gdas(gdas_path)
    def load_gfswave(self,gfswave_path):
        ds=xr.open_dataset(gfswave_path,engine='cfgrib',backend_kwargs={'indexpath': ''})
        self.gfswave_df = ds.to_dataframe()
        lat_gfswave=[]
        lon_gfswave=[]
        for i in self.gfswave_df.index:
            x,y,z = i
            lat_gfswave.append(x)
            lon_gfswave.append(y)
        self.gfswave_points = [(x, y) for x,y in zip(lat_gfswave, lon_gfswave)]
        self.closest_gfswave_points=None
        self.gfswave_df.reset_index()
    def return_gfswave(self):
        return self.gfswave_df
    def load_gdas(self,gdas_path):
        ds=xr.open_dataset(gdas_path,engine='cfgrib',backend_kwargs={'indexpath': ''})
        self.gdas_df = ds.to_dataframe()
        lat_gdas=[]
        lon_gdas=[]
        for i in self.gdas_df.index:
            x,y = i
            lat_gdas.append(x)
            lon_gdas.append(y)
        self.gdas_points = [(x, y) for x,y in zip(lat_gdas, lon_gdas)]
        self.closest_gdas_points=None
        self.gdas_df.reset_index()
    def return_gdas(self):
        return self.gdas_df
    def closest_point(self,point, points):
        self.current_point = point
        return [cdist([point], points).argmin()]
    def wind_direction(self,lat,long):
        if self.closest_gfswave_points==None:
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        if self.current_point!=(lat,long):
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        return self.gfswave_df.iloc[self.closest_gfswave_points[0]]['wdir']
    def wind_speed(self,lat,long):
        if self.closest_gfswave_points==None:
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        if self.current_point!=(lat,long):
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        return self.gfswave_df.iloc[self.closest_gfswave_points[0]]['ws']
    def wave_direction(self,lat,long):
        if self.closest_gfswave_points==None:
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        if self.current_point!=(lat,long):
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        return self.gfswave_df.iloc[self.closest_gfswave_points[0]]['wvdir']
    def wave_height(self,lat,long):
        if self.closest_gfswave_points==None:
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        if self.current_point!=(lat,long):
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        return self.gfswave_df.iloc[self.closest_gfswave_points[0]]['shww']
    def wave_period(self,lat,long):
        if self.closest_gfswave_points==None:
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        if self.current_point!=(lat,long):
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        return self.gfswave_df.iloc[self.closest_gfswave_points[0]]['mpww']
    def swell_direction(self,lat,long):
        if self.closest_gfswave_points==None:
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        if self.current_point!=(lat,long):
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        return self.gfswave_df.iloc[self.closest_gfswave_points[0]]['swdir']
    def swell_height(self,lat,long):
        if self.closest_gfswave_points==None:
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        if self.current_point!=(lat,long):
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        return self.gfswave_df.iloc[self.closest_gfswave_points[0]]['swell']
    def swell_period(self,lat,long):
        if self.closest_gfswave_points==None:
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        if self.current_point!=(lat,long):
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        return self.gfswave_df.iloc[self.closest_gfswave_points[0]]['swper']
    def air_temperature(self,lat,long):
        if self.closest_gdas_points==None:
            self.closest_gdas_points=self.closest_point((lat,long),list(self.gdas_points))
        if self.current_point!=(lat,long):
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
        return self.gdas_df.iloc[self.closest_gdas_points[0]]['t']
    def return_json_payload(self,lat,long):
        if self.current_point!=(lat,long):
            self.closest_gfswave_points=self.closest_point((lat,long),list(self.gfswave_points))
            self.closest_gdas_points=self.closest_point((lat,long),list(self.gdas_points))
        payload = {'wind_direction':str(self.wind_direction(lat, long)),'wind_speed':str(self.wind_speed(lat, long)),'wave_direction':str(self.wave_direction(lat, long)),
                   'wave_height':str(self.wave_height(lat, long)),'wave_period':str(self.wave_period(lat, long)),'swell_direction':str(self.swell_direction(lat, long)),
                   'swell_height':str(self.swell_height(lat, long)),'swell_period':str(self.swell_period(lat, long)),'air_temperature':str(self.air_temperature(lat, long))}
        return json.dumps(payload)

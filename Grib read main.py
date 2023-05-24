from wwstread import wwst 
import time

def main():
    if input("Do you want input directory(otherwise use default dir)?(y/n)")=='n':
        gfswave_path = r"DEFAULT PATH HERE"
        gdas_path = r"DEFAULT PATH HERE"
    else:
        gfswave_path = input("Path of GFS Wave file :")
        gfswave_path = r"{}".format(gfswave_path)
        gdas_path = input("Path of GDAS file :")
        gdas_path = r"{}".format(gdas_path)
    print("Loading data")
    load_time_start = time.perf_counter()
    test_object = wwst(gfswave_path,gdas_path)
    load_time_end = time.perf_counter()
    print("Loaded data")
    lat = float(input("Latitude :"))
    long = float(input("Longitude :"))
    print("Retrieving data for requested coords as json")
    retrieve_time_start = time.perf_counter()
    json_obj = test_object.return_json_payload(lat,long)
    retrieve_time_end = time.perf_counter()
    print("Retrieved data")
    print(json_obj)
    print(f"Loaded data in {load_time_end - load_time_start:0.4f} seconds")
    print(f"Retrieved data in {retrieve_time_end - retrieve_time_start:0.4f} seconds")
    
if __name__ == "__main__":
    main()
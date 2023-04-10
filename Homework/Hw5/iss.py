"""
This program contains 1 function working with API named track_iss().

Author: Nguyen Chinh Quan
Time spent: 3 days
"""
import requests
import time
def track_iss():
    """
    This function prints out the current ISS position including latitude and longitude and the location it's on.
    This function will terminate once it has been running for 5 minutes
    or as soon as the ISS makes a transition from being over water to over land (or vice versa).
    """
    count_ocean = 0
    count_land = 0
    i = 1
    while i <= 30:
        i += 1
        url_ISS = "http://api.open-notify.org/iss-now.json"
        url_GeoNames = "http://api.geonames.org/findNearbyJSON?"
        url_GeoNames_ocean = "http://api.geonames.org/oceanJSON?"
        username = "nhimmu21"
        response_ISS = requests.get(url_ISS)
        if response_ISS.status_code == 404:
            print("The resource you tried to access was not found on the server.")
            break
        iss_position = response_ISS.json()["iss_position"]
        latitude = iss_position["latitude"]
        longitude = iss_position["longitude"]
        parameters = {
            "lat": latitude,
            "lng": longitude,
            "username": username
        }
        response_GeoNames_ocean = requests.get(url_GeoNames_ocean, params=parameters)
        if response_GeoNames_ocean.status_code != 200:
            print("The resource you tried to access was not found on the server.")
            break
        response_GeoNames = requests.get(url_GeoNames, params=parameters)
        if response_GeoNames.status_code == 404:
            print("The resource you tried to access was not found on the server.")
            break
        location_land = response_GeoNames.json()['geonames']
        if list(response_GeoNames_ocean.json().keys())[0] == "ocean":
            count_ocean += 1
            location_ocean = response_GeoNames_ocean.json()['ocean']
            ocean_Name = location_ocean['name']
            print("Current ISS position: " + str(latitude) + ', ' + str(longitude) + ' (over ' + str(ocean_Name) + ')')
        else:
            count_land += 1
            toponym_Name = location_land[0]['toponymName']
            country_Name = location_land[0]['countryName']
            print("Current ISS position: " + str(latitude) + ', ' + str(longitude) + ' (over ' + str(toponym_Name) +
                  ', ' + str(country_Name) + ')')
        if count_ocean > 0 and count_land > 0:
            break
        time.sleep(10)
#track_iss()


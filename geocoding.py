"""
==========================================
classe :
    geocoding
methode : 
    geocode_address(address): latitude, longitude => résultat de la requet de l'api 
==========================================
"""

# importations des librairie
import googlemaps
from dotenv import load_dotenv
import os

repertoir_fichier = os.path.dirname(__file__)
env_path = f'{repertoir_fichier}/.env'
load_dotenv(dotenv_path=env_path)


api_key = os.getenv('GEOCODING_KEY')
gmaps = googlemaps.Client(key=api_key)

def geocode_address(address):
    # Geocode the address
    geocode_result = gmaps.geocode(address, language = 'fr')
    
    # Extract latitude and longitude from the geocode result
    if geocode_result and 'geometry' in geocode_result[0] and 'location' in geocode_result[0]['geometry']:
        location = geocode_result[0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']
        return latitude, longitude
    else:
        return None
    
latitude_1, longitude_1 = geocode_address('tours')
print("latitude, longitude :",latitude_1, longitude_1)

latitude_2, longitude_2 = geocode_address('paris')
print("latitude, longitude :",latitude_2, longitude_2)
#from pygal_maps_world.i18n import COUNTRIES
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        #print(code, name)
        if country_name == name:
            return code

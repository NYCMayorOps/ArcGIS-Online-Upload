import os
import arcgis
from arcgis.gis import GIS
from dotenv import load_dotenv
from pathlib import Path
secrets_file = Path(f'C:\\Users\\{os.getlogin()}\\secrets\\.env')
load_dotenv(secrets_file)
ESRI_USERNAME = os.getenv('ESRI_USERNAME')
ESRI_PASSWORD = os.getenv('ESRI_PASSWORD')
assert ESRI_USERNAME is not None
assert ESRI_PASSWORD is not None

class Authenticate:

    def __init__(self):
        self.gis = self.authenticate()

    def authenticate(self) -> arcgis.gis.GIS:
        gis = GIS("https://www.arcgis.com", ESRI_USERNAME, ESRI_PASSWORD)
        print("Logged in as " + str(gis.properties.user.username))
        return gis

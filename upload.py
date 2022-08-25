
import os
import arcgis
from pathlib import Path
from dotenv import load_dotenv
from authenticate import Authenticate


def upload_shapefile(gis: arcgis.gis.GIS, filename: str, filepath: Path, tags: str):
    #this will upload a file, but it will not be a feature layer.
    #you may download it but not interact with it
    file_properties={'title': filename,
                    'type': 'Shapefile',
                    'tags': tags,
                    'overWrite': True}
    file_item =  gis.content.add(data=filepath,
                                item_properties=file_properties,
                                thumbnail=None,
                                overwrite=True)
    return file_item

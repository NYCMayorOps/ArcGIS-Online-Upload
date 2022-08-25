
import os
from pathlib import Path
from dotenv import load_dotenv
from upload import upload_shapefile
from authenticate import Authenticate
secrets_file = Path(f'C:\\Users\\{os.getlogin()}\\secrets\\.env')
load_dotenv(secrets_file)

GIS_PATH=os.getenv('GIS_PATH')
if __name__ == '__main__':
    gis = Authenticate().gis
    filename='test_upload_from_python'
    filepath = GIS_PATH + 'nycparksopenspace.zip'
    file_item = upload_shapefile(gis, filename, filepath, tags='python, test')
    file_item.share(org=True)
    file_item.publish(overwrite=True)
    print(f'{filename} uploaded')

# Im kind of lazy and tired and havent thought about the best way to make this file so it is usable by everyone
# Should I accept command line arguments that represent the desired year, as well as the path you want to save the file to?
import requests, zipfile, io
zip_file_url = 'https://github.com/guga31bb/nflfastR-data/raw/master/data/play_by_play_1999.zip'
r = requests.get(zip_file_url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("C:/Users/jrsav/Documents/Fall Semester 2020/Machine Learning/Final Project")
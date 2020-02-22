#!/usr/bin/env python3.8
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from hw16 import gmaps, print_info_about

"""
    Написать скрипт, который будет вытаскивать gps данные
    из фотографии (jpg файл) и передавать их на вход программе
    из hw16.txt
"""

def retrieve_coordinates_block(exif_data):
    for key, value in exif_data.items():
        if TAGS.get(key) == 'GPSInfo':
            ret = value
    return ret
    
def _convert_to_degress(value: list) -> float:
    return (float(value[0][0]) / float(value[0][1]) + 
            float(value[1][0]) / float(value[1][1]) / 60 + 
            float(value[2][0]) / float(value[2][1]) / 3600) * (1 if True else -1)

def main():
    data = Image.open('temp/03.jpg')._getexif()
    b = retrieve_coordinates_block(data)
    print_info_about(_convert_to_degress(b[2]),
                     _convert_to_degress(b[4]))

if __name__ == "__main__":
    main()

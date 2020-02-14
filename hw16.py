#!/usr/bin/env python3.8
import re
import googlemaps

"""
    Написать программу, которая будет считывать из файла gps координаты,
    и формировать текстовое описание объекта и ссылку на google maps.
    Пример:

    Input data: 60,01';30,19'
    Output data:
    Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
    Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322
"""

gmaps = googlemaps.Client(key='AIzaSyB2421b9hl9XVxPkVt3kHYZD9MQjMDtBUA')

def form_degrees(in_str: str) -> float:
    a = re.match(r"([0-9]+)[,\.]([0-9]+)([']?)", in_str).groups()
    if a[2] == "'":
        return float(a[0]) + float('0.' + a[1])* 100 / 60
    else: 
        return float(a[0]) + float('0.' + a[1])

def get_input() -> list:
    f = open('hw16_input.txt', 'r')
    lines = f.readlines()
    ret = [[form_degrees(a) for a in x.split(';')] for x in lines]
    return ret

def print_info_about(lat: float, lng: int):
    reverse_geocode_result = gmaps.reverse_geocode((lat, lng))
    a, b = reverse_geocode_result[0]['geometry']['location']['lat'], reverse_geocode_result[0]['geometry']['location']['lng']
    print(reverse_geocode_result[0]['formatted_address'])
    print('Google Maps URL:', f'https://www.google.com/maps/search/?api=1&query={a},{b}')

def main():
    input_coordinates = get_input()
    for coordinates in input_coordinates:
        lat, lng = coordinates
        print('----', f'{lat:.3f} : {lng:.3f}', '----')
        print_info_about(lat, lng)

if __name__ == "__main__":
    main()

from classes.City import City
from classes.PhotoSource import PhotoSource
from classes.ImageProcessing import getAverageColor, getImageArrayFromFile, getImageArrayFromUrl

from typing import List

import jsonpickle

import os

def main():
    cities = loadConfig("cities.json")

    results = {}

    for city in cities:
        results[city.Name] = [getAverageColor(getImageArrayFromUrl(ps.Url, ps.Kind)) for ps in city.PhotoSourceList]

    print(results)

def loadConfig(filePath) -> List[City]:
    with open(filePath, 'r') as f:
        return jsonpickle.decode(f.read())


if __name__ == '__main__':
    main()
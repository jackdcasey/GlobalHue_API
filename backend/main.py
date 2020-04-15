from classes.City import City
from classes.PhotoSource import PhotoSource
from classes.ImageProcessing import processPhotoSourceList

from typing import List

import jsonpickle

import os

def main():

    print("Starting")

    cwd = os.path.dirname(os.path.abspath(__file__))
    citiesFile = os.path.join(cwd, 'cities.json')

    print(f"Loading from {citiesFile}")

    cities = loadConfig(citiesFile)

    results = {}

    for city in cities:

        print(city.Name)

        try:
            results[city.Name] = processPhotoSourceList(city.PhotoSourceList)
        except:
            pass

    print(results)

    print("Exiting")

def loadConfig(filePath) -> List[City]:
    with open(filePath, 'r') as f:
        return jsonpickle.decode(f.read())


if __name__ == '__main__':
    main()
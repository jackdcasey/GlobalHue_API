from classes.City import City
from classes.PhotoSource import PhotoSource
from classes.ImageProcessing import processPhotoSourceList

from typing import List

import jsonpickle

def main():

    cities = loadConfig("cities.json")

    results = {}

    for city in cities:

        results[city.Name] = processPhotoSourceList(city.PhotoSourceList)

    print(results)

def loadConfig(filePath) -> List[City]:
    with open(filePath, 'r') as f:
        return jsonpickle.decode(f.read())


if __name__ == '__main__':
    main()
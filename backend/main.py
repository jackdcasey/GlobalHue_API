from classes.City import City
from classes.PhotoSource import PhotoSource

from typing import List

import jsonpickle

def main():
    cities = loadConfig("cities.json")

    # TODO :)

def loadConfig(filePath) -> List[City]:
    with open(filePath, 'r') as f:
        return jsonpickle.decode(f.read())


if __name__ == '__main__':
    main()
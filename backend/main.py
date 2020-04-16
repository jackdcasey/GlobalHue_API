from classes.City import City
from classes.PhotoSource import PhotoSource
from classes.ImageProcessing import processPhotoSourceList
from classes.db import WriteToDatabase, GetAllInTable

from typing import List

import jsonpickle, schedule

import os, time

def main():

    start()
    schedule.every(1).minutes.do(start)

    while True:
        schedule.run_pending()
        time.sleep(1)

def start():

    print("Starting")

    cwd = os.path.dirname(os.path.abspath(__file__))
    citiesFile = os.path.join(cwd, 'cities.json')

    print(f"Loading from {citiesFile}")

    cities = loadConfig(citiesFile)

    for city in cities:

        print(city.Name)

        try:
            color = processPhotoSourceList(city.PhotoSourceList)
        except LookupError:
            color = "Error"

        WriteToDatabase('GlobalHue_Current',
            {
                'location': city.Name,
                'color': color
            }
        )

    print("Exiting")

def loadConfig(filePath) -> List[City]:
    with open(filePath, 'r') as f:
        return jsonpickle.decode(f.read())


if __name__ == '__main__':
    main()
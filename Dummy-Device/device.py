import pyrebase
from datetime import datetime
import time
import random

# ------ Important ------
# This won't run on python 3.10 or above. Run in python 3.9 or below
# pip install pyrebase

# Change deviceID, and sleep time as your preference
DEVICE_ID = 1
SLEEP_TIME = 5      # minutes

''' firebaseConfig={"apiKey": "qSErU9t9a7O8Tj2vTJWPdatLBlbFJ58c7twgkIuh",
    "authDomain": "new-arduino-project-default-rtdb.asia-southeast1.firebasedatabase.app",
    "databaseURL": "https://smart-planting-system-b7c5e-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "new-arduino-project",
    "storageBucket": "pyrebaserealtimedbdemo.appspot.com",
    "messagingSenderId": "843349173643",
    "appId": "1:843349173643:web:90ff345ff844aa89d5fb8e",
    "measurementId": "G-DT093HRL5R"} '''

firebaseConfig={"apiKey": "qSErU9t9a7O8Tj2vTJWPdatLBlbFJ58c7twgkIuh",
    "authDomain": "smart-planting-system-b7c5e-default-rtdb.asia-southeast1.firebasedatabase.app",
    "databaseURL": "https://smart-planting-system-b7c5e-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "smart-planting-system-b7c5e",
    "storageBucket": "smart-planting-system-b7c5e.appspot.com"}

# Reference
# LightIntensity: F = full shade S = semi-shade N = no shade
# Soil Moisture: D = dry M = Moist We = wet Wa = water
# Water level:  level 3 -------- OK
#               level 2 -------- OK
#               level 1 -------- Low water warning
#               level 0 -------- Do not turn on pump!!

lightList = ['F', 'S', 'N']
moistureList = ['D', 'M', 'We', 'Wa']
waterList = ['level 3', 'level 2', 'level 1', 'level 0']

# Get user inputs for device ID and sleep time
DEVICE_ID = input("Enter Device ID: ")
SLEEP_TIME = int(input("Enter a time interval(minutes): "))

if(SLEEP_TIME < 1):
    SLEEP_TIME = 1

# Do not change
# ---------------------------
while True:
    DateTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    LightIntensity = random.choice(lightList)
    SoilMoisture = random.choice(moistureList)
    Temperature = str(round(random.uniform(8.5, 40.9), 1)) + "°C"
    WaterLevel = random.choice(waterList)

    print(DateTime)

    firebase=pyrebase.initialize_app(firebaseConfig)

    db=firebase.database()

    #Multi-location update data
    data = {"plants/" + DEVICE_ID:{"DateTime":DateTime, "LightIntensity" : LightIntensity, "SoilMoisture": SoilMoisture, "Temperature":Temperature, "WaterLevel": WaterLevel}}
    db.update(data)

    # Sleep time
    time.sleep(SLEEP_TIME * 60)

# ---------------------------
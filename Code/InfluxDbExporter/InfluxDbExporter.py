import pandas as pd
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import numpy as np
import os

############################ SECTION: Importing dataset from InfluxDB ############################
bucket = "casa-mqtt-data"
org = "casa0014"
token = "################# YOUR TOKEN HERE ##################=="
# Store the URL of your InfluxDB instance
url="################# YOUR URL HERE ##################"
fromDate = '2023-08-20T16:00:12.000000000Z'  #2023-08-20 17:32:12
toDate = '2023-08-23T01:20:43.941926044Z' #2023-08-23 01:11:43

def influxDbQuery(valueName):
    client = influxdb_client.InfluxDBClient(
       url=url,
       token=token,
       org=org
    )
    query_api = client.query_api()
    query = 'from(bucket: "'+bucket+'")\
    |> range(start:' + fromDate + ' , stop:' + toDate + ' )\
    |> filter(fn: (r) => r["_field"] == "value")\
    |> filter(fn: (r) => r["plant-topics"] == "loraMesh/BR1/'+valueName+'")'
    result = query_api.query(org=org, query=query)
    results = []
    for table in result:
      for record in table.records:
        results.append((record.get_time(), record.get_value()))
    return results
   

selectedSensorReading = influxDbQuery('Light')


print(len(selectedSensorReading))


############################ SECTION: Converting the shape of the dataset ############################


selectedSensorReadingDataset = np.array(selectedSensorReading)[:, 1]

datetimeDataset = np.array(selectedSensorReading)[:, 0]

df = pd.DataFrame({'datetime':datetimeDataset, 'Light':selectedSensorReadingDataset})

df.to_csv('importedDataset.csv')
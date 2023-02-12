import json
import urllib.request

json_data_source = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/9/1880-2022.json'

#with open(json_data_source, 'r', encoding= 'utf-8') as data:
with urllib.request.urlopen(json_data_source) as json_stream:
    # Read the data from the stream we've opened, and decode it from UTF-8
    data = json_stream.read().decode('utf-8')
    # Decode the data after reading
    anomalies = json.loads(json_stream)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ... {value:6.2f}')
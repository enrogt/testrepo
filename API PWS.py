# Importación de librerías
from datetime import datetime
import requests
import json
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

today = datetime.now()
today = str(today)
# print(today)

# Credenciales de la API
app_key = '59263A759A7D799C0168DF3B005A6731'
api_key = 'e5065688-aa9d-48eb-be19-8ee7090a849d'
mac_almacen = 'E8:DB:84:E3:E2:6F'


''' 
###Tiempo real
url_almacen = 'https://api.ecowitt.net/api/v3/device/real_time?application_key={}&api_key={}&mac={}&call_back=all'.format(app_key,api_key,mac_almacen)
url_almacen_request = requests.get(url_almacen, params={'temp_unitid':1,'wind_speed_unitid':7,'rainfall_unitid':12}).text
print(url_almacen_request)
'''

# Historical data
## url con datos
url_almacen_hist = 'https://api.ecowitt.net/api/v3/device/history?application_key={}&api_key={}&mac={}&start_date=2023-08-04 00:00:00&end_date=2023-08-05 00:00:00&cycle_type=30min&call_back=rainfall,outdoor.temperature,solar_and_uvi'.format(app_key,api_key,mac_almacen)
almacen_hist = requests.get(url_almacen_hist, params={'rainfall_unitid':12,'temp_unitid':1}).text
# print(almacen_hist)

results_almacen_hist = json.loads(almacen_hist)
# print(results_almacen_hist)

results_almacen_hist = pd.DataFrame(results_almacen_hist['data']['outdoor'])

print(results)


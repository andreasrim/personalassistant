import xml.etree.ElementTree as ET
# <link text="Værvarsel fra Yr, levert av NRK og Meteorologisk institutt" url="http://www.yr.no/sted/Norge/Trøndelag/Trondheim/Trondheim/"/>

tree = ET.parse("varsel.xml")
root = tree.getroot()

for child in root[5][1]: 
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild)


print("="*25)

print(root[5][1][0])

print("="*25)


def get_forecast_week():
    for forecast in root[5][1].findall('time'):
        print(forecast.attrib["from"], forecast.attrib["to"], forecast.attrib["period"])
        print(forecast.find('temperature').attrib, forecast.attrib)

def get_temperature_now():
    forecast = root[5][1].find('time')
    return forecast.find('temperature').attrib


def get_forecast_now():
    forecast = root[5][1].find('time')
    description = forecast.find('symbol').attrib
    wind = forecast.find('windSpeed').attrib
    temp = forecast.find('temperature').attrib
    return [description, temp, wind]   

def forecast_to_string(forecast):
    description_dict = forecast[0]
    description = description_dict.get("name")
    temp_dict = forecast[1]
    temp = temp_dict.get("value")
    temp_unit = temp_dict.get("unit")
    wind_dict = forecast[2]
    wind = wind_dict.get("name")
    forecast = description + " " + temp + temp_unit + " " + wind
    return forecast


print(forecast_to_string(get_forecast_now()))

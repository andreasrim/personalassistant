import xml.etree.ElementTree as ET
import os
from urllib import request


# <link text="Værvarsel fra Yr, levert av NRK og Meteorologisk institutt" url="http://www.yr.no/sted/Norge/Trøndelag/Trondheim/Trondheim/"/>

class Weather:

	root = ""

	def __init__(self):
		#try:
			parser = ET.XMLParser(encoding="utf-8")
			tree = ET.parse("test.xml", parser=parser)
			self.root = tree.getroot()
			
		#except:	
		#	self.get_forecast_yr()
		#	tree = ET.parse("varsel.xml")
		#	self.root = tree.getroot()


	def get_forecast_week(self):
		for forecast in self.root[5][1].findall('time'):
			print(forecast.attrib["from"], forecast.attrib["to"], forecast.attrib["period"])
			print(forecast.find('temperature').attrib, forecast.attrib)

	def get_temperature_now(self):
		forecast = self.root[5][1].find('time')
		return forecast.find('temperature').attrib


	def get_forecast_now(self):
		self.get_forecast_yr
		location = self.root.find("./location/name").text
		forecast = self.root[5][1].find('time')
		description = forecast.find('symbol').attrib
		wind = forecast.find('windSpeed').attrib
		temp = forecast.find('temperature').attrib
		return [location, description, temp, wind]   

	def forecast_to_string(self, forecast):
		location = forecast[0]
		description_dict = forecast[1]
		description = description_dict.get("name")
		temp_dict = forecast[2]
		temp = temp_dict.get("value")
		temp_unit = temp_dict.get("unit")
		wind_dict = forecast[3]
		wind = wind_dict.get("name")
		forecast = location + " " + description + " " + temp + " " + temp_unit + " " + wind
		return forecast

	def check_forecast_last_update(self):
		last_update = self.root[3][1]
		return last_update.text

	# bør ikke kjøres mer enn en gang hvert 10. min
	def get_forecast_yr(self):
		#resp = request.urlopen("https://www.yr.no/sted/Norge/Trøndelag/Trondheim/Trondheim/varsel.xml")
		resp = request.urlopen("http://localhost:8000/test.xml")
		if resp.code == 200: 
			data = resp.read()
			with open("test.xml", "wb") as f:
				f.write(data)
		else: 
			print("<-------------Access denied-------->")



forecast = Weather()
forecast.get_forecast_now()

print(forecast.forecast_to_string(forecast.get_forecast_now()))

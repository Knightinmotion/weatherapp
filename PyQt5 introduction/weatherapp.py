import sys

import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QVBoxLayout, QPushButton, QLineEdit)
from PyQt5.QtCore import Qt
from requests import RequestException


class WeatherApp(QWidget):
	
	def __init__(self):
		super().__init__()
		self.city_label = QLabel("Enter city name: ", self)
		self.city_input = QLineEdit(self)
		self.get_weather_button = QPushButton("Get weather", self)
		self.temperature_label = QLabel(self)
		self.emoji_label = QLabel(self)
		self.description_label = QLabel(self)
		self.initUI()
	
	def initUI(self):
		self.setWindowTitle("Weather App")
		
		vbox = QVBoxLayout()
		
		vbox.addWidget(self.city_label)
		vbox.addWidget(self.city_input)
		vbox.addWidget(self.get_weather_button)
		vbox.addWidget(self.temperature_label)
		vbox.addWidget(self.emoji_label)
		vbox.addWidget(self.description_label)
		
		self.setLayout(vbox)
		
		self.city_label.setAlignment(Qt.AlignCenter)
		self.city_input.setAlignment(Qt.AlignCenter)
		self.temperature_label.setAlignment(Qt.AlignCenter)
		self.emoji_label.setAlignment(Qt.AlignCenter)
		self.description_label.setAlignment(Qt.AlignCenter)
		
		self.city_label.setObjectName("city_label")
		self.city_input.setObjectName("city_input")
		self.get_weather_button.setObjectName("get_weather_button")
		self.temperature_label.setObjectName("temperature_label")
		self.emoji_label.setObjectName("emoji_label")
		self.description_label.setObjectName("description_label")
		
		self.setStyleSheet("""
			QLabel, QPushButton{
				font-family: calibri;
			}
			QLabel#city_label{
				font-size: 25px; 
				font-style: italic;
			}
			QLineEdit#city_input{
				font-size: 20px;
			}
			QPushButton#get_weather_button{
				font-size: 25px;
				font-weight:bold;
			}
			QLabel#temperature_label{
				font-size: 35px;
			}
			QLabel#emoji_label{
				font-size: 85px;
				font-family: Segoe UI emoji;
			}
			QLabel#description_label{
				font-size: 30px;
			}
		""")
		
		self.get_weather_button.clicked.connect(self.get_weather)
	
	def get_weather(self):
		api_key = "ab71c4062929c438b5e330984b39c620"
		city = self.city_input.text()
		url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
		
		try:
			response = requests.get(url)
			response.raise_for_status()
			data = response.json()
			
			if data["cod"] == 200:
				self.display_weather(data)
		
		except requests.exceptions.HTTPError:
			match response.status_code:
				case 400:
					print("Bad request\nPlease check your input")
				case 401:
					print("Unauthorized\nPlease check your input")
				case 403:
					print("Forbidden\nAccess is denied")
				case 404:
					print("Not found\nCity not found")
				case 500:
					print("Internal Server Error\nPlease check your input")
				case 502:
					print("Bad Gateway\nInvalid response form the server")
				case 503:
					print("Service Unavailable\nServer is down")
				case 504:
					print("Gateway Timeout\nNo response from the server")
				case _:
					print(f"HTTP error occurred\nStatus Code: {response.status_code}")
		
		except requests.exceptions.ConnectionError:
			print("Connection Error: \nCheck your internet connection")
		except requests.exceptions.Timeout:
			print("Timeout Error:\nThe request timed out")
		except requests.exceptions.TooManyRedirects:
			print("Too many Redirects: \nCheck the URL")
		except requests.exceptions.RequestException as req_error:
			print(f"Request Error:\n {req_error}")
	
	def display_error(self, message):
		self.temperature_label.setStyleSheet("font-size: 30px;")
		self.temperature_label.setText(message)
	
	def display_weather(self, data):
		# Extract weather data
		temp_kelvin = data['main']['temp']
		temp_celsius = temp_kelvin - 273.15
		weather_desc = data['weather'][0]['description'].title()
		condition = data['weather'][0]['main'].lower()
		
		# Set emoji based on weather condition
		emojis = {
			'clear': '☀️',
			'clouds': '☁️',
			'rain': '🌧️',
			'thunderstorm': '⛈️',
			'snow': '❄️',
			'mist': '🌫️',
			'drizzle': '🌦️'
		}
		emoji = emojis.get(condition, '🌈')
		
		# Update UI
		self.temperature_label.setText(f"{temp_celsius:.1f}°C")
		self.description_label.setText(weather_desc)
		self.emoji_label.setText(emoji)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	weather_app = WeatherApp()
	weather_app.show()
	sys.exit(app.exec_())

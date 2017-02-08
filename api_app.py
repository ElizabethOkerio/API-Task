import requests
import json
# The purpose of the application is to help a user get the
# list of the holdays in a country in a particular year
# def get_holidays():
# Enter the name of the country. The name should
# follow the (ISO 3166-2 format) like Argentina is AR,
country = input('Enter country(ISO 3166-2 format): ')
# Enter the year for which you want the holidays be displayed
year = input('Enter Year: ')
api_key = '370b4375-19ea-4f7e-9159-b080786fe326'

get_holidays_request = requests.get('https://holidayapi.com/v1/holidays?key='+api_key+'&country='+country+'&year='+year)

if(get_holidays_request.status_code==200):

	holidays_info = get_holidays_request.json()

	result = json.dumps(holidays_info)

	result1 = json.loads(result)

	print(result1)

else:
	print("not acceptable country")


	

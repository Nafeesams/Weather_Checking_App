import json
import requests
import win32com.client as wincom
city = input("enter city\n")
url = f"http://api.weatherapi.com/v1/current.json?key=ad63e4cdb1a84556bf551124232106&q={city}"
r = requests.get(url)
print(r.text)
we_dict = json.loads(r.text)
print(we_dict["current"]["temp_c"])

import requests

url = "http://www.kmoni.bosai.go.jp/api/"  
response = requests.get(url)
if response.status_code == 200:
    data = response.json()  # or .xml depending on the format
    print(data)

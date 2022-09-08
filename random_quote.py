import requests

url = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
	"X-RapidAPI-Key": "4d8389b856msh70ace6f646a7918p101b48jsn0dce6744806f",
	"X-RapidAPI-Host": "quotes15.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
x=response.json()
quote=(x['content'])
author=(x['originator']['name'])
print(author,"said that ", quote)

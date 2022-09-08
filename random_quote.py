import requests

url = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
	"X-RapidAPI-Key": "4d8389b856msh70ace6f646a7918p101b48jsn0dce6744806f",
	"X-RapidAPI-Host": "quotes15.p.rapidapi.com"
}
##custom header response
response = requests.request("GET", url, headers=headers)
##load for json
x=response.json()
##finding path to json
quote=(x['content'])
author=(x['originator']['name'])
##print
print(author,"said that ", quote)

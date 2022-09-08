import requests

##api details by rapid api
url = "https://quotes15.p.rapidapi.com/quotes/random/"
headers = {
	"X-RapidAPI-Key": "4d8389b856msh...........3456yhgrt456",
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
print(author,"said that ",quote)
##result
##Malala Yousafzai said that  It is so hard to get things done in this world. You try and too often it doesn't work. But you have to continue. And you never give up. 


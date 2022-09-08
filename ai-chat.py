import requests
while True :
	url = "https://waifu.p.rapidapi.com/path"
	message=input('Enter Msg:')
	querystring = {"user_id":"sample_user_id","message":message,"from_name":"Boy","to_name":"Girl","situation":"girl and boy formal chat","translate_from":"auto","translate_to":"en"}

	payload = {}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "4d8389b856msh70ace6f646a7918p101b48jsn0dce6744806f",
		"X-RapidAPI-Host": "waifu.p.rapidapi.com"
	}

	response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

	print(response.text)

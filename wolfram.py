import wolframalpha as wa
try:
	while True:
		question=input("Enter your Question:")
		app_id='98U7W6-9R4AHKGW2T'
		client= wa.Client(app_id)
		res =client.query(question)
		answer = next(res.results).text
		print(answer)
except:
	print('Something Went Wrong')

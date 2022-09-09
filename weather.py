import requests as r
import sys
try:
	city=sys.argv[1]
	url='https://api.openweathermap.org/data/2.5/weather?q='+(city)+'&appid=e365571f77c64461e8aaba91f772c647&units=metric'
	res=r.request("GET", url)
	x=res.json()
	desc=(x['weather'])
	temp=(x['main']['temp'])
	feels_like=(x['main']['feels_like'])
	print("""\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


                    """)

	print("Temperature:",temp)
	print("Feels Like:",feels_like)
	print("Desc:",desc[0]['description'])
except:
	print("""\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /


Usage: python3 weather.py city_name                    """)

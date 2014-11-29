import requests
import json

url = 'http://services.wine.com/api/beta2/service.svc/json/catalog'
apikey = 'd5845b19633cfd732646e1089e43b3e1'

def getWineInfoBySearch(params, sort='name'):
    params = params.split()
    searchString = ""
    for i in params:
        searchString += i
        searchString += '+'

    searchString = searchString[:-1] #remove the last +

    urlString = url + '?search=' +  searchString
    if(sort):
    	urlString += '&sortBy=' + 'sort'

    urlString += '&apikey=' + apikey

    r = requests.get(urlString)
    return r.json()

def getWineNamesFromSearch(request):
	wines = request['Products']['List']
	names = []
	for w in wines:
		names.append(w['Name'])
	return names

def getNumberOfWinesFromSearch(request):
	return request['Products']['Total']

def getWineImageURLSFromSearch(request):
	wines = request['Products']['List']
	imURLS = []
	for w in wines:
		labels = w['Labels']
		for l in labels:
			imURLS.append(l['Url'])
	return imURLS
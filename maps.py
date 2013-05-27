from urllib import urlopen
from urllib import quote
import json

# import necessary libs for json and/or xml
 
#print quote("Google's homepage!") # encodes data for URL use
#print urlopen('http://www.google.com').read()
 
def quoteStuff(objectsToQuote):
    quotedObjects = dict()
    for key, value in objectsToQuote.items():
        quotedObjects[key] = quote(value)
    return quotedObjects;
 
def main():
    # can use "json" or "xml"
    directionsURL = "http://maps.googleapis.com/maps/api/directions/json?"
 
    # params as per:
    # http://code.google.com/apis/maps/documentation/directions/#RequestParameters
    params = dict()
    params['origin'] = "Santa Rita 1355, La Reina, Santiago, Chile"
    params['destination'] = "Vicuna Mackenna 4860, Macul, Santiago, Chile"
    params['mode'] = "walking" # optional -- defaults to driving
    params['waypoints'] = "" # optional
    params['alternatives'] = "" #optional
    params['avoid'] = "" #optional -- needs to be "tolls" or "highways"
    params['units'] = "" #optional
    params['region'] = "" # optional
    params['language'] = "spanish" #optional
    params['sensor'] = "true" # indicates if request comes from device w/GPS
 
    quotedParams = quoteStuff(params)
   
    for key, value in quotedParams.items():
        directionsURL = directionsURL + key + "=" + value + "&"
 
    # chop off the trailing &
    directionsURL = directionsURL[:-1]
    #print "url is: ", directionsURL
 
    o = urlopen(directionsURL)
    #print ( o.read())
    
    hola = o.read()
    myFile = open('data.json', 'w')
    myFile.write(hola)
    myFile.close()
    json_data=open('data.json')

    data = json.load(json_data)
    x = 0
    while True:
        try:
            lat = str(data["routes"][0]["legs"][0]["steps"][x]["end_location"]["lat"])
            lng = str(data["routes"][0]["legs"][0]["steps"][x]["end_location"]["lng"])
            print("Latitud: " + lat + "| Longitud:" + lng)
            x += 1
        except :
            print "Se terminO"
            json_data.close()
            break;
   
    return 0;
if __name__ == '__main__': main()
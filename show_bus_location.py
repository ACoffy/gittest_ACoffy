import json
import sys
import urllib2
import requests

if __name__=='__main__':
	mta_key = sys.argv[1]
	bus_code = sys.argv[2]
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (mta_key, bus_code)
	#request = urllib2.urlopen(url)
	request = requests.get(url)
	data = request.json()
	#metadata = json.loads(request.read())
    
	loc_bus = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

	print "Busline", bus_code
	bus_count = len(loc_bus)
	print "Number of Active Buses", bus_count

	busNum = 0
	for i in loc_bus:
		busNum +=1 #Makes the first bus print as 1 but is still position 0 for bus_count
		buslong = i["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
		buslat = i["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]

		print "Bus %d is at latitude %.5f and longitude %.5f" % (busNum, buslong, buslat)

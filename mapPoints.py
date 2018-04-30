import csv
from Term_Project.classes import airportAtlas

#loading in data for all airports, please see classes for airport atlas class
t=airportAtlas()
t.loadData("airport.csv")

def mapPoints(route):

    if route[:-1] != "Not feasible":
        latLng=""
        for i in range(len(route) - 1):
            latLng += str(t.getAirport(route[i]).getLat()) +","+ str(t.getAirport(route[i]).getLng()) + ","
        return latLng[:-1].split(",")


with open("bestroutes.csv", encoding="utf-8-sig") as csvfile:
    file = csv.reader(csvfile)
    coords=[['lat1','long1','lat2','long2','lat3','long3','lat4','long4','lat5','long5','lat6','long6']]
    for line in file:
        flights = line
        points=mapPoints(line)
        coords.append(points)


        #Output results to a csv file
with open("latLng.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(coords)


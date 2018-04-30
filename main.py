from math import pi, sin, cos, acos
import csv
from classes import airport, airportAtlas, aircraft, countryCurrency, currencyRate
import math
from itertools import permutations


def createDict(flights):
    """storing distance, rate and cost for all flight combinations in a dictionary
    error handling when exchange rate can't be located.
    Set to one but alert made to user to update as this flight information would not be accurate
    return a dictionary """
    distanceDict = {}
    for code1 in flights[:-1]:
        distanceDict[code1] = {}
        for code2 in flights[:-1]:
            if code1 != code2:
                distance = (t.getDistanceBetweenAirports(code1, code2))
                try:
                    rate = float(currencyRate.getCurrencyRate(
                        currencyRatesDict[countryCurrency.getCCurrency(countryCurrencyDict[t.getCountry(code2)])]))
                except:
                    with open("error_logs", 'a') as logfile:
                        print("error converting to Euro for", t.getCountry(code2), "Setting rate to 1",file=logfile)
                        logfile.close()
                    rate = 1
                cost = distance * rate
                distanceDict[code1][code2] = {'distance': distance, 'rate': rate, 'cost': cost}
    return distanceDict


def getCheapest(flights,distanceDict):
    """Function to update the permutations list of all possible flight routes to have a start and end airport
    Check if the distance between each station is feasible
    If feasible add a cost to the flight and return the cheapest flight price
    if not feasible return not feasible"""

    flightPrice = []

    for f in permutations(flights[1:-1]):
        f = list(f)
        f.append(flights[0])
        f.insert(0, flights[0])
        feasible = True
        for i in range(0, len(f) - 1):
            if distanceDict[f[i]][f[i + 1]]['distance'] > aircraftDict[flights[5]].getRange():
                feasible = False
        if feasible:
            price = (distanceDict[f[0]][f[1]]['cost'] + distanceDict[f[1]][f[2]]['cost'] + distanceDict[f[2]][f[3]][
                'cost'] + distanceDict[f[3]][f[4]]['cost'] + distanceDict[f[4]][f[5]]['cost'])
            f.append(price)
            flightPrice.append(f)
        else:
            f.append("Not feasible")
            flightPrice.append(f)

    currentLowestPrice = flightPrice[0]

    for i in range(len(flightPrice)):
        if isinstance(flightPrice[i][-1], float):
            if currentLowestPrice[-1] == "Not feasible":
                currentLowestPrice = flightPrice[i]
            elif flightPrice[i][-1] < currentLowestPrice[-1]:
                currentLowestPrice = flightPrice[i]
    return (currentLowestPrice)



#Reading in from Aircraft csv and putting information in a dictionery
#Updating the imperial units to metric so all units stored in the dictionary on metric
aircraftDict = {}
with open("aircraft.csv", encoding="utf8") as fileAircraft:
    for line in fileAircraft:
        if "code,type" not in line: # exclude header from csv file
            line=line.split(",")
            if line[2] == "metric":
                c = line[0]
                t = line[1]
                u = line[2]
                m = line[3]
                r = float(line[4])
                aircraftDict[c] = aircraft(c,t,u,m,r)
            elif line[2] == "imperial":
                c = line[0]
                t = line[1]
                u = "metric"
                m = line[3]
                r = (int(line[4])*1.6093)
                aircraftDict[c] = aircraft(c, t, u, m, r)
            else:
                print("Unit not recognised")


#Reading in the country currency csv and storing values in a dictionary
countryCurrencyDict = {}
with open("countrycurrency.csv", encoding="utf8") as csvfile:
    fileCCurrency = csv.reader(csvfile)
    for line in fileCCurrency:
        name = line[0]
        cc = line[14]
        countryCurrencyDict[name] = countryCurrency(name, cc)


#Reading values in from currency rates csv and storing in a dictionary
currencyRatesDict = {}
with open ("currencyrates.csv", encoding="utf8") as fileCurrencyRates:
    for line in fileCurrencyRates:
        line = line.split(",")
        cName = line[0]
        cCode = line[1]
        EuroR = line[2]
        NEuroR = line[3]
        currencyRatesDict[cCode] = currencyRate(cName, cCode, EuroR, NEuroR)

#loading in data for all airports, please see classes for airport atlas class
t=airportAtlas()
t.loadData("airport.csv")



#Read in testroutes csv and store each line in the variable called flights
with open("testroutes.csv", encoding="utf-8-sig") as csvfile:
    file = csv.reader(csvfile)
    for line in file:
        flights = line

        #Call functions
        dictionary = createDict(flights)
        cheapest = getCheapest(flights,dictionary)

        #Output results to a csv file
        with open("bestroutes.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerows([cheapest])


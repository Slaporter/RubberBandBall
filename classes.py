from math import pi, sin, cos, acos
import csv
import collections

class aircraft:
    "A class representing airplanes"

    def __init__(self, c, t, u, m, r):
        self.code = c
        self.type = t
        self.units = u
        self.manu = m
        self.range = r

    def getRange(self):
        return self.range

    def __str__(self):
        return "code is %s, range is %s" %(self.code, self.range)


class airport:
    "A class representing airports"

    def __init__(self, id, ci, country, code, lat, lng, cont):
        self.id = id
        self.city = ci
        self.country = country
        self.code = code
        self.lat = lat
        self.lng = lng
        self.cont = cont

    def getCountry(self):
        return self.country

    def getCode(self):
        return self.code

    def getLat(self):
        return self.lat

    def getLng(self):
        return self.lng

class airportAtlas:
    "A class for multiple airport objects"

    def __init__(self):
        self.airportDict = {}

    def loadData(self, csvFile):
        with open(csvFile, encoding="utf8") as csvfile:
            fileAirport = csv.reader(csvfile)
            for line in fileAirport:
                id = line[0]
                ci = line[1]
                country = line[3]
                code = line[4]
                lat = line[6]
                lng = line[7]
                cont = line[11]
                self.airportDict[code] = airport(id, ci, country, code, lat, lng, cont)

    def getAirport(self, code):
        return self.airportDict[code]

    def getAllCodes(self):
        return self.airportDict.keys()


    #code taken from tutorial notes, calculates distance between two co-ordinates using great circle distance
    @staticmethod
    def greatcircledist(lat1, lng1, lat2, lng2):
        radiusearth = 6371  # km
        theta1 = lng1*(2*pi)/360
        theta2 = lng2 * (2 * pi)/360
        phi1 = (90-lat1)*(2*pi)/360
        phi2 = (90-lat2)*(2*pi)/360
        distance = acos(sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2))* radiusearth
        return distance

    def getDistanceBetweenAirports(self, code1, code2):
        return self.greatcircledist(float(self.airportDict[code1].getLat()), float(self.airportDict[code1].getLng()), float(self.airportDict[code2].getLat()), float(self.airportDict[code2].getLng()))

    def getCountry(self,code):
        return self.airportDict[code].getCountry()

class countryCurrency:
    "A class representing country currencies"

    def __init__ (self, name, cc):
        self.name = name
        self.CCurrency = cc

    def getName(self):
        return self.name

    def getCCurrency(self):
        return self.CCurrency


class currencyRate:
    "A class for currency rates"

    def __init__ (self, cName, cCode, EuroR, NEuroR):
        self.currencyName = cName
        self.currencyCode = cCode
        self.toEuroRate = EuroR
        self.fromEuroRate = NEuroR

    def getCurrencyCode(self):
        return self.currencyName

    def getCurrencyRate(self):
        return self.toEuroRate

    def getCurrencyName(self):
        return self.currencyName

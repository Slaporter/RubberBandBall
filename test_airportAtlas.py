from unittest import TestCase
from Term_Project.classes import airportAtlas

class TestAirportAtlas(TestCase):
    def test_getDistanceBetweenAirports(self):
        myatlas = airportAtlas()
        myatlas.loadData('airport.csv')
        answer = 5103.02675898737
        assert myatlas.getDistanceBetweenAirports('DUB', 'JFK') == answer


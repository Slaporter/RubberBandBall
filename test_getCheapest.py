from unittest import TestCase
from Term_Project.main import getCheapest
from Term_Project.main import createDict


class TestGetCheapest(TestCase):
    def test_getCheapest(self):
        answer=['LOV', 'BHI', 'BBO', 'VCS', 'VKO', 'LOV', 1658.6244275911931]
        assert getCheapest(['LOV','BBO','BHI','VKO','VCS','747'],(createDict(['LOV','BBO','BHI','VKO','VCS','747'])))== answer

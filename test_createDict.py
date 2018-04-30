from unittest import TestCase
from Term_Project.main import createDict

class TestCreateDict(TestCase):
    def test_createDict(self):
        answer = {'LOV':
                      {'BBO': {'distance': 14503.905310109256, 'rate': 0.001394, 'cost': 20.218444002292305},
                       'BHI': {'distance': 8367.801923501298, 'rate': 0.1081, 'cost': 904.5593879304903},
                       'VKO': {'distance': 10036.878445019349, 'rate': 0.01524, 'cost': 152.96202750209488},
                       'VCS': {'distance': 15022.446358159088, 'rate': 4.48e-05, 'cost': 0.6730055968455271}},
                  'BBO': {'LOV': {'distance': 14503.905310109256, 'rate': 0.06138, 'cost': 890.2497079345061},
                          'BHI': {'distance': 12208.159141572942, 'rate': 0.1081, 'cost': 1319.702003204035},
                          'VKO': {'distance': 5070.878431969962, 'rate': 0.01524, 'cost': 77.28018730322222},
                          'VCS': {'distance': 6756.599998651961, 'rate': 4.48e-05, 'cost': 0.30269567993960783}},
                  'BHI': {'LOV': {'distance': 8367.801923501298, 'rate': 0.06138, 'cost': 513.6156820645097},
                          'BBO': {'distance': 12208.159141572942, 'rate': 0.001394, 'cost': 17.01817384335268},
                          'VKO': {'distance': 14015.103312574809, 'rate': 0.01524, 'cost': 213.59017448364008},
                          'VCS': {'distance': 16497.40871165063, 'rate': 4.48e-05, 'cost': 0.7390839102819482}},
                  'VKO': {'LOV': {'distance': 10036.878445019349, 'rate': 0.06138, 'cost': 616.0635989552876},
                          'BBO': {'distance': 5070.878431969962, 'rate': 0.001394, 'cost': 7.0688045341661265},
                          'BHI': {'distance': 14015.103312574809, 'rate': 0.1081, 'cost': 1515.0326680893368},
                          'VCS': {'distance': 7918.672649745605, 'rate': 4.48e-05, 'cost': 0.3547565347086031}},
                  'VCS': {'LOV': {'distance': 15022.446358159088, 'rate': 0.06138, 'cost': 922.0777574638048},
                          'BBO': {'distance': 6756.599998651961, 'rate': 0.001394, 'cost': 9.418700398120833},
                          'BHI': {'distance': 16497.40871165063, 'rate': 0.1081, 'cost': 1783.3698817294332},
                          'VKO': {'distance': 7918.672649745605, 'rate': 0.01524, 'cost': 120.68057118212302}}}

        assert createDict(['LOV','BBO','BHI','VKO','VCS','747'])==answer
import sys 
sys.path.append("delivery_network")

from optimal_profit import opti
import unittest


class test_optimal(unittest.TestCase):
    def test_route1(self):
        Trucks = opti(1, 0, Budget = 1000000)  # test of the opti function with file routes.1.in and trucks.0.in        
        self.assertEqual(Trucks, (9997, [(6000000, 900000, 9997)]))

    def test_route1_bis(self):
        Trucks = opti(1, 0, Budget = 200000000)  # test of the opti function with file routes.1.in and trucks.0.in        
        self.assertEqual(Trucks, (19994, [(6000000, 900000, 9997), (2000000, 200000, 9997)]))

    def test_route2(self):
        Trucks = opti(2, 0, Budget = 200000)  # test of the opti function with file routes.2.in and trucks.0.in        
        self.assertEqual(Trucks, (20000, [(6000000, 900000, 10000), (2000000, 200000, 10000)]))
if __name__ == '__main__':
    unittest.main()


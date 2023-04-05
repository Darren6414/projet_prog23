import sys 
sys.path.append("delivery_network")

from optimal_profit import opti
import unittest


class test_optimal(unittest.TestCase):
    def test_route1():
        Trucks = opti(1, 0, Budget = 2000000000000000)  # test of the opti function with file routes.1.in and trucks.0.in        
        self.assertIn(Trucks, [    ])
    
    def test_route3():
        Trucks = trucks_selection(3, 1, Budget = 2000000000000000)  # test of the opti function with file routes.3.in and trucks.1.in
        Trucks_expected= 
        self.assertEqual(Trucks, Trucks_expected)

    def test_route7():
        Trucks = trucks_selection(7, 2, Budget = 2000000000000000)  # test of the opti function with file routes.7.in and trucks.2.in
        Trucks_expected= 
        self.assertEqual(Trucks, Trucks_expected)
   
if __name__ == '__main__':
    unittest.main()
import sys 
sys.path.append("delivery_network")

from approx_profit import trucks_selection
import unittest


class test_approx(unittest.TestCase):
    def test_route1():
        Trucks = trucks_selection(1, 0, Budget = 2000000000000000)  # test of the trucks_selection function with file routes.1.in and trucks.0.in        
        self.assertIn(Trucks, [ ])
    
    def test_route3():
        Trucks = trucks_selection(3, 1, Budget = 2000000000000000)  # test of the trucks_selection function with file routes.3.in and trucks.1.in
        Trucks_expected= 
        self.assertEqual(Trucks, Trucks_expected)

    def test_route7():
        Trucks = trucks_selection(7, 2, Budget = 2000000000000000)  # test of the trucks_selection function with file routes.7.in and trucks.2.in
        Trucks_expected= 
        self.assertEqual(Trucks, Trucks_expected)
   
if __name__ == '__main__':
    unittest.main()
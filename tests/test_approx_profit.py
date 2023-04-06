import sys 
sys.path.append("delivery_network")

from approx_profit import trucks_selection
import unittest


class test_approx(unittest.TestCase):
    def test_route1(self):
        Trucks = trucks_selection(1, 0, Budget = 2000000)  # test of the trucks_selection function with file routes.1.in and trucks.0.in        
        self.assertIn(Trucks, [[(2000000, 200000), (2000000, 200000), (2000000, 200000), (2000000, 200000), 
                               (2000000, 200000), (2000000, 200000), (2000000, 200000), (2000000, 200000), 
                               (2000000, 200000), (2000000, 200000)], [(2000000, 200000), (2000000, 500000)]])
    
    def test_route3(self):
        Trucks = trucks_selection(3, 1, Budget = 20000000)  # test of the trucks_selection function with file routes.3.in and trucks.1.in
        Trucks_expected= [(6500000, 910000), (6500000, 910000), (4000000, 560000), (6500000, 910000), (6500000, 910000), (4000000, 560000), (4000000, 560000), (5000000, 580000), 
                          (4500000, 570000), (4000000, 560000), (7000000, 980000), (7000000, 980000), (3500000, 430000), (7000000, 980000), (4000000, 560000), (6500000, 910000), 
                          (5000000, 580000), (4500000, 570000), (3000000, 360000), (5000000, 580000), (5500000, 740000), (9000000, 1450000), (3000000, 360000), (4000000, 560000), 
                          (3000000, 360000), (9500000, 1500000)]
        self.assertEqual(Trucks, Trucks_expected)

    def test_route7(self):
        Trucks = trucks_selection(7, 2, Budget = 2000000)  # test of the trucks_selection function with file routes.7.in and trucks.2.in
        Trucks_expected= [(7797000, 389874), (8556000, 431175), (6650000, 335699), (7411000, 370983), (5297000, 267605)]
        self.assertEqual(Trucks, Trucks_expected)
   
if __name__ == '__main__':
    unittest.main()
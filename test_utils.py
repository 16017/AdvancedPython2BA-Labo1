# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(n):
        try :
            while n>0:
                fact = 1
                fact*=n
                n-=1
        except :
            pass
        finally :
            return fact
        pass
    
    def test_roots(a, b, c):
        delta = b^2-4*a*c
        if delta < 0:
            roots=('/')
        if delta >= 0:
            roots=((-b+sqrt(delta))/2*a,(-b-sqrt(delta))/2*a)
        return roots
            
        pass
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())

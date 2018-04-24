#!/usr/bin/env python

import unittest
import confidenceInterval

class TestInterval(unittest.TestCase):
    def test_confInt(self):
        result=confidenceInterval.confInt(25,150,.95)
        expResult=(0.10705, 0.22635)
        self.assertEqual(expResult,result)
    
    
if __name__=='__main__':
    unittest.main()
    
import unittest
import dateConvert

class TestDateStuff(unittest.TestCase):
    def test_dateC(self):
        result=dateConvert.dateC("13 Apr. 1927")
        expResult=13,4,1927
        self.assertEqual(expResult, result)
    def test_is20(self):
        #test case for a specific date, when the person was over 20
        resultOverNotC=dateConvert.is20("29 July 1861","24 Mar. 1930")
        expResultOverNotC=False, False
        self.assertEqual(expResultOverNotC, resultOverNotC)
        #test case for a specific date, when the person was under 20
        resultUnderNotC=dateConvert.is20("30 Aug. 1917","16 May 1930")
        expResultUnderNotC=True, False
        self.assertEqual(expResultUnderNotC, resultUnderNotC)
        #test case for an approximate birthdate, over 20, not close enough
        #to be ambiguous
        resultOverCNotA=dateConvert.is20("c.1866","24 Dec. 1925")
        expResultOverCNotA=False, False
        self.assertEqual(expResultOverCNotA, resultOverCNotA)
        #test case for an approximate birthdate, over 20, is close enough
        #to be ambiguous
        resultOverCA=dateConvert.is20("c.1901","24 Dec. 1925")
        expResultOverCA=False, True
        self.assertEqual(expResultOverCA, resultOverCA)
        #test case for an approximate birthdate, under 20, not ambiguous
        resultUnderCNotA=dateConvert.is20("c.1920","24 Jan. 1925")
        expResultUnderCNotA=True, False
        self.assertEqual(expResultUnderCNotA, resultUnderCNotA)
        #test case for an approximate birthdate, under 20, close enough to
        #be ambiguous.
        resultUnderCA=dateConvert.is20("c.1907","23 Aug. 1925")
        expResultUnderCA=True, True
        self.assertEqual(expResultUnderCA, resultUnderCA)


if __name__=='__main__':
    unittest.main()
    

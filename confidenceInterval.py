#!/usr/bin/env python
import scipy.stats as st
import math

def confInt(success,number,sigLevel):
    s=sigLevel
    x=float(success)
    print("x=" + str(x))
    n=float(number)
    print("n=" +str(n))
    pHat=x/n
    print pHat
    zStar=st.norm.ppf(1-(1-s)/2)
    print zStar
    thing1=pHat*(1-pHat)
    print thing1
    thing2=thing1/n
    thing=math.sqrt(thing2)
    print thing
    margError=zStar*thing
    print margError
    lower=pHat-margError
    upper=pHat+margError
    return(lower,upper)

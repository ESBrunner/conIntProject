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
    print ("p-hat=" + str(pHat))
    zStar=st.norm.ppf(1-(1-s)/2)
    thing1=pHat*(1-pHat)
    thing2=thing1/n
    thing=math.sqrt(thing2)
    margError=zStar*thing
    lower=pHat-margError
    upper=pHat+margError
    return(lower,upper)

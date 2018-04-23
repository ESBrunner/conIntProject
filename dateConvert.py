import re

def dateConvert(date):
        monthDict={"Jan.":1, "Feb.":2, "Mar.": 3, "Apr.":4, "May":5, "June":6, "July":7,
               "Aug.":8, "Sept.":9, "Oct.":10, "Nov.":11, "Dec.":12}
        thing=date.split()
        day=int(thing[0])
        month=monthDict[thing[1]]
        year=int(thing[2])
        return(day, month, year)
    

def is20(birthDate, deathDate):
    birthMonth=0
    birthDay=0
    birthYear=0
    deathMonth=0
    deathDay=0
    deathYear=0
    hasC=False
    isApprox=False
    lessThan20=False

    deathDay, deathMonth, deathYear=dateConvert(deathDate)
    if re.match(r"c.", birthDate)is not None:
        birthMonth=1
        birthDay=1
        year=re.search(r"[0-9]{4}",birthDate)
        birthYear=int(year.group(0))
        hasC=True
    else:
        birthDay, birthMonth, birthYear=dateConvert(birthDate)
    yearDiff=deathYear-birthYear
    if yearDiff>20:
        if hasC==False:
            lessThan20=False
            isApprox=False
        elif hasC==True:
            if yearDiff<30:
                lessThan20=False
                isApprox=True
    elif yearDiff<20:
        if hasC==False:
            lessThan20=True
            isApprox=False
        elif hasC==True:
            if yearDiff>15:
                lessThan20=True
                isApprox=True
    elif yearDiff==20:
        if deathMonth>birthMonth:
            lessThan20=True
        elif deathMonth<birthMonth:
            lessThan20=False
        elif deathMonth==birthMonth:
            if deathDay<birthDay:
                lessThan20=False
            elif deathDay>=birthDay:
                lessThan20=True
        if hasC==True:
            isApprox=True
    return (lessThan20, isApprox)
    
    

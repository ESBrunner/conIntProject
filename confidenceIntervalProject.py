#!/usr/bin/env python

from random import randint
import csv
import confidenceInterval
import dateConvert



#helper function to make set of random numbers
#create an empty set and populate it with random numbers.
#x is the number of numbers I want in the set. 
def randNums(x):
    randSet=set()
    while len(randSet)<500: 
        randSet.add(randint(1,x))
    return randSet

#I'm redoing my stats project in python. Here's what I need to do
def statsProject(sigLevel):
    sig=sigLevel
#establish some variables.
    lineCount=0
    under20Count=0
    n=500
    #Some of my birthdates are approximate. I need to keep track of how many of these are close enough to
    #20 years before the death date to complicate my analysis. 
    possibleProblemCount=0
#make a set of random numbers between 1 and 17049, which is the number of names in the database. 
    randSet=randNums(17049)
#read in dataset. I converted it to an excel file, and I can convert that to csd.
#what I need to do here: extract birthdate. Deal with birthdates in the format c. 1865. (I think I can
# just convert them to 01/01/1865.) Extract death date.
    with open('data.csv') as csvfile:
        reader=csv.DictReader(csvfile, fieldnames= ('name', 'birthdate', 'birthplace','deathdate'))
        #for each line in the dataset, if the lineCount corresponds to a number in randSet, I'm going to
        #run deathAge() to get the age at death. If the difference in years is
        #less than 20, add 1 to under20Count. Regardless, add one to lineCount.
        for row in reader:
            if lineCount in randSet:
                print(row['name'], row['birthdate'], row['deathdate'])
                #I'm getting a few errors because of improperly-formatted data.
                #For now, I'm going to throw an exception that excludes them from teh results.
    
                try:
                    results=dateConvert.is20(row['birthdate'],row['deathdate'])
                    if results[0]==True:
                        under20Count+=1
                    if results[1]==True:
                        possibleProblemCount+=1
                        print('Problem!')
                except (ValueError, KeyError, IndexError):
                    n-=1
            lineCount+=1
    conf=confidenceInterval.confInt(under20Count, n,sig)
    print(under20Count)
    percent=str(int(sig*100))
    return("The " + percent +"% confidence interval is (" + str(conf[0])+"," + str(conf[1]) + "), and the number of possible problem results is " + str(possibleProblemCount) +'.')




#!/usr/bin/env python

from random import randint
import csv

#helper function to get age at death by subtracting birth date from death date. 
def deathAge():
    pass

#helper function to make set of random numbers
#create an empty set and populate it with random numbers.
#x is the number of numbers I want in the set. 
def randNums(x):
    randSet={}
    while len(randSet)<500: 
        randSet.add(randint(1,x))
    return randSet

#I'm redoing my stats project in python. Here's what I need to do
def statsProject():
#establish some variables.
    lineCount=0
    under20Count=0
    #Some of my birthdates are approximate. I need to keep track of how many of these are close enough to
    #20 years before the death date to complicate my analysis. 
    possibleProblemCount=0
#make a set of random numbers between 1 and 17049, which is the number of names in the database. 
    randSet=randNums(17050)
#read in dataset. I converted it to an excel file, and I can convert that to csd.
#what I need to do here: extract birthdate. Deal with birthdates in the format c. 1865. (I think I can
# just convert them to 01/01/1865.) Extract death date. 

#for each line in the dataset, if the lineCount corresponds to a number in randSet, I'm going to
#run deathAge() to get the age at death. If the difference in years is
#less than 20, add 1 to under20Count. Regardless, add one to lineCount.

#while lineCount<17050:
#   if lineCount in randSet:
#       age=deathAge()
#       if age<20:
#           under20Count+=1
#   lineCount+=1


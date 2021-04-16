# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 02:12:50 2021

@author: jkcho
"""

import os
import math

def reading(filename): #importowanie danych z pliku
    
    os.chdir("E:/Pobrane/")
    table=[]
    with open(filename,"r", encoding="utf-8" ) as file:
        for row in file:
            querry = row.rstrip()
            querry = querry.split(",")
            table.append(querry)
    return table

def possiblevalues(filename):
    possiblevalues = {}
    table=reading(filename)
    table = list(zip(*table))
    i=0
    for attr in table:
        possiblevalues["a"+str(i+1)] = list(set(attr))
        possiblevalues["a"+str(i+1)].insert(0,len(possiblevalues["a"+str(i+1)]))
        i+=1
    possiblevalues["d"]=possiblevalues["a"+str(i)]
    del possiblevalues["a"+str(i)]
    return possiblevalues

def countedvalues(filename):
    countedvalues={}
    possiblevaslues = possiblevalues(filename)
    table = reading(filename)
    table = list(zip(*table))
    
    i = 0
    for attr, values in possiblevaslues.items():
        temp={}
        for value in values[1:]:
            temp[value]=table[i].count(value)
        i+=1
        countedvalues[attr]=temp
        
    return countedvalues

def probability(filename):
    problist=[]
    counted=countedvalues(filename)['d']
    sumd=sum(counted.values())
    for x in counted.values():
        problist.append(x/sumd)
    return problist


    
def entropy(filename):
    sump=0
    probtable=probability(filename)
    for x in probtable:
        sump+=(x*math.log2(x))
        
    return -sump

    
    

          

print(probability("test.txt"))
print(countedvalues("test.txt"))
print(possiblevalues("test.txt"))
print(entropy("test.txt"))
    
        


# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 02:12:50 2021

@author: jkcho
"""

import os

def reading(filename): #importowanie danych z pliku
    
    os.chdir("E:/Pobrane/testGielda")
    table=[]
    with open(filename,"r", encoding="utf-8" ) as file:
        for row in file:
            querry = row.rstrip()
            querry = querry.split(",")
            table.append(querry)
    return table

def possiblevalues(table=[]):
    possiblevalues = {}
    table = list(zip(*table))
    i=0
    for attr in table:
        possiblevalues["a"+str(i+1)] = list(set(attr))
        possiblevalues["a"+str(i+1)].insert(0,len(possiblevalues["a"+str(i+1)]))
        i+=1
    return possiblevalues

def countedvalues(table=[]):
    countedvalues={}
    possiblevaslues = possiblevalues(table)
    table = list(zip(*table))
    
    i = 0
    for attr, values in possiblevaslues.items():
        temp={}
        for value in values[1:]:
            temp[value]=table[i].count(value)
        i+=1
        countedvalues[attr]=temp
        
    return countedvalues

    
    
    
print(countedvalues(reading("gielda.txt")))
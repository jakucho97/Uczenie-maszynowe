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
    

def countingattr(table): #liczenie możliwej wartosci każdego atrybutu
    attributes={}
    i=0
    while i<len(table[0]): 
        temp=[]
        for row in table:
            for attribute in row[i:len(row):len(row)]:
                temp.append(attribute)
            temp=list(set(temp))
        temp.insert(0,len(temp))
        attributes["a"+str(i+1)]=temp      
        i+=1
    return attributes

print(countingattr(reading("gielda.txt")))
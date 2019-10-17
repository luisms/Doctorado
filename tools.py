import os, sys, paperInfo
import numpy as np
# -*- coding: utf-8 -*-
#load data from file, return list of lines

UECountries ={"Spain","Austria","Greece","Germany","Netherlands","Ireland",
"France","Italy","UK","Finland","Romania","Hungary","Denmark","Sweden","Portugal"}


def readFile(name):
    f = open(name,'r')
    data = f.readlines()
    return data

#split lines of data in to information

def spliter(data):
    splited = data.split("\t")
    return splited

def sortDictionary(dictionary):
    sortedDict = {}
    sortedList = sorted(dictionary)
    for value in sortedList:
        sortedDict[value] = dictionary[value]
    return (sortedDict)


def sortAndFillDictionary(dictionary):
    sortedDict = {}
    sortedList = np.arange(2000,2019)
    for value in sortedList:
        if(str(value) in dictionary):
            sortedDict[str(value)] = dictionary[str(value)]
        else:
            sortedDict[str(value)] = 0
    return (sortedDict)


def filtered(dictionary,filter):
    filteredDict = {"others": 0}
    valueList = dictionary.keys()
    for value in valueList:
        if((dictionary[value]<=filter)):
            filteredDict["others"] = filteredDict["others"] + dictionary[value]
        else:
            filteredDict[value] = dictionary[value] 
    
    return filteredDict

def filteredYear(dictionary,filter):
    filteredDict = {}
    valueList = dictionary.keys()
    for value in valueList:
        if((int(value)>filter)):
            filteredDict[value] = dictionary[value] 
    return filteredDict


def filteredUE(dictionary,filter):
    filteredDict = {"others": 0,"EU":0}
    
    valueList = dictionary.keys()
    for value in valueList:
        if((value in UECountries)):
            filteredDict["EU"] =filteredDict["EU"] + dictionary[value] 
        elif((dictionary[value]<=filter)):
            filteredDict["others"] = filteredDict["others"] + dictionary[value]
        else:
            filteredDict[value] = dictionary[value]
    return filteredDict        


#split hole file into lines, list ->list[list]
def toPaperData(data):
    dataList = []
    for line in data: 
        line.replace('\t',"")
        dataList.append(spliter(line))
    return dataList
"""
#get data and put in to paper class
def loadDataToPaper(dataToFill):
    papers = []
    for i in dataToFill[1:]:
        papers.append(paperInfo.paper(i))
    return papers
"""
#get data and put in to paper class

def loadDataToPaper(dataToFill):
    papers = []
    for i in dataToFill[1:]:
        paperRaw = paperInfo.paper(i)
        if(paperRaw.issn!="X" and int(paperRaw.year)>=2000):
            papers.append(paperRaw)
    return papers


#from raw data get a list of papers
def importPapers(file):
    papers = []
    dataRaw = readFile(file)
    dataReady = toPaperData(dataRaw)
    papers = loadDataToPaper(dataReady)
    print("+importPapers+ total number of papers found:",len(papers))
    return papers

def countries(paperInfo):
    countryAcu = 0
    countriesDict ={}
    for paper in paperInfo:
       for country in paper.country:
           countryAcu =countryAcu+1 
           if country in countriesDict:
               aux = countriesDict[country]
               countriesDict[country] = aux +1     
           else:
               countriesDict[country] = 1
    print("+countries+ total countries found:",countryAcu, "Diferent countries",len(countriesDict.keys()),print(countriesDict.keys()))
    return countriesDict

def aplicationFields (paperInfo):
    aplicationDict ={} 
    for paper in paperInfo:
        if paper.aplicationField in aplicationDict:
            aux = aplicationDict[paper.aplicationField]
            aplicationDict[paper.aplicationField] = aux +1     
        else:
            aplicationDict[paper.aplicationField] = 1
    return aplicationDict


def specialization(paperInfo):
    specializationDict ={} 
    for paper in paperInfo:
        if paper.specialization in specializationDict:
            aux = specializationDict[paper.specialization]
            specializationDict[paper.specialization] = aux +1     
        else:
            specializationDict[paper.specialization] = 1
    return specializationDict

def publicationYear(paperInfo):
    yearDict={}
    for paper in paperInfo:              
        if paper.year in yearDict:
            aux = yearDict[paper.year]
            yearDict[paper.year] = aux +1     
        else:
            yearDict[paper.year] = 1
    return yearDict


def publicationYearEU(paperInfo):
    yearDict={}
    for paper in paperInfo:              
        
            if paper.year in yearDict:
                aux = yearDict[paper.year]
                yearDict[paper.year] = aux +1     
            else:
                yearDict[paper.year] = 1
    return yearDict    




def findField(dictionary,value):
    print(value)
    for values in dictionary:
        if(values.aplicationField == value):
            print (values.name)

def getPapersByEU(dictionary):
    papersByEU = []
    for values in dictionary:
        for country in values.country:
            if country in UECountries:
               papersByEU.append(values)
    return papersByEU

def getPapersByField(lista, valueToFind):
    paperByFields = []
    for value in lista:
        if(valueToFind ==value.aplicationField):
            paperByFields.append(value)
    return (paperByFields)


def getPapersByUSA(dictionary):
    EUCountries ={"USA"}
    papersByEU = []
    for values in dictionary:
        for country in values.country:
            if country in EUCountries:
               papersByEU.append(values)
    return papersByEU

def getPapersByCountry(dictionary,countryToFind):
    papersBy = []
    for values in dictionary:
        for country in values.country:
            if country == countryToFind:
                #print(values.name)
                papersBy.append(values)
    return papersBy


def filterByTechnology(paperList, technologtToFiltered):
    papersFiltered = []
    for paper in paperList:
        #print(paper.technology,technologtToFiltered,paper.technology.find(technologtToFiltered))

        if(paper.technology.find(technologtToFiltered)>=0):
            papersFiltered.append(paper)
        #else:
            #print(paper.technology,technologtToFiltered,paper.technology.find(technologtToFiltered))
    return papersFiltered
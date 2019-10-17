import paperInfo, tools

#split hole file into lines, list ->list[list]
def toPaperData(data):
    dataList = []
    for line in data: 
        line.replace('\t',"")
        dataList.append(tools.spliter(line))
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
    dataRaw = tools.readFile(file)
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
    UECountries ={"Spain","Austria","Greece","Germany","Netherlands","Ireland"
    "France","Italy","UK","Finland","Romania","Hungary","Denmark","Sweden","Portugal"}
    yearDict={}
    for paper in paperInfo:              
        
            if paper.year in yearDict:
                aux = yearDict[paper.year]
                yearDict[paper.year] = aux +1     
            else:
                yearDict[paper.year] = 1
    return yearDict    


def sortDictionary(dictionary):
    sortedDict = {}
    sortedList = sorted(dictionary)
    for value in sortedList:
        sortedDict[value] = dictionary[value]
    print (sortedDict)

def findField(dictionary,value):
    print(value)
    for values in dictionary:
        if(values.aplicationField == value):
            print (values.name)

def getPapersByEU(dictionary):
    UECountries ={"Spain","Austria","Greece","Germany","Netherlands","Ireland"
    "France","Italy","UK","Finland","Romania","Hungary","Denmark","Sweden","Portugal"}
    papersByEU = []
    for values in dictionary:
        for country in values.country:
            if country in EUCountries:
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
                print(values.name)
                papersBy.append(values)
    return papersBy





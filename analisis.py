import tools
import paperInfo
import plots
import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-

def allCountries(papers):
   countries = tools.countries(papers) 
   filteredCountries  = tools.filteredUE(countries,6)
   print(filteredCountries)
   plots.pieChart(filteredCountries,"Publications by countries")
   

def allFields(papers):
   fields = tools.aplicationFields(papers)
   filteredFields = tools.filtered(fields,5)
   plots.pieChart(filteredFields,"General study fields")

def EUFields(papers):
   papersByEU = tools.getPapersByEU(papers)
   print("analized papers from UE: ",len(papersByEU))
   EUFields = tools.aplicationFields(papersByEU)
   EUfilteredFields = tools.filtered(EUFields,5)
   plots.pieChart(EUfilteredFields,"EU Study fields")

def USAFields(papers):
   papersByUSA = tools.getPapersByUSA(papers)
   print("analized papers from USA: ",len(papersByUSA))
   USAFields = tools.aplicationFields(papersByUSA)
   USAfilteredFields = tools.filtered(USAFields,5)
   plots.pieChart(USAfilteredFields,"USA Study fields ")

def allDataYear(papers):
   year = tools.publicationYear(papers)
   sortedYear = tools.sortAndFillDictionary(year)
   filteredYears = tools.filteredYear(sortedYear,1999)
   return filteredYears
   
def EUdataYear(papers):
  
   paperByEU = tools.getPapersByEU(papers)
   year = tools.publicationYear(paperByEU)
 
   sortedYear = tools.sortAndFillDictionary(year)
   filteredYears = tools.filteredYear(sortedYear,1999)
   return filteredYears

def CountrydataYear(papers,country):

   papersByCountry = tools.getPapersByCountry(papers,country)
   year = tools.publicationYear(papersByCountry)
 
   sortedYear = tools.sortAndFillDictionary(year)
   filteredYears = tools.filteredYear(sortedYear,1999)
   return filteredYears

    
def dataYearCombine(papers):
   
   Alldata = allDataYear(papers)
   EUdata = EUdataYear(papers)
   USAdata = CountrydataYear(papers,"USA")
   print(1,USAdata)
   plots.barChartCom2(Alldata,EUdata,USAdata,"Comparative publications by year")   


def globalMedicalData(papers):
   papersByEU = tools.countries(papers)
   papersByField = tools.getPapersByField(papers,"Healthcare")
   print("medical papers", len(papersByField))
   globalSpecialization = tools.specialization(papersByField)
   globalSpecializationGrouped = tools.filtered(globalSpecialization,6)
   plots.pieChart(globalSpecializationGrouped,"global healthcare specialization")

def EUMedicalData(papers):
   papersByEU = tools.getPapersByEU(papers)
   papersByField = tools.getPapersByField(papersByEU,"Healthcare")
   print("EU medical papers", len(papersByField))
   globalSpecialization = tools.specialization(papersByField)
   globalSpecializationGroped = tools.filtered(globalSpecialization,5)
   plots.pieChart(globalSpecializationGroped,"UE healthcare pecialization")

def USAMedicalData(papers):
   papersByEU = tools.getPapersByUSA(papers)
   papersByField = tools.getPapersByField(papersByEU,"Healthcare")
   print("USA medical papers", len(papersByField))
   globalSpecialization = tools.specialization(papersByField)
   globalSpecializationGroped = tools.filtered(globalSpecialization,1)
   plots.pieChart(globalSpecializationGroped,"USA healthcare specialization")

def medicalCountries(paper):
   papersByField = tools.getPapersByField(paper,"Healthcare")
   print("medical papers", len(papersByField))
   #filteredCountries  = tools.filteredUE(countries,3)
   #plots.pieChart(filteredCountries,"Publications by countries")
   countries = tools.countries(papersByField)
   filteredCountries  = tools.filteredUE(countries,1)
   plots.pieChart(filteredCountries,"Publications by countries") 


def technologyData(paper):
  
   paperVR = tools.filterByTechnology(paper,"VR")
   paperAR = tools.filterByTechnology(paper,"AR")
   paperMR = tools.filterByTechnology(paper,"MR")
   paperBoth = tools.filterByTechnology(paper,",")
   plots.vennDiagram(paperVR,paperAR,paperBoth)



if __name__== "__main__":
   papers = tools.importPapers("data.tsv")
   
   plots.publicationEvolution()

   
   
   #technologyData(papers)
   
   #healthCarePapers= tools.getPapersByField(papers,"Healthcare")
   #technologyData(healthCarePapers)

  # for a in paperDouble:
   #   print(a.name, a.technology)

  

   #allCountries(papers)
   #print("general data")
   #allFields(papers)
   #EUFields(papers)
   #USAFields(papers)
   #dataYearCombine(papers)

   #print("medical data")   
   #globalMedicalData(papers)
   #EUMedicalData(papers)
   #USAMedicalData(papers)
   #medicalCountries(papers)
   

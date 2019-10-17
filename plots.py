import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import numpy as np
import os


def pieChart(dictionary,text):
    labels = dictionary
    sizes = dictionary.values()
    explode = [0.05 for i in range(len(labels)) ]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels,explode=explode, startangle=90,autopct='%1.1f%%',rotatelabels=True, labeldistance=1.1, pctdistance=0.85)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()  
    fig.gca().add_artist(centre_circle)
    
    fig = plt.gcf()
    fig.canvas.set_window_title(text)
    
    plt.show()



def barChart(dictionary,text):
    labels = list(dictionary.keys())
    sizes = list(dictionary.values())
   
    fig, axs = plt.subplots()
    axs.bar(labels, sizes)
    #fig.suptitle(text)

    

    plt.show()

def barChartCom(dictionaryGen ,dictioaryEU,text):
    labelsGen = list(dictionaryGen.keys())
    sizesGen = list(dictionaryGen.values())

    labelsEU = list(dictioaryEU.keys())
    sizesEU = list(dictioaryEU.values())

   
    pGen = plt.bar(labelsGen,sizesGen)
    pEU = plt.bar(labelsEU,sizesEU)

    plt.ylabel("Publications")
    plt.legend((pGen[0], pEU[0]), ('Total', 'EU'))
    
    fig = plt.gcf()
    fig.canvas.set_window_title(text)
    
    plt.show()



def publicationEvolution():
    
    labelsAR = [2300, 2570, 3190, 5540, 4640, 5160, 5820, 6670, 7410, 8070, 10800,13400,16900,19700,24400,27600,30500,35400,31100,21100]
    labelsVR = [14100,15900,17800,19800,23200,24600,29100,29900,34000,36500,38600,40200,42100,45700,45900,46100,50700,57400,47600,27700]
    labelsYear =[str(2000+i) for i in range(20) ]
    
    fig = plt.figure(facecolor='w',figsize=(12,3))
    ax = fig.add_subplot(1,1,1)

    ax.scatter(12,16900,color="blue")
    ax.scatter(16,30500,color="blue")

    ax.scatter(12,42100,color="orange")
    ax.scatter(13,45900,color="orange")
    ax.scatter(16,50700,color="orange")
    

    # Saple data
    
    ax.plot(labelsYear,labelsAR,label="AR")
    ax.plot(labelsYear,labelsVR,label="VR")
    # Annotation with normal padding around the text
    ax.annotate('Google Glass', xy=(12,16900), xytext=(8,16900),
                arrowprops=dict(arrowstyle='->'))


    ax.annotate('Pokémon Go', xy=(16,30500), xytext=(12,30500),
                arrowprops=dict(arrowstyle='->'))
    
    
    ax.annotate('Oculus rift', xy=(12,42100), xytext=(8,42100),
                arrowprops=dict(arrowstyle='->'))


    ax.annotate('facebook', xy=(13,45900), xytext=(10,45900),
                arrowprops=dict(arrowstyle='->'))

    ax.annotate('Oculu rift', xy=(16,50700), xytext=(12,50700),
                arrowprops=dict(arrowstyle='->'))
    # Annotation with decreased padding around the text
    plt.ylabel("Publications")
    plt.xlabel("year")
    plt.legend()
    fig.canvas.set_window_title("Publications evolution ")
    plt.show()



def barChartCom2(dictionaryGen ,dictionaryEU, dictionaryUSA, text):
    labelsGen = list(dictionaryGen.keys())
    labelsEU = list(dictionaryEU.keys())
    labelsUSA = list(dictionaryUSA.keys())

    sizesGen = list(dictionaryGen.values())
    sizesEU = list(dictionaryEU.values())
    sizesUSA = list(dictionaryUSA.values())
    # create plot
    print((labelsGen),(labelsUSA))
    fig, ax = plt.subplots()
    index = np.arange(len(labelsGen))
    bar_width = 0.25
    opacity = 0.8

    
    pGen = plt.bar(index, sizesGen, bar_width,label="General")

    pEU = plt.bar(index+bar_width, sizesEU, bar_width,label="EU")

    pUSA = plt.bar(index+2*bar_width, sizesUSA, bar_width,label="USA")
    
    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')



    autolabel(pGen)
    #autolabel(pEU)
    #autolabel(pUSA)
    
    plt.legend((pGen[0], pEU[0],pUSA[0]), ('Total', 'EU','USA'))
    plt.legend()
    plt.xticks(index + bar_width,labelsGen )
    fig = plt.gcf()
    fig.canvas.set_window_title(text)
    fig.tight_layout()
    plt.show()

def vennDiagram(a,b,c):
    # First way to call the 2 group Venn diagram:
    venn2(subsets = (len(a), len(b), len(c)), set_labels = ('VR', 'AR'))
    plt.ylabel("Technology used")

    fig = plt.gcf()
    fig.canvas.set_window_title("Technology used in general")

    plt.show()
 

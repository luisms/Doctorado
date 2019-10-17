class paper:
    name = ""
    issn = ""
    searchWord = ""
    dataSet = "GoolgeScholar"
    searchConf = ""
    year = ""
    publication = "" 
    country = []   
    typeOfPaper =  0 # 0 paper, 1 app, 2 paper + app, 3 review
    technology = ""
    reviewTech = ""
    comProtocol = ""
    cooperative = ""
    computing = 0 # 0 local , 1 cloud, 2 edge, 3 mixed
    compatibility = ""
    aplicationField = ""
    specialization = ""
    availableSofw = ""
    resume = ""
    utility = ""

    def __init__ (self):
        self.name  = ""
        self.issn = ""
        self.searchWord = ""
        self.dataSet = "GoolgeScholar"
        self.searchConf = ""
        self.year = ""
        self.publication = "" 
        self.country = []   
        self.typeOfPaper =  0 # 0 paper, 1 app, 2 paper + app, 3 review
        self.technology = ""
        self.reviewTech = ""
        self.comProtocol = ""
        self.cooperative = ""
        self.computing = 0 # 0 local , 1 cloud, 2 edge, 3 mixed
        self.compatibility = ""
        self.aplicationField = ""
        self.specialization = ""
        self.availableSofw = ""
        self.resume = ""
        self.utility = "Default constructor"

    def __init__(self, data):
        
        if (len(data) < 18):
            print ( error + data[0])

        else:   
            self.name  = data[0]
            self.issn  =data [1]
            self.searchWord = data[2]
            self.dataSet = data[3]
            self.searchConf = data[4]
            self.year = data[5]
            self.publication = data[6]
            self.country =data[7].replace(" ","").split(',')
            self.typeOfPaper = data[8]# 0 paper, 1 app, 2 paper + app, 3 review
            self.technology = data[9]
            self.reviewTech = data[10]
            self.comProtocol = data[11]
            self.cooperative = data[12]
            self.computing = data[13] # 0 local , 1 cloud, 2 edge, 3 mixed
            self.compatibility = data[14]
            self.aplicationField = data[15]#.replace(" ","").split(',')
            self.specialization = data[16]
            self.availableSofw = data[17]
            self.resume = data[18]
            self.utility = data[19]
            
    def print(self):
        print(self.name,'/',self.searchWord,'/',self.dataSet,'/',self.searchConf,'/',self.year,'/',self.publication,'/',self.country,'/',self.typeOfPaper,'/',self.technology,'/',self.reviewTech,'/',self.comProtocol,'/',
        self.cooperative,'/',self.computing,'/',self.compatibility,'/',self.aplicationField,'/',self.availableSofw,'/',self.resume,'/',self.utility)

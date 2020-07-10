class pet:
    import time
    happy = 0
    fill = 0
    birthtime = 0
    name =''
    latestmiles = 0
    balance = 0
    lastupdated = 0
    def __init__(self,name,originalmiles):
        self.name = name
        self.birthtime = self.time.time()
        self.fill = 5
        self.happy = 3
        self.latestmiles=originalmiles
        self.lastupdated = self.time.time()
    def getStatus(self):
        return [self.name,self.time.time()-self.birthtime,self.happy,self.fill,self.balance]
    def feed(self):
        self.fill +=1
    def timePass(self):
        hrsDiff = (self.time.time()-self.lastupdated)/(60*60)
        self.fill -=.1*hrsDiff
        self.happy -= .1*hrsDiff
        self.lastupdated = self.time.time()
    def buyToy(self):
        self.happy +=.5
    def refresh(self,miles):
        if (miles == self.latestmiles):
            return
        else:
            balance += miles-self.latestmiles
            self.latestmiles = miles
    def editMiles(self, num):
        self.balance+=nums
        return self.balance

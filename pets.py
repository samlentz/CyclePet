class pet:
    import time
    happy = 0
    fill = 0
    birthtime = 0
    name =''
    latestmiles = 0
    balance = 0
    lastupdated = 0
    itemList = ['Food              ','Toy               ','Background Upgrade','Nothing           ',]
    itemCosts = [2,1,20,0]
    background = ['dirt.png','grass.png','floor.jpg','marble.jpg']
    bgLevel = 0
    dead = False
    def __init__(self,name,originalmiles):
        self.name = name
        self.birthtime = self.time.time()
        self.fill = 5
        self.happy = 3
        self.latestmiles=originalmiles
        self.lastupdated = self.time.time()
    def playWith(self):
        self.happy +=.5
        if(self.happy >10):
            self.happy = 10
    def getStatus(self):
        return [self.name,self.time.time()-self.birthtime,self.happy,self.fill,self.balance,self.bgLevel,self.dead]
    def feed(self):
        self.fill +=3
        if self.fill > 10:
            self.fill = 10
    def timePass(self):
        hrsDiff = (self.time.time()-self.lastupdated)/(60*60)
        self.fill -=.1*hrsDiff
        self.happy -= .1*hrsDiff
        self.lastupdated = self.time.time()
        if(self.fill < 0 or self.happy < 0):
            if not self.dead:
                with open('graveyard.txt', 'a') as file:
                    file.write("RIP to " + self.name + '. They died at only ' +str(int((self.time.time()-self.birthtime)/3600)) + ' hours old' + '\n')
            self.dead = True
            print("****Your pet has died. You can view him in the graveyard text file where you launch this game****")
    def buyToy(self):
        self.happy +=1.5
        if(self.happy >10):
            self.happy = 10
    def refresh(self,miles):
        if (miles == self.latestmiles):
            return
        else:
            self.balance += miles-self.latestmiles
            self.latestmiles = miles
    def editMiles(self, num):
        self.balance+=nums
        return self.balance
    def runStore(self):
        self.printStore()
        check =True
        while(check):
            print("What would you like to buy? Enter item number")
            i = int(input())
            if(self.itemCosts[i] <= self.balance):
                self.balance -= self.itemCosts[i]
                if(i==0):
                    self.feed()
                elif(i==1):
                    self.buyToy()
                elif(i==2):
                    print(self.bgLevel,len(self.background))
                    if(self.bgLevel < len(self.background)-1):
                        self.bgLevel +=1
                    else:
                        print('background max level already achieved!')
                        self.balance += self.itemCosts[i]
                elif(i == 3):
                    print('Leaving store')
                elif(i ==4):
                    self.fill = 0
                check = False
                print("Thank you for using the store")
            else:
                print('insufficiant funds')
    def printStore(self):
        print("-------STORE-------")
        for i in range(len(self.itemList)):
            print(str(i) + '. '+self.itemList[i] + '        ' + str(self.itemCosts[i]) +' Coins')
        
             

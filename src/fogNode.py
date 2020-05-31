import random
import constants

class fogNode:
    def __init__(self):
        # initializing the fogNode object. We store values such as reputation and some values used in RBTS
        self.FK = random.randint(10000000000, 20000000000)           # CPU Power in hz
        self.BK = random.randint(37500000000, 375000000000)          # memory enough for every user to associate with this node
        self.WK = constants.BANDWIDTH             # bandwidth in bits/s  
        self.noNo = 0;
        self.noYes = 0;
        #self.m0 = random.random();
        self.m0 = 0.2;
        self.reputation = self.m0;
        #self.ahk = random.random()
        self.ahk = 0.51;
        self.alk = 1.0 - self.ahk;
        
        
    def incNo(self):
        # increase the NO meter
        self.noNo += 1;
        
    def incYes(self):
        #increase the YES meter
        self.noYes += 1;
        
    def calculateReputation(self):
        # calculate this node new reputation given the amount of YES and NO answers
        numerator = self.m0 * pow(self.ahk, self.noYes) * pow(self.alk, self.noNo);
        denominator = numerator + (1 - self.m0) * pow(self.alk, self.noYes) * pow(self.ahk, self.noNo);
        self.reputation = numerator / denominator;
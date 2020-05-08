import constants;
import random;

class fogNode:
    def __init__(self, myahk):
        self.FK = random.randint(10000000000, 25000000000)      # CPU Power in hz
        self.BK = random.randint(16000000000, 32000000000)      # memory in range 2GB - 4GB in bits
        self.WK = random.randint(40000000, 200000000)           # bandwidth in bits/s  
        self.noNo = 0;
        self.noYes = 0;
        self.m0 = random.random();
        self.reputation = self.m0;
        self.ahk = random.random()
        self.alk = 1.0 - self.ahk;
        
        
    def incNo(self):
        self.noNo += 1;
        
    def incYes(self):
        self.noYes += 1;
        
    def calculateReputation(self):
        numerator = self.m0 * pow(self.ahk, self.noNo) * pow(self.alk, self.noYes);
        denominator = numerator + (1 - self.m0) * pow(self.alk, self.noNo) * pow(self.ahk, self.noYes);
        self.reputation = numerator / denominator;
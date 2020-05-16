import random
import numpy as np
import constants

class fogUser:
    def __init__(self, k):
        # the fogUser object is initialized with a random task, represented by a tuple as follows (application bits, application intense parameter, application CPU cycles)
        self.ongoingTask = (0, 0, 0);
        self.probVector = np.ones(k);
        self.noNodes = k;
        self.eu = random.randint(0, 100000000000000)
        self.initTask();
        self.initProbs(k);
        
    def initTask(self):
        #Initializing the tuple of ongoing task
        appBits = random.randint(80000000, 320000000)
        appIP = random.randint(1000000, 20000000)
        appCPUCycles = random.randint(1000000000, 10000000000)
        self.ongoingTask = (appBits, appIP, appCPUCycles);
        
    def initProbs(self, k):
        self.probVector = np.ones(k);
        self.probVector /= k;
        
    def hasDecided(self):
        return any(self.probVector > 0.95);
    
    def giveSelection(self):
        return self.probVector.argmax();
    
    def chooseNode(self):
        temp = random.random();
        i = 0;
        
        while temp > self.probVector[i]:
            temp -= self.probVector[i];
            i += 1;
            
        return i
    
    
    def updateProbs(self, curNode, reward):
        for i in range(self.noNodes):
            if i == curNode:
                self.probVector[i] = self.probVector[i] + constants.beta * reward * (1 - self.probVector[i]);
            else:
                self.probVector[i] = self.probVector[i] - constants.beta * reward * self.probVector[i];
import constants
import compFunctions
import numpy as np
import random

class SLA:
    def __init__(self, nodeList, userList, curNodeList, energyOverheads, timeOverheads, fuk):
        self.nodes = nodeList;
        self.users = userList;
        self.assignment = curNodeList;
        self.eOver = energyOverheads;
        self.tOver = timeOverheads;
        self.fuks = fuk;
        self.uggps = self.computeUGGP();
        self.congs = self.computeCongs();
        self.RFKs = self.computeRFKs();
        
    def computeUGGP(self):
        lista = []
        for i in range(len(self.nodes)):
            nodeSum = 0;
            usersOnNode = compFunctions.indices(self.assignment, i);
            onNode = len(usersOnNode);
            for userIndex in usersOnNode:
                nodeSum += self.tOver[userIndex] / constants.TIMESLOTDURATION;
                nodeSum += self.eOver[userIndex] / self.users[userIndex].eu;
            if onNode == 0:
                lista.append(0);
            else:
                lista.append(nodeSum / onNode);
        
        return np.array(lista);
    
    def computeCongs(self):
        lista = [];
        totalItus = compFunctions.addIUS(self.users);
        for i in range(len(self.nodes)):
            nodeISum = 0;
            usersOnNode = compFunctions.indices(self.assignment, i);
            for userIndex in usersOnNode:
                nodeISum += self.users[userIndex].ongoingTask[0];
            lista.append(nodeISum / totalItus);
            
        return np.array(lista);
    
    def computeRFKs(self):
        lista = []
        for i in range(len(self.nodes)):
            perNode = 0;
            usersOnNode = compFunctions.indices(self.assignment, i);
            onNode = len(usersOnNode);
            for userIndex in usersOnNode:
                perNode += self.fuks[userIndex];
            if onNode == 0:
                lista.append(0);
            else:
                lista.append(perNode / onNode);
        divisor = sum(lista);
        
        array = np.array(lista);
        array /= divisor;
        
        return array;
    
    def computeRewards():
        None
    
    def newRound(self):
        # Needs implementation of actual SLA ITerations
        lista = [];
        for i in range(constants.USERS):
            lista.append(random.randrange(constants.NODES));
        return lista, compFunctions.randomVector(constants.USERS);
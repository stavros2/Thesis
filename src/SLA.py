import compFunctions
import constants
import numpy as np
import random

class SLA:
    def __init__(self, nodeList, userList, curNodeList, energyOverheads, timeOverheads, fuk):
        self.nodes = nodeList;
        self.k = len(nodeList)
        self.users = userList;
        self.u = len(userList)
        self.assignment = curNodeList;
        self.eOver = energyOverheads;
        self.tOver = timeOverheads;
        self.fuks = fuk;
        
    def computeUGGP(self, assignment):
        lista = []
        for i in range(self.k):
            nodeSum = 0;
            usersOnNode = compFunctions.indices(assignment, i);
            onNode = len(usersOnNode);
            for userIndex in usersOnNode:
                nodeSum += self.tOver[userIndex] / constants.TIMESLOTDURATION;
                nodeSum += self.eOver[userIndex] / self.users[userIndex].eu;
            if onNode == 0:
                lista.append(0);
            else:
                lista.append(nodeSum / onNode);
        
        return np.array(lista);
    
    def computeCongs(self, assignment):
        lista = [];
        totalItus = compFunctions.addIUS(self.users);
        for i in range(self.k):
            nodeISum = 0;
            usersOnNode = compFunctions.indices(assignment, i);
            for userIndex in usersOnNode:
                nodeISum += self.users[userIndex].ongoingTask[0];
            lista.append(nodeISum / totalItus);
            
        return np.array(lista);
    
    def computeRFKs(self, assignment):
        lista = []
        for i in range(self.k):
            perNode = 0;
            usersOnNode = compFunctions.indices(assignment, i);
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
    
    def computeRewards(self, assignment):
        UGGP = self.computeUGGP(assignment);
        congs = self.computeCongs(assignment);
        RFKs = self.computeRFKs(assignment);
        lista = [];
        totalRewards = 0;
        for i in range (self.u):
            nodeIndex = assignment[i]
            userReward = self.nodes[nodeIndex].reputation * RFKs[nodeIndex];
            userReward /= UGGP[nodeIndex] * congs[nodeIndex];
            totalRewards += userReward;
            lista.append(userReward);
            
        rewards = np.array(lista);
        normalizedRewards = rewards / totalRewards;
        
        return rewards, normalizedRewards;
        
            
    def iteration(self, assignment, maxReward):
        rewards, normalizedRewards = self.computeRewards(assignment);
        for i in range(self.u):
            self.users[i].updateProbs(assignment[i], normalizedRewards[i]);
            if maxReward[i] < normalizedRewards[i]:
                maxReward[i] = normalizedRewards[i];
        return normalizedRewards;
        
    def newRound2(self):
        checkList = [False] * self.u
        newAssignment = self.assignment;
        maxReward = np.array([0.0000000001] * self.u);
        curRewards = np.array([0] * self.u);
        while not all(checkList):
            curRewards = self.iteration(newAssignment, maxReward);
            newAssignment = [user.chooseNode() for user in self.users]
            checkList = [user.hasDecided() for user in self.users];
        
        newAssignment = [user.giveSelection() for user in self.users]
        probabilities = curRewards / maxReward
        return newAssignment, probabilities;
    
    def newRound(self):
        # Needs implementation of actual SLA ITerations
        lista = [];
        for i in range(self.u):
            lista.append(random.randrange(self.k));
        return lista, compFunctions.randomVector(self.u);
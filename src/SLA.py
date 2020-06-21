import compFunctions
#import plotFunctions
import constants
import numpy as np
import random
#import copy 
import math

class SLA:
    def __init__(self, nodeList, userList, curNodeList, puk, guk, rbts, it = -1):
        # initializing the SLA object with the needed lists. 
        self.nodes = nodeList;
        self.k = len(nodeList)
        self.users = userList;
        self.u = len(userList)
        self.assignment = curNodeList;
        self.puks = puk;
        self.guks = guk;
        self.RBTSScores = rbts;
        self.turn = it;
        
    def computeUGGP(self, assignment, tOver, eOver):
        # computing the UGGP values, according to the formulas
        lista = []
        for i in range(self.k):
            nodeSum = 0;
            usersOnNode = compFunctions.indices(assignment, i);
            onNode = len(usersOnNode);
            for userIndex in usersOnNode:
                nodeSum += tOver[userIndex] / constants.TIMESLOTDURATION;
                nodeSum += eOver[userIndex] / self.users[userIndex].eu;
            if onNode == 0:
                lista.append(0);
            else:
                lista.append(nodeSum / onNode);
        
        return np.array(lista);
    
    def computeCongs(self, assignment):
        # computing the Conegstion (on each node) values, according to the formulas
        lista = [];
        totalItus = compFunctions.addIUS(self.users);
        for i in range(self.k):
            nodeISum = 0;
            usersOnNode = compFunctions.indices(assignment, i);
            for userIndex in usersOnNode:
                nodeISum += self.users[userIndex].ongoingTask[0];
            lista.append(nodeISum / totalItus);
            
        return np.array(lista);
    
    def computeRFKs(self, assignment, fuks):
        # computing the Reputation Factor (used in the reward calculation below)

        lista = []
        for i in range(self.k):
            perNode = 0;
            usersOnNode = compFunctions.indices(assignment, i);
            onNode = len(usersOnNode);
            for userIndex in usersOnNode:
                perNode += fuks[userIndex];
            if onNode == 0:
                lista.append(0);
            else:
                lista.append(perNode / onNode);
                
                
                
                
        divisor = sum(lista);
        
        array = np.array(lista);
        array /= divisor;
        
        return array;
    
    def computeRewards(self, assignment, fuks, userTime, userEnergy):
        # computing the reward each node gives to its paired users
        UGGP = self.computeUGGP(assignment, userTime, userEnergy);
        congs = self.computeCongs(assignment);
        RFKs = self.computeRFKs(assignment, fuks);
        nodeRewards = np.zeros(self.k);
        lista = [];
        totalRewards = 0;
        
        for i in range(self.k):
            if UGGP[i] == 0 or congs[i] == 0:
                nodeRewards[i]  = 0;
            else:
                nodeRewards[i] = self.nodes[i].reputation * RFKs[i] / (UGGP[i] * congs[i]);
        
        for i in range (self.u):
            userReward = nodeRewards[assignment[i]]
            #totalRewards += userReward;
            lista.append(userReward);
            
        rewards = np.array(lista);
      #  totalRewards = sum(nodeRewards);
        #normalizedRewards = rewards / totalRewards;
        #normalizedRewards = [];
        #for i in range(self.u):
         #   normalizedRewards.append(random.random())
        
       # nodeRewards = nodeRewards / totalRewards;
        #normalizedRewards = compFunctions.rewardsRange(rewards, constants.MAXRANGE, constants.MINRANGE)
        normalizedRewards = np.sqrt(np.sqrt(rewards / sum(rewards)));
        totalRewards = sum(normalizedRewards);
        
        return rewards, normalizedRewards, totalRewards;
        
            
    def iteration(self, assignment, maxReward):
        # an iteration of the SLA algorithm. We keep the maxRewards
        ruks = compFunctions.computeRUK(self.nodes, self.puks, self.guks, assignment, self.k, self.u);
        fuks = compFunctions.computeFUK(self.nodes, self.users, assignment, self.k, self.u, self.RBTSScores);

        userTime = compFunctions.computeTimeOverheads(self.users, ruks, fuks);
        userEnergy = compFunctions.computeEnergyOverheads(self.users, constants.USERS, assignment, self.puks, ruks)
        
        rewards, normalizedRewards, totalReward = self.computeRewards(assignment, fuks, userTime, userEnergy);
        #updateData = compFunctions.rewardsRange(normalizedRewards, constants.MAXRANGE, constants.MINRANGE)
        updateData = normalizedRewards;
        
        for i in range(self.u):
            self.users[i].updateProbs(assignment[i], updateData[i]);
            if maxReward[i] < normalizedRewards[i]:
                maxReward[i] = normalizedRewards[i];
        
        return normalizedRewards, totalReward, rewards;
        
    def newRound2(self):
        
        # the actual SLA. Computes the pairings between nodes and users. Also
        # returns a probability for each node (the reward each user got by selecting
        # the last node / the max Reward it received at some point during the SLA).
        # This probability value is used directly as the prediction report for the
        # RBTS
        checkList = [False] * self.u
        newAssignment = self.assignment;
        maxReward = np.array([0.0000000001] * self.u);
        curRewards = np.array([0] * self.u);
        totalRewards = [];
        
        while not all(checkList):
            newAssignment = [user.chooseNode() for user in self.users];
            curRewards, totalReward, rewards = self.iteration(newAssignment, maxReward);
            checkList = [user.hasDecided() for user in self.users];
            totalRewards.append(totalReward);
            
        newAssignment = [user.giveSelection() for user in self.users]
        probabilities = curRewards / maxReward
        totalRewards = np.array(totalRewards);
        totalRewards /= self.u;
        
        
        return newAssignment, probabilities, totalRewards;
    
    def newRound(self):
        # Dummy SLA. Returns 2 random lists, one for pairing nodes and users and one for prediction reports. 
        lista = [];
        for i in range(self.u):
            lista.append(random.randrange(self.k));
        return lista, compFunctions.randomVector(self.u);
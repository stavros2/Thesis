import random
import numpy as np
import compFunctions

class RBTS:
    def __init__(self, nodeList, userList, curNodeList, probs):
        self.nodes = nodeList;
        self.users = userList;
        self.assignement = curNodeList;
        self.predictionReports = probs;
        self.informationReports = self.createReports();
        
    
    def createReports(self):
        lista = [];
        for i in range(len(self.users)):
            temp = random.random();
            if temp > self.predictionReports[i]:
                lista.append(1)
            else:
                lista.append(0);
        
        return lista;
    
    def getPeersRefs(self):
        references = []
        peers = []
        for i in range(len(self.users)):
            nodeIndex = self.assignement[i]
            usersOnNode = compFunctions.indices(self.assignement, nodeIndex);
            onNode = len(usersOnNode);
            userIndex = usersOnNode.index(i);
            references.append(usersOnNode[(userIndex + 1) % onNode]);
            peers.append(usersOnNode[(userIndex + 2) % onNode]);
        
        return references, peers;
    
    def calculateYu(self, refsList):
        lista = []
        for i in range(len(self.users)):
            refNode = refsList[i];
            delta = min(self.predictionReports[refNode], 1 - self.predictionReports[refNode]);
            if self.informationReports[i] == 0:
                lista.append(self.predictionReports[refNode] - delta);
            elif self.informationReports[i] == 1:
                lista.append(self.predictionReports[refNode] + delta);
        
        return np.array(lista);
    
    def scoring(self):
        refs, peers = self.getPeersRefs();
        yu = self.calculateYu(refs);
        lista = []
        for i in range(len(self.users)):
            xk = self.informationReports[peers[i]]
            lista.append(compFunctions.RQ(yu[i], xk) + compFunctions.RQ(self.predictionReports[i], xk))
        
        return np.array(lista);
    
    def finalAnswers(self):
        lista = []
        scores = self.scoring();
        for i in range(len(self.nodes)):
            sumYes, sumNo, noNo, noYes, yesScore, noScore = 0, 0, 0, 0, 0, 0
            usersOnNode = compFunctions.indices(self.assignement, i)
            for user in usersOnNode:
                if self.informationReports[user] == 0:
                    sumNo += scores[user];
                    noNo += 1;
                elif self.informationReports[user] == 1:
                    sumYes += scores[user];
                    noYes += 1;
                if noNo == 0:
                    noScore = 0;
                else:
                    noScore = sumNo / noNo;
                    
                if noYes == 0:
                    yesScore = 0;
                else:
                    yesScore = sumYes / noYes;
                    
            if yesScore > noScore:
                lista.append(1);
            else:
                lista.append(0);
        
        return lista;
class BayesianBelief:
    def __init__(self, nodeList, userAnswers):
        #unitializing the BayesianBelief object with the needed lists.
        self.nodes = nodeList;
        self.answers = userAnswers;
        
        
    def updateYesNoCounter(self):
        # updating the yes and no counters for the nods
        for i in range(len(self.answers)):
            if self.answers[i] == 1:
                self.nodes[i].incYes();
            elif self.answers[i] == 0:
                self.nodes[i].incNo();
        
    def updateReputations(self):
        # updating every node reputation
        self.updateYesNoCounter();
        for node in self.nodes:
            node.calculateReputation();
            
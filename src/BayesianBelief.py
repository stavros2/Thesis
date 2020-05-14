class BayesianBelief:
    def __init__(self, nodeList, userAnswers):
        self.nodes = nodeList;
        self.answers = userAnswers;
        
        
    def updateYesNoCounter(self):
        for i in range(len(self.answers)):
            if self.answers[i] == 1:
                self.nodes[i].incYes();
            elif self.answers[i] == 0:
                self.nodes[i].incNo();
        
    def updateReputations(self):
        self.updateYesNoCounter();
        for node in self.nodes:
            node.calculateReputation();
            
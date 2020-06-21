import compFunctions
import constants
import SLA
import RBTS
import BayesianBelief
import plotFunctions    
import MonteCarloSmoothing
import numpy as np

if __name__ == "__main__":
    distances = compFunctions.generateDistances(10, 400, constants.NODES, constants.USERS);
    nodes, users = compFunctions.initalize(constants.NODES, constants.USERS);
    accRBTSScores = np.zeros(constants.USERS);
    allRounds = [];
    
    puks = compFunctions.computePUK(distances, constants.NODES, constants.THETA1);
    guks = compFunctions.computeGUK(distances, constants.THETA2);
    # plotFunctions.plotNodeCharacteristics(nodes)
    
    print("Initial Reputations");
    for node in nodes:
        print(node.__dict__)
        
    
    #noes, yeses, reps= [[] for i in range(constants.NODES)], [[] for i in range(constants.NODES)], [[] for i in range(constants.NODES)];
    i = 0;
    while i < 1000:
        """for j in range(constants.NODES):
            noes[j].append(nodes[j].noNo);
            yeses[j].append(nodes[j].noYes);
            reps[j].append(nodes[j].reputation);
        """
        
        currentNodes = compFunctions.firstRound(constants.NODES, constants.USERS)
        
        sla = SLA.SLA(nodes, users, currentNodes, puks, guks, accRBTSScores);
        currentNodes, probabilities, avgRewards = sla.newRound2();
        
        #plotFunctions.plotAvgReward(avgRewards)
        allRounds.append(avgRewards)
        
        rbts = RBTS.RBTS(nodes, users, currentNodes, probabilities);
        answers, RBTSScores = rbts.finalAnswers()
        #accRBTSScores += RBTSScores;
            
        """believes = BayesianBelief.BayesianBelief(nodes, answers);
        believes.updateReputations();"""
        
        for user in users:
            user.initProbs(constants.NODES);
        
        i += 1;
        if i%10 ==0:
            print(i)
    smoother = MonteCarloSmoothing.MonteCarloSmoothing();
    allSmoothed = smoother.smooth(allRounds);
    plotFunctions.plotMonteCarlo(allSmoothed, i);
    
    
    
    print("New Reputations")
    for node in nodes:
        print(node.__dict__);
        
        
    """plotFunctions.pltStep2dlist(noes, "Number of No Answers");
    plotFunctions.pltStep2dlist(yeses, "Number of Yes Answers");
    plotFunctions.plotReps(reps);
    plotFunctions.barAvgRep(reps);
    #lotFunctions.plotAggrRewards(rounds); """ 
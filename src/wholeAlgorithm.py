import compFunctions
import constants
import SLA
import RBTS
import BayesianBelief
    
if __name__ == "__main__":
    distances = compFunctions.generateDistances(10, 400, constants.NODES, constants.USERS);
    nodes, users = compFunctions.initalize(constants.NODES, constants.USERS);
    
    print("Initial Reputations");
    for node in nodes:
        print(node.__dict__)
    puks = compFunctions.computePUK(distances, constants.NODES, constants.THETA1);
    guks = compFunctions.computeGUK(distances, constants.THETA2);
    currentNodes = compFunctions.firstRound(constants.NODES, constants.USERS)
    
    ruks, ruksArray = compFunctions.computeRUK(nodes, puks, guks, currentNodes, constants.NODES, constants.USERS);
    fuks = compFunctions.computeFUK(nodes, users, currentNodes, constants.NODES, constants.USERS);
    
   
    i = 0;
    while i < 10:
        userTimeOverheads = compFunctions.computeTimeOverheads(users, ruks, fuks);
        userEnergyOverheads = compFunctions.computeEnergyOverheads(users, constants.USERS, currentNodes, puks, ruks)
        sla = SLA.SLA(nodes, users, currentNodes, userEnergyOverheads, userTimeOverheads, fuks);
        currentNodes, probabilities = sla.newRound2();
            
            
        rbts = RBTS.RBTS(nodes, users, currentNodes, probabilities);
        answers = rbts.finalAnswers()
            
        believes = BayesianBelief.BayesianBelief(nodes, answers);
        believes.updateReputations();
        i += 1;
        for user in users:
            user.initProbs(constants.NODES);
            user.initTask();
    
    print("New Reputations")
    for node in nodes:
        print(node.__dict__);
        
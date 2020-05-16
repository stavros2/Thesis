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
    userTimeOverheads = compFunctions.computeTimeOverheads(users, ruks, fuks);
    userEnergyOverheads = compFunctions.computeEnergyOverheads(users, constants.USERS, currentNodes, puks, ruks)
   
    sla = SLA.SLA(nodes, users, currentNodes, userEnergyOverheads, userTimeOverheads, fuks);
    newRoundNodes, probabilities = sla.newRound2();
        
        
    """print("New round");
        print(newRoundNodes);
        print("Reports")
        print(probabilities)"""
        
    rbts = RBTS.RBTS(nodes, users, newRoundNodes, probabilities);
    answers = rbts.finalAnswers()
        
    believes = BayesianBelief.BayesianBelief(nodes, answers);
    believes.updateReputations();
    
    print("New Reputations")
    for node in nodes:
        print(node.__dict__);
    
    
    
    """print("Would most of the users wish to change fogNode?");
    print(answers)
    
    print("Nodes");
    for node in nodes:
        print(node.__dict__)
    print("Users");
    for user in users:
        print(user.__dict__)
    print("Distances")
    print(distances);
    print("PUKS")
    print(puks);
    print("GUKS")
    print(guks);
    print("o kathenas en dame");
    print(currentNodes);
    print("RUKS")
    print(ruks)
    print("RUKS in array");
    print(ruksArray)
    
    print("FUKS");
    print(fuks);
    print("Time Overheads");
    print(userTimeOverheads);
    print("Energy Overheads");
    print(userEnergyOverheads);
    print("Total Overheads");
    print(userTimeOverheads + userEnergyOverheads);
    
    print("SLA")
    print(sla.__dict__)
    
    print("RBTS")
    print(rbts.__dict__);
    """
    
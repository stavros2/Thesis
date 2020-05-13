import compFunctions
import constants
import SLA
    
if __name__ == "__main__":
    distances = compFunctions.generateDistances(10, 400, constants.NODES, constants.USERS);
    nodes, users = compFunctions.initalize(constants.NODES, constants.USERS);
    puks = compFunctions.computePUK(distances, constants.NODES, constants.THETA1);
    guks = compFunctions.computeGUK(distances, constants.THETA2);
    currentNodes = compFunctions.firstRound(constants.NODES, constants.USERS)
    
    ruks, ruksArray = compFunctions.computeRUK(nodes, puks, guks, currentNodes, constants.NODES, constants.USERS);
    fuks = compFunctions.computeFUK(nodes, users, currentNodes, constants.NODES, constants.USERS);
    userTimeOverheads = compFunctions.computeTimeOverheads(users, ruks, fuks);
    userEnergyOverheads = compFunctions.computeEnergyOverheads(users, constants.USERS, currentNodes, puks, ruks)
    
    
    sla = SLA.SLA(nodes, users, currentNodes, userEnergyOverheads, userTimeOverheads, fuks);
    newRoundNodes = sla.newRound();
    
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
    print("o kathensa en dame");
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
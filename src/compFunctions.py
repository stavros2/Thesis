import fogNode
import fogUser
import random
import constants
import numpy as np

def initalize(k, u):
    # initalizing 2 lists. One of k fogNodes and one of u fogUsers
    nodes = [];
    users = [];
    for i in range(k):
        temp = fogNode.fogNode();
        nodes.append(temp)
    for i in range(u):
        temp = fogUser.fogUser(k);
        users.append(temp);
    return nodes, users;
    

def generateDistances(start, end, k, u):
    # returning a 2d list with distances between every node and every user. Rows represent nodes and columns represent users
    # inputs is the minimum and maximum distance (start and end) non-inclusive and the number of nodes, k and users, u
    lista = [];
    for i in range(k):
        row = [];
        for j in range(u):
            temp = random.randrange(start, end) + random.random();
            row.append(temp);
        lista.append(row);
    
    return np.array(lista)


def computePUK(distArray, k, theta):
    # Calculate the Puk value for every possible pair of Node and User. Inputs is the distance array and its number of rows and the theta factor
    lista = [];
    for i in range(k):
        distRow = distArray[i];
        maxRow = max(distRow)
        distRowNormalized = distRow / maxRow;
        finalRow = np.power(distRowNormalized, theta)
        lista.append(finalRow);
    return np.array(lista);
    
def computeGUK(distArray, theta):
    # calcalate the Guk value for every possible pair of Node and User. Inpiuts is the distance array an the theta factor
    newArray = 1 / distArray;
    return np.power(newArray, theta);

def firstRound(k, u):
    # a random assignment of each user to a node for the first round. Returns an array of size u with the node number.
    lista = [];
    for i in range(u):
        lista.append(random.randrange(k));
    return lista;

def indices(lista, element):
    return [index for index, value in enumerate(lista) if value == element]


def computeRUK(nodeList, puks, guks, curNodeList, k, u):
    lista = [];
    pinakas = np.zeros((k,u));
    for i in range(u):
        nodeIndex = curNodeList[i];
        node = nodeList[nodeIndex];
        usersOnNode = indices(curNodeList, nodeIndex);
        usersOnNode.remove(i);
        mysum = 0 ;
        for user in usersOnNode:
            mysum += puks[nodeIndex][user] * guks[nodeIndex][user];
        toLog = 1 + (puks[nodeIndex][i] * guks[nodeIndex][i]) / (constants.G0 + mysum) 
        ruk = node.WK * np.log2(toLog)
        lista.append(ruk);
        pinakas[nodeIndex][i] = ruk
    
    return np.array(lista), pinakas;

def computeFUK(nodeList, userList, curNodeList, k, u):
    lista = [];
    for i in range(u):
        nodeIndex = curNodeList[i];
        node = nodeList[nodeIndex];
        usersOnNode = indices(curNodeList, nodeIndex);
        phiSum = 0;
        iotaSum = 0;
        for user in usersOnNode:
            phiSum += userList[user].ongoingTask[1]
            iotaSum += userList[user].ongoingTask[0];
        fuk = userList[i].ongoingTask[1] / phiSum 
        fuk *= 1 - iotaSum / node.BK;
        fuk *= node.FK
        lista.append(fuk)
   
    return np.array(lista);


def computeTimeOverheads(userList, ruks, fuks):
    lista = [];
    for i in range(len(userList)):
        overhead = userList[i].ongoingTask[0] / ruks[i] + userList[i].ongoingTask[2] / fuks[i]   
        lista.append(overhead);
    
    return np.array(lista);

def computeEnergyOverheads(userList, u, curNodeList, puks, ruks):
    lista = [];
    for i in range(u):
        nodeIndex = curNodeList[i];
        EO = userList[i].ongoingTask[0] * puks[nodeIndex][i] / ruks[i];
        lista.append(EO);
        
    return np.array(lista);
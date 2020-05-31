import matplotlib.pyplot as plt
import constants
import numpy as np
from statistics import mean


def plotNodeCharacteristics(nodeList):
    FKs, BKs, mks= [], [], [];
    index = np.array(range(constants.NODES))
    for node in nodeList:
        FKs.append(node.FK / pow(10,10));
        BKs.append(node.BK / pow(10,10));
        mks.append(node.m0);
    
    
    plot = plt.figure();
    plt.title("Node Characteristics");
    plt.bar(index - 0.2, BKs, width = 0.2, color = 'b', align = 'center', label = "BKs");
    plt.bar(index, FKs, width = 0.2, color = 'r', align = 'center', label = "FKs");
    plt.bar(index + 0.2, mks, width = 0.2, color = 'g', align = 'center', label = "mks");
    plt.xticks(range(constants.NODES));
    plt.xlabel("Nodes");
    plt.ylabel("Red and Blue bars in e10")
    plt.legend()
    plt.show()
    
    return plot

def plotUsersOnNode(array):
    plot = plt.figure();
    plt.title("Number of users on each node over time");
    plt.xlabel("SLA Iterations(x100)");
    plt.ylabel("Number of User");
    for i in range(len(array)):
        thisLine = array[i];
        plt.plot(range(len(thisLine)), thisLine, label = str(i));
    
    plt.legend();
    plt.show();
    
    return plot;
    
    
def plotUserProbabilities(array):
    toplot = array.transpose();
    plot = plt.figure()
    plt.title("The probability of choosing each node for user 0");
    for i in range(len(toplot)):
        thisLine = toplot[i];
        plt.plot(range(len(thisLine)), thisLine, label = str(i))
        
        
    plt.legend();
    plt.xlabel("SLA Iterations");
    plt.ylabel("Porbability");
    plt.show();
    
    return plot;

def plotUserReward(array):
    plot = plt.figure();
    plt.plot(range(len(array)), array)
    plt.title("Reward over time for user 0")
    plt.xlabel("SLA Iterations(x100)");
    plt.ylabel("Normalized Reward");
    plt.show();
    
    return plot;


def plotNodeRewards(array):
    toplot = array.transpose();
    plot = plt.figure()
    plt.title("The reward given by each node");
    for i in range(len(toplot)):
        thisLine = toplot[i];
        plt.plot(range(len(thisLine)), thisLine, label = str(i))
        
        
    plt.legend();
    plt.xlabel("SLA Iterations(x100)");
    plt.ylabel("Normalized Reward");
    plt.show();
    
    return plot;

def plotAvgProbabilites(array):
    plot = plt.figure();
    plt.title("Average probability of node chossing");
    plt.xlabel("SLA Iterations");
    plt.ylabel("Avg Probability");
    for i in range(len(array)):
        thisLine = array[i];
        plt.plot(range(len(thisLine)), thisLine, label = str(i));
    
    plt.legend();
    plt.show();
    
    return plot;

def plotNodeRewardCharacteristic(array, element):
    toplot = array.transpose();
    plot = plt.figure()
    plt.title("The " + element + " of each node");
    for i in range(len(toplot)):
        thisLine = toplot[i];
        plt.plot(range(len(thisLine)), thisLine, label = str(i))
        
        
    plt.legend();
    plt.xlabel("SLA Iterations(x100)");
    plt.ylabel(element);
    plt.show();
    
    return plot;
    
def plotBarCharacteristics(array, element):
    toplot = array.transpose();
    plot = plt.figure()
    plt.title("The avarage " + element + " of each node");
    plotMaterial = [];
    for i in range(constants.NODES):
        plotMaterial.append(mean(toplot[i]));
    
        
    plt.bar(range(constants.NODES), plotMaterial)
    plt.xticks(range(constants.NODES))
    plt.xlabel("Nodes");
    plt.ylabel(element);
    plt.show();
    
    return plot;
    
def plotAvgReward(array):
    plot = plt.figure();
    plt.title("Average Reward for users");
    plt.xlabel("SLA Iterations");
    plt.ylabel("Avg Reward");
    plt.plot(range(len(array)), array)
    plt.show();
    
    return plot;

def pltStep2dlist(list2d, element):
    plot = plt.figure();
    plt.title(element + " of nodes over time")
    plt.xlabel("Timeslot");
    plt.ylabel(element);
    for i in range(len(list2d)):
        plt.step(range(len(list2d[i])),list2d[i], label = str(i));
    
    plt.legend();
    plt.show();
    return plot


def plotReps(list2d):
    plot = plt.figure();
    plt.title("Reputation of nodes over time")
    plt.xlabel("Timeslot");
    plt.ylabel("Reputation");
    for i in range(len(list2d)):
        plt.plot(range(len(list2d[i])),list2d[i], label = str(i));
    
    plt.legend();
    plt.show();
    return plot
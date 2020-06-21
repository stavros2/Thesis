import numpy as np

class MonteCarloSmoothing:
    def extend(self, toExtend):
        maxSize = len(max(toExtend, key = len));
        listOfLists = []
        for array in toExtend:
            lista = list(array)
            toAdd = lista[-1];
            for i in range(len(lista), maxSize):
                lista.append(toAdd);
            listOfLists.append(lista)   
        return listOfLists;
    
    def smooth(self, toSmooth):
        extended = self.extend(toSmooth);
        avg = np.zeros(len(extended[0]));
        for lista in extended:
            avg = avg + np.array(lista);
        
        avg = avg / len(extended);
        
        return avg;
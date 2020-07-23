import time
start_time = time.time()
import sys
from scipy.spatial.distance import pdist, squareform
import numpy as np
import os

class ReadData():
    def __init__(self, filename):

        self.name = filename
        self.size = self.getSize()
        self.EdgeWeightType = self.getEdgeWeightType()
        self.format_ = self.getFormat()  
        self.time_to_read = 0

    def getFormat(self):
        format_ = "None"
        try:
            with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'NearestNeighbour/trial.tsp')) as data:
                datalist = data.read().split()
                for ind, elem in enumerate(datalist):
                    if elem == "EDGE_WEIGHT_FORMAT:":
                        format_ = datalist[ind + 1]
                        break
                    elif elem == "EDGE_WEIGHT_FORMAT":
                        format_ = datalist[ind + 2]
                        break
            return format_

        except IOError:
            print("Input file not found1")
            sys.exit(1)

    def getEdgeWeightType(self):
        EdgeType = "None"
        try:
            with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'NearestNeighbour/trial.tsp')) as data:
                datalist = data.read().split()
                for ind, elem in enumerate(datalist):
                    if elem == "EDGE_WEIGHT_TYPE:":
                        EdgeType = datalist[ind + 1]

                        break
                    elif elem == "EDGE_WEIGHT_TYPE":
                        EdgeType = datalist[ind + 2]

                        break
            return EdgeType

        except IOError:
            print("Input file not found2")
            sys.exit(1)

    def getSize(self):

        size = 0
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'NearestNeighbour/trial.tsp')) as data:
            datalist = data.read().split()
            for ind, elem in enumerate(datalist):
                if elem == "DIMENSION:":
                    size = datalist[ind + 1]
                    #print(size)
                    break
                elif elem == "DIMENSION":
                    size = datalist[ind + 2]
                    #print(size)
                    break
            return int(size)

    def read_Data(self):
        with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'NearestNeighbour/trial.tsp')) as data:
            cities = []
            Isdata = True
            while (Isdata):
                line = data.readline().split()
                if len(line) <= 0:
                    break
                tempcity = []
                for i, elem in enumerate(line):
                    try:
                        temp = float(elem)
                        tempcity.append(temp)
                    except ValueError:
                        break
                if len(tempcity) > 0:
                    cities.append(np.array(tempcity))
        return np.array(cities)

    def GetDistanceMat(self):

        if self.EdgeWeightType == "EUC_2D":
            DistanceMat = self.EuclidDist()
            self.time_to_read = time.time() - start_time
            return DistanceMat
        else:
            return None

    def EuclidDist(self):
        cities = self.read_Data()
        A = cities[:, 1:3]
        DistanceMat = np.round(squareform(pdist(A)))
        return DistanceMat

   

    def getMat(self):
        DataFormat = self.getFormat()
        if DataFormat == "FULL_MATRIX":
            cities = self.read_Data()
            DistanceMat = cities[:self.size]
            return DistanceMat



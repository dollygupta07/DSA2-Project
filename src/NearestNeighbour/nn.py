''' *****************Implementing Nearest Neighbour algorithm in TSP************** '''
import time
start_time = time.time()
import sys
from NearestNeighbour.readData import ReadData
import numpy as np
import os

class NN():
    name = "Nearest Neighbor"

    def __init__(self, file):

        self.file = file
        self.instance = ReadData(self.file)
        self.size = self.instance.size
        self.dis_mat = self.instance.GetDistanceMat()
        self.time_read = self.instance.time_to_read
        self.time_algo = 0

    def get_dist_mat(self):

        D = self.dis_mat.copy()
        for i in range(self.size):
            D[i][i]=np.inf
        return D


    def nn_algo(self,startPoint):
    
        dist_mat = self.get_dist_mat()
        Tour = [startPoint]
        for _ in  range(self.size-1):
            min_index = np.argmin(dist_mat[Tour[-1]])
            for t in Tour:
                dist_mat[min_index][t] = np.inf
                dist_mat[t][min_index] = np.inf
            Tour.append(min_index)
        return np.array(Tour)

    
    def run(self):

        tours_dist = []
        tours = []
        self.write_info()
        startPoints = self.stat_pt_list()
        for s in startPoints:
            t = self.nn_algo(s)
            d = self.get_tour_distance(t)
            tours.append(t+1)
            tours_dist.append(d)
        
        self.best_tour(tours,tours_dist) 

    def best_tour(self,Ts,Tsd):
        min_dist_index = np.argmin(Tsd)
        self.write_stat(Tsd[min_dist_index], Ts[min_dist_index])

    def get_tour_distance(self,T):
        s = 0
        for i,t in enumerate(T):
            try:
                s+=self.dis_mat[t][T[i+1]]
            except IndexError:
                s+=self.dis_mat[t][T[0]]
        return s

    def write_info(self):


        print("\nNumber of cities : ", self.size)
        print("\n \t Running Nearest Neighbour Algorithm over 50 random tours ")

    def write_stat(self,D,T):

        print("\n Tour Distance: ",D)
        print("\n Best Tour by Nearest Neighbour is: \n", T)
        print("\n Time to read instance (sec): ", round(self.time_read))
        self.time_algo = time.time() - start_time
        print(" Time to run instances(sec): ", round(self.time_algo))
        print(" Total Time (sec): ", round(self.time_read+self.time_algo))
   
    def stat_pt_list(self):

        np.random.seed(1)
        a = round(self.size*0.1)
        mi = 10
        mx = 1000
        if a>mx:
            l = np.random.choice(self.size, mx, replace=False)
            return(l)
        elif a<=10:
            l = np.random.choice(self.size, mi, replace=False)
            return(l)
        else:
            l = np.random.choice(self.size, a, replace=False)
            return(l)


def main(filename):
	graph_file = open(filename)
	t = NN(graph_file)
	t.run()

if __name__ == '__main__':
    main(filename)	          

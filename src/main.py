import MinCut.algo.mincut as mincut
import KLforcircuits.klc as klc
import LKTSP.lktsp as lktsp
from NearestNeighbour.readData import ReadData
import NearestNeighbour.nn as nn
import os

def min_cut():
    print("\nRunning Karger-Stein's MinCut algorithm.....")
    print('*'*70)
    os.getcwd()
    # Input files to initialize the graph
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'MinCut/data/KargerMinCut.txt')
    print(f'\nInput file used: {filename}')
    mincut.main(filename)
    print('*'*70)
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'MinCut/data/RandomGraph.txt')
    print(f'\nInput file used: {filename}')
    mincut.main(filename)
    print('*'*70)
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'MinCut/data/test1.txt')
    print(f'\nInput file used: {filename}')
    mincut.main(filename)
    print('*'*70)

def kl(): 
    print("\nRunning Kernighan Lin's algorithm for circuit partitioning.....")
    print('*'*70)
    klc.main()
    print('*'*70)

def tspopt():
    print("\nRunning 2-opt Lin Kernighan algorithm for solving TSP.....")
    print('*'*70)
    os.getcwd()
    # Input files to initialize the graph
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'LKTSP/tsp_example_1.txt')
    print(f'\nInput file used: {filename}')
    lktsp.main(filename)
    print('*'*70)

def nearest():
    print("\nRunning Nearest Neighbour algorithm for solving TSP.....")
    print('*'*70)
    os.getcwd()
    # Input files to initialize the graph
    filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'NearestNeighbour/trial.tsp')
    print(f'\nInput file used: {filename}')
    nn.main(filename)
    print('*'*70)

def main():
    min_cut()
    kl()
    tspopt()
    nearest()
    
if __name__ == '__main__':
    main()




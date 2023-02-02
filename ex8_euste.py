'''
Exercise 8: Game of Life

Implement Conway's game of life using numpy array to hold data.

Neighbours are defined as adjacent cells.

    Any LIVING cell with 2 or 3 neighbours survives.
    Any DEAD cell with 3 neighbours comes alive.
    Any OTHER LIVING cell dies.
    All deaths and births occur simultaneously
    
'''

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

class Game_of_Life(object):
    
    def __init__(self,N=0,lattice=None):
        if N==0:
            self.lattice = lattice
        else:
            self.N = N
            self.lattice = np.random.randint(0,2,size=(N,N))
            
        self.counter = np.zeros(self.lattice.shape)
        
        
    def count_neighbor(self):
        '''
        Calculate the number of alive neighbors.
        '''
        self.counter = np.roll(self.lattice,1,axis=1) + \
            np.roll(self.lattice,-1,axis=1) + \
                np.roll(self.lattice,1,axis=0) + \
                    np.roll(self.lattice,-1,axis=0) +\
                        np.roll(self.lattice,1,axis=(0,1)) +\
                            np.roll(self.lattice,1,axis=(1,0)) +\
                                np.roll(self.lattice,-1,axis=(0,1)) +\
                                    np.roll(self.lattice,-1,axis=(1,0))
    

        
    def imshow(self,X):
        plt.imshow(X)
        plt.pause(0.01)
        plt.show()
        
        
    def evolve(self,t_max=50):
        for t in range(t_max):
            self.counter = np.zeros(self.lattice.shape)
            
            self.count_neighbor()
            
            #die if alive and neighbor not 2 or 3
            self.lattice[np.where((self.lattice==1) & ((self.counter!=2) | (self.counter!=3)))] = 0
            
            #add child if neighbor 3
            self.lattice[np.where((self.lattice==0) & (self.counter==3))] = 1
            
            self.imshow(self.lattice)


        
    
            
            
            
    
X = np.genfromtxt('gun.txt')
    

game = Game_of_Life(lattice=X)
game.evolve(t_max=50)


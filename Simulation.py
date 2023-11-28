import numpy as np
import math
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
import time

matrix_x = 1000
matrix_y = 1000

class Array:
    def __init__(self,size = 120):
        self.size = (size,size)
        self.rows = size
        self.columns = size
        self.array = self.create_array()

    def create_array(self):
        array = np.zeros((120,120), dtype = int)
        return(array)

def step(life_array,neighbors_array):
    for (i,j), cell in np.ndenumerate(life_array.array):

        if life_array.array[i,j] == 1 and neighbors_array.array[i,j] < 2: # Rule 1
            life_array.array[i,j] = 0
        elif life_array.array[i,j] == 1 and neighbors_array.array[i,j] > 3: # Rule 3 
            life_array.array[i,j] = 0 
        elif neighbors_array.array[i,j] == 3: # Rule 4
            life_array.array[i,j] = 1

def simulate(): 

    neighbors_array = Array() 
    life_array = Array()
    life_array.array = np.random.choice([0,1],size = life_array.size)
    life_array_state_list = []
    neighbors_array_state_list = []
    neighbors_array_state_list.append(np.copy(life_array))
    
    for epoch in range (1,200):
        for (i, j), cell in np.ndenumerate(life_array.array):
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if [x,y] == [i,j] or x < 0 or y < 0 or x >= life_array.rows or y >= life_array.rows:
                        continue
                    elif life_array.array[x,y] == 1:
                        neighbors_array.array[i,j] += 1
        
        step(life_array,neighbors_array)
        life_array_state_list.append(np.copy(life_array.array))

        neighbors_array_state_list.append(neighbors_array.array)
        neighbors_array.array = np.zeros(neighbors_array.size, dtype = int)

    return life_array_state_list                       
        
life_sim = simulate()
fig, ax = plt.subplots()

#Visualization

def update(frame):
    ax.clear()
    ax.imshow(life_sim[frame], cmap='gray')

ani = FuncAnimation(fig,update,frames = len(life_sim), interval = 50)
plt.show()
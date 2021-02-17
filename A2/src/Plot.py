## @file Plot.py
#  @author Bhavna Pereira
#  @brief Function to plot objects in motion
#  @date 16/02/2021
#  @details

import matplotlib.pyplot as plt

## @brief This method 
def plot(w,t):
    if len(w) != len(t):
        raise ValueError
    else:
        fig, axs = plt.subplots(3)
        fig.suptitle('Motion Simulation')
        axs[0].set(ylabel = 'x(m)')
        axs[1].set(ylabel = 'y(m)')
        axs[2].set(ylabel = 'y(m)')
        axs[2].set(xlabel = 'x(m)')
        x = []
        y = []
        for i in range(0, len(w)):
            x.append(w[i][0])
        for i in range(0, len(w)):
            y.append(w[i][1])
        axs[0].plot(x, t)
        axs[1].plot(y, t)
        axs[2].plot(y, x)
        plt.show()

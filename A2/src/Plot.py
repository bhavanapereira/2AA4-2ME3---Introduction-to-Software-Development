## @file Plot.py
#  @author Bhavna Pereira
#  @brief Function to plot objects in motion
#  @date 16/02/2021
#  @details Using the matplotlib library, the function
#           provides a visual representation of objects in motion

import matplotlib.pyplot as plt

## @brief This method sets up and graphs the track of objects in motion
#  @details the method creates three subplots to represent to compare
#           the x coordinate of the CM against the time of motion, the y coordinate
#           of the CM against the time of motion, and the x coordinate versus the
#           y coordinate
#  @param w represents a sequence of sequences
#  @param t represents the sequence of time values


def plot(w, t):
    if len(w) != len(t):
        raise ValueError
    else:
        fig, axs = plt.subplots(3)
        fig.suptitle('Motion Simulation')
        axs[0].set(ylabel='x(m)')
        axs[1].set(ylabel='y(m)')
        axs[2].set(ylabel='y(m)')
        axs[2].set(xlabel='x(m)')
        x = []
        y = []
        for i in range(0, len(w)):
            x.append(w[i][0])
        for i in range(0, len(w)):
            y.append(w[i][1])
        axs[0].plot(t, x)
        axs[1].plot(t, y)
        axs[2].plot(x, y)
        plt.show()

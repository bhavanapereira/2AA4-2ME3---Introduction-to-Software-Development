## @file Scene.py
#  @author Bhavna Pereira
#  @brief Class implementation of Scene with the use of Shape.py
#  @date 16/02/2021
#  @details The class makes use of the shape of the object, its
#           unbalanced forces in order to create data points to track its
#           motion


import scipy.integrate

## @brief The following class outlines properties of an object in motion
#  @details The properties include the shape, its initial velocities, and
#           the forces acting upon it


class Scene:
    ## @brief This method is a constructor for Scene
    #  @details The method creates state variables for the shape type,
    #           its velocities, and the forces acting upon it
    #  @param the method takes in five parameters s, Fx, Fy, vx, vy
    #         to represent the shape, horizontal acting forces,
    #         vertical acting forces, initial horizontal velocity, and initial
    #         vertical velocity, respectively
    def __init__(self, s, Fx, Fy, vx, vy):
        self.__s = s
        self.__Fx = Fx
        self.__Fy = Fy
        self.__vx = vx
        self.__vy = vy

    ## @brief this method returns the shape of the object
    #  @returns Returns the state variable of the correct type
    def get_shape(self):
        return self.__s

    ## @brief this method returns the forces acting upon the objects
    #         both horizontally and vertically
    #  @returns Returns the state variable of the correct type
    def get_unbal_forces(self):
        return self.__Fx, self.__Fy

    ## @brief this method returns the velocity of the object
    #         both horizontally and vertically
    #  @returns Returns the state variable of the correct type
    def get_init_velo(self):
        return self.__vx, self.__vy

    ## @brief this method sets the property of the shape to a
    #         variable to be used in calculation
    def set_shape(self, s):
        self.__s = s

    ## @brief this method sets the property of the forces to
    #         variables to be used in calculation
    def set_unbal_forces(self, Fx, Fy):
        self.__Fx = Fx
        self.__Fy = Fy

    ## @brief this method sets the property of the velocities to
    #         variables to be used in calculation
    def set_init_velo(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    ## @brief this method extracts data points to represent the track of
    #         the object in motion
    #  @details
    #  @param the method takes in two parameters representing the final time
    #         and the number of steps or movements of the object
    #  @returns the method returns the time and the respective track of the
    #           object for each moment of its course in motion
    def sim(self, tfinal, nsteps):
        t = []
        for i in range(0, nsteps):
            t.append((i * tfinal) / (nsteps - 1))
            val = [self.__s.cm_x(), self.__s.cm_y(), self.__vx, self.__vy]
            val2 = scipy.integrate.odeint(self.ode, val, t)
        return (t, val2)

    def ode(self, w, t):
        return (w[2], w[3], self.__Fx(t) / self.__s.mass(), self.__Fy(t) / self.__s.mass())

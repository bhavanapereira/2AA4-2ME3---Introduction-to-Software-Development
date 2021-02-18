## @file Scene.py
#  @author Nathan Uy
#  @brief Contains the Scene module which creates scenes.
#  @date 02/16/2021
#  @details A Scene has a shape, unbalance force functions in x and y
#  and initial velocities in x and y.

from scipy.integrate import odeint
from Shape import Shape

## @brief An abstract data type that represents a scene.


class Scene:

    ## @brief A Scene constructor.
    # @details Initializes a Scene object with s, fx, fy, vx, and vy.
    # @param s A shape object.
    # @param fx The unbalanced force function in the x direction.
    # @param fy The unbalanced force function in the y direction.
    # @param vx A float that represents the x direction of initial velocity.
    # @param vy A float that represents the x direction of initial velocity.
    def __init__(self, s, fx, fy, vx, vy):
        self.s = s
        self.fx = fx
        self.fy = fy
        self.vx = vx
        self.vy = vy

    ## @brief Gets the shape of the Scene object.
    # @return A Shape object.
    def get_shape(self):
        return self.s

    ## @brief Gets the unbalanced force functions in the x and y direction.
    # @return 2 functions that represent the unbalanced force functions
    # in the x and y direction, respectively.
    def get_unbal_forces(self):
        return (self.fx, self.fy)

    ## @brief Gets the initial velocity in the x and y direction.
    # @return 2 floats that represent the initial velocity in the
    # x and y direction, respectively.
    def get_init_velo(self):
        return (self.vx, self.vy)

    ## @brief Sets the Shape of the Scene object.
    # @param s A Shape object that will replace the Scene's current Shape.
    def set_shape(self, s):
        self.s = s

    ## @brief Sets the unbalanced force functions of the Scene object.
    # @param newfx A function that will replace the Scene's current
    # unbalanced force function in x direction.
    # @param newfy A function that will replace the Scene's current
    # unbalanced force function in y direction.
    def set_unbal_forces(self, newfx, newfy):
        self.fx = newfx
        self.fy = newfy

    ## @brief Sets the initial velocities of the Scene object.
    # @param newvx A float that will replace the Scene's current
    # initial velocity in the x direction.
    # @param newvy A float that will replace the Scene's current
    # initial velocity in the y direction.
    def set_init_velo(self, newvx, newvy):
        self.vx = newvx
        self.vy = newvy

    ## @brief Calculates the interval of t and the odeint of the object.
    # @details Uses the scipy library to calculate odeint
    # @param tfinal A float that represents the final time.
    # @param nsteps An integer greater than or equal to zero
    # that represents the number of partitions of t.
    # @return A sequence of floats and a sequence of sequence of 4 floats
    # that represents the t interval and the odeint respectively.
    def sim(self, tfinal, nsteps):
        t = list(map(lambda i: i * tfinal / (nsteps - 1), range(nsteps)))
        return t, odeint(self.__ode__, [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy], t)

    ## @brief Calculates the derivative of seq at t.
    # @param seq A sequence of 4 floats.
    # @param t A float that represents the time.
    # @return A sequence of 4 floats which represents the
    # derivative of seq at t.
    def __ode__(self, seq, t):
        new_seq = [seq[2], seq[3], self.fx(t) / self.s.mass(), self.fy(t) / self.s.mass()]
        return new_seq

## @file
#  @author
#  @brief
#  @date
#  @details


import scipy.integrate

class Scene:

    def __init__(self, s, Fx, Fy, vx, vy):
        self.__s = s
        self.__Fx = Fx
        self.__Fy = Fy
        self.__vx = vx
        self.__vy = vy

    def get_shape(self):
        return self.__s

    def get_unbal_forces(self):
        return self.__Fx, self.__Fy

    def get_init_velo(self):
        return self.__vx, self.__vy

    def set_shape(self, s):
        self.__s = s

    def set_unbal_forces(self, Fx, Fy):
        self.__Fx = Fx
        self.__Fy = Fy

    def set_init_velo(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    def sim(self, tfinal, nsteps):
        t = []
        for i in range(0, nsteps):
            t.append((i * tfinal)/(nsteps - 1))
            val = [self.__s.cm_x(), self.__s.cm_y(), self.__vx, self.__vy]
            val2 = scipy.integrate.odeint(self.ode, val,t)
        return (t, val2)


    def ode(self,w,t):
        return (w[2], w[3], self.__Fx(t)/self.__s.mass(), self.__Fy(t)/self.__s.mass())

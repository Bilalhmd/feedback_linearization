import numpy as np



class StateControlTrajectory(np.ndarray):
    """A state-control trajectory, used to store a trajectory for a full simulation.

    This data structure is extending an `np.array` with shape
    [horizon + 1, state_size + control_size].
    """

    def __new__(cls, state_size, control_size, horizon):
        obj = np.ndarray.__new__(
            cls, shape=(horizon + 1, state_size + control_size))
        obj[:] = 0.
        return obj

    def __init__(self, state_size, control_size, horizon):
        """Initializes our array.

        Args:
            state_size: Size of states.
            control_size: Size of controls.
            horizon: The length of the trajectory.
        """
        self.n = state_size
        self.m = control_size
        self.N = horizon

    def __reduce__(self):
        pickled_state = super(
            StateControlTrajectory, self).__reduce__()
        new_state = pickled_state[2] + (self.n, self.m, self.N,)
        return pickled_state[0], pickled_state[1], new_state

    def __setstate__(self, state):
        super(StateControlTrajectory, self).__setstate__(state[:-3])
        self.__init__(*state[-3:])

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.n = getattr(obj, 'n', None)
        self.m = getattr(obj, 'm', None)
        self.N = getattr(obj, 'N', None)

    def __array_wrap__(self, out_arr, context=None):
        return np.ndarray.__array_wrap__(self, out_arr, context)

    @property
    def x(self):
        return self[:, :self.n]

    @x.setter
    def x(self, value):
        self[:, :self.n] = value

    @property
    def u(self):
        return self[:-1, self.n:]

    @u.setter
    def u(self, value):
        self[:-1, self.n:] = value

    def get_x_trajectory(self):
        return self.x.transpose()

    def get_u_trajectory(self):
        return self.u.transpose()
import numpy as np
import sympy as sp # sympy is a symbolic mathematics library




def compute_jacobian(f, x):
    """ function for symbolic computation of jacobians.
    Args:
        f: symbolic vector function
        x: symbolic vector of variables

    Returns:
        J: jacobian of the given function f relative to the variables in x
        """
    return None

class RobotModel(object):

    def __init__(self, joints, parameters):
        """ initialize the robot model class

        Args:
            joints:
            parameters:

            """
        self.kinematics = RobotKinematics(joints, parameters)
        self.dynamics = RobotDynamics(self.kinematics)



    def __call__(self, *args, **kwargs):
        "calls one integration step of the dynamics"
        pass




    




class RobotKinematics(object):
    """ Symbolic and Numerical Evaluation of the Kinematics of the Biped """

    def __init__(self, joints, parameters):
        """ initialize the robot kinematics class """

        self.joints = joints
        self.parameters = parameters

        self.vars = None

        self.sym_pos = None
        self.sym_vel = None

        self.lambda_pos = None
        self.lambda_vel = None




    def _change_coordinates(self):
        pass

    def _construct_position(self):
        pass

    def  _construct_velocity(self):
        pass

    def position(self):
        pass

    def velocity(self):
        pass

    def ground_detection(self, terrain):
        pass





class RobotDynamics(object):
    """ Derives the Equations of motion for the Biped in the swing phase using basic Lagrangian Formulation
        both symbolic and numerical functions are available """

    def __init__(self, kinematics):
        """ initialize the robot dynamics class """
        self.kinematics = kinematics

    def _create_kinetic_energy(self):
        pass

    def _create_potential_energy(self):
        pass

    def _create_mass_matrix(self):
        """ constructs symbolic mass matrix for the model """
        pass

    def _create_coriolis_matrix(self):
        """ constructs symbolic coriolis matrix for the model """
        pass

    def _create_gravity_matrix(self):
        """ constructs symbolic gravity matrix for the model """
        pass

    def _create_control_matrix(self):
        """ constructs symbolic control matrix for the model """
        raise NotImplementedError('symbolic control matrix is not implemented!')

    def _conservation_momentum(self):
        pass

    def _noslip_condition(self):
        pass

    def mass_matrix(self):
        pass

    def coriolis_matrix(self):
        pass

    def gravity_matrix(self):
        pass

    def control_matrix(self):
        pass

    def kinetic_energy(self):
        pass

    def potential_energy(self):
        pass

    def ct_dx(self):
        """ Symbolic continuous time dynamics in state space notation """
        pass
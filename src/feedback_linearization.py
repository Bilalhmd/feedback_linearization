""" Controller implemented in this file is based on the following script:
    Stable Walking of a 7-DOF Biped Robot
    by Plestan, Grizzle, Westervelt, Abba
    Transactions on Robotics and Automation, August 2003
"""


class Controller(object):
    """ Constructs a Feedback Linearization controller for the biped and provides a numerical evaluation function """
    def __init__(self, robot_model):
        self.robot_model = robot_model
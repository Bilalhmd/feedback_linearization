# in this file we experiment with constructing the code

from robot_model import RobotKinematics

robot_parameters = {'g':9.81,}
robot_joints = ['q1', 'q2', 'q3',]


def test_kinematics(joints, parameters):
    kinematics = RobotKinematics(joints, parameters)






def test_dynamics(joints,parameters):
    test_kinematics(joints,parameters)
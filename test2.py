
# Example number 2, 
# Mirco Robotic ARM 

from connect import openconnection
import sim
from time import sleep
clientId = openconnection()

err , joint1 = sim.simxGetObjectHandle(clientId, "MicoHand_fingers12_motor1",  sim.simx_opmode_blocking)
err2 , joint2 = sim.simxGetObjectHandle(clientId, "RG2_openCloseJoint",  sim.simx_opmode_blocking)

print(err2)
while True:
    sim.simxSetJointTargetVelocity(clientId, joint2, .04, sim.simx_opmode_oneshot)
    sleep(5)
    sim.simxSetJointTargetVelocity(clientId, joint2, -.04, sim.simx_opmode_oneshot)
    sleep(5)



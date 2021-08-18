import sim
from time import sleep
import sys
print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections

clientID = -1   # Client ID returned from the API will be stored here

# Connect to the API and optain a client ID
while clientID == -1:
    try:
        clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
        if clientID == -1:
            print('Unable to connect to the API, Retrying after 2 sec...')
            sleep(2)
        else:
            print('Connected the API...')
    except KeyboardInterrupt:
        sys.exit("Application closed by the user")
    except:
        sys.exit("Something went wrong! Exiting application.")


# Getting object handle of the motors in the sim env
errorcode, motorleft = sim.simxGetObjectHandle( clientID, "Pioneer_p3dx_leftMotor", sim.simx_opmode_blocking)
errorcode, motorright = sim.simxGetObjectHandle( clientID, "Pioneer_p3dx_rightMotor", sim.simx_opmode_blocking)

while True:
    x = input("Please input directions: ")
    if x == "1":
        sim.simxSetJointTargetVelocity(clientID, motorleft, 0.2, sim.simx_opmode_oneshot) # giving 0.2 forward speed to the left motor
        sim.simxSetJointTargetVelocity(clientID, motorright, 0.2, sim.simx_opmode_oneshot) # giving 0.2 forward speed to the right motor
    elif x == "-1":
        sim.simxSetJointTargetVelocity(clientID, motorleft, -0.2, sim.simx_opmode_oneshot)  # giving 0.2 backward speed to the left motor
        sim.simxSetJointTargetVelocity(clientID, motorright, -0.2, sim.simx_opmode_oneshot) # giving 0.2 backward speed to the right motor
    else:
        sim.simxSetJointTargetVelocity(clientID, motorleft, 0, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetVelocity(clientID, motorright, 0, sim.simx_opmode_oneshot)



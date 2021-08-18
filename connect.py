
import sys
import sim 
from time import sleep


def openconnection():
    clientID = -1
    while clientID == -1:
        try:
            clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
            if clientID == -1:
                print('Unable to connect to the API, Retrying after 2 sec...')
                sleep(2)
            else:
                print('Connected the API...')
                return clientID
        except KeyboardInterrupt:
            sys.exit("Application closed by the user")
        except:
            sys.exit("Something went wrong! Exiting application.")

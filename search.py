from robot import ROBOT
import random
import pyrosim
import matplotlib.pyplot as plt

for i in range(0,10):
	sim =pyrosim.Simulator( play_paused = False , eval_time=100)
	robot = ROBOT( sim, random.random()*2 -1)
	sim.start()
	sim.wait_to_finish()
#sensorData=sim.get_sensor_data(sensor_id=P2)
#print(sensorData)
#f=plt.figure()
#panel=f.add_subplot(111)
#plt.plot(sensorData)
#panel.set_ylim(-2,+2)
#plt.show()





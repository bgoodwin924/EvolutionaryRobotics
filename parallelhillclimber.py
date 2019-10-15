from population import POPULATION
from robot import ROBOT
from individual import INDIVIDUAL
import copy
import pickle
import random
import pyrosim
import matplotlib.pyplot as plt

parents=POPULATION(10)
parents.Evaluate()
parents.Print()
for i in range(1,200):
	children=copy.deepcopy(parents)
	children.Mutate()
	children.Evaluate()
	parents.ReplaceWith(children)
	print(i),
	parents.Print()
parents.Evaluate2()
#parent=INDIVIDUAL()
#parent.Evaluate(True)
#print(parent.fitness)
#for i in range(0,100):
#	child=copy.deepcopy( parent )
#	child.Mutate()
#	child.Evaluate(True)
#	print('[g:',i,']','[pw',parent.genome,']','[p:',parent.fitness, ']','[c:',child.fitness,']')
#	if(child.fitness > parent.fitness):
#		child.Evaluate(False)
#		parent=child
		#f=open('robot.p','w')
		#pickle.dump(parent,f)
		#f.close()
		
	
	

	#sim =pyrosim.Simulator( play_paused = False , eval_time=100)
	#robot = ROBOT( sim, random.random()*2 -1)
	#sim.start()
	#sim.wait_to_finish()
	#x=sim.get_sensor_data(sensor_id=robot.P4, svi=0)
	#y=sim.get_sensor_data(sensor_id=robot.P4, svi=1)
	#z=sim.get_sensor_data(sensor_id=robot.P4, svi=2)
	#print(y[-1])







#sensorData=sim.get_sensor_data(sensor_id=P2)
#print(sensorData)
#f=plt.figure()
#panel=f.add_subplot(111)
#plt.plot(sensorData)
#panel.set_ylim(-2,+2)
#plt.show()





import random
import math
import numpy
import pyrosim
from robot import ROBOT
class INDIVIDUAL:
	def __init__(self, i):
		self.ID=i
		self.fitness=0
		self.genome = 1* numpy.random.random((4,8))*2 -1
		#self.genome = numpy.random.random(4)*2 -1		
	def Start_Evaluate(self, pb):
		self.sim =pyrosim.Simulator( play_paused = False , eval_time=1000, play_blind=pb)
		self.robot = ROBOT( self.sim, self.genome)
		self.sim.start()
	def Computer_Fitness(self):
		self.sim.wait_to_finish()
		y=self.sim.get_sensor_data( sensor_id=self.robot.P4, svi=1)
		self.fitness=y[-1]
		del self.sim
		pass
	def Mutate(self):
		geneToMutateRow=random.randint(0,3)
		geneToMutateCol=random.randint(0,7)
		self.genome[geneToMutateRow,geneToMutateCol] = random.gauss(self.genome[geneToMutateRow,geneToMutateCol],math.fabs(self.genome[geneToMutateRow,geneToMutateCol]))
		#print(self.genome[geneToMutateRow,geneToMutateCol])
		if(self.genome[geneToMutateRow,geneToMutateCol] >1):
			self.genome[geneToMutateRow,geneToMutateCol]=1
		if(self.genome[geneToMutateRow,geneToMutateCol] <-1):
			self.genome[geneToMutateRow,geneToMutateCol] =-1 
	def Print(self):
		print('['),
		print(self.ID),
		print(self.fitness),
		print(']'),
		

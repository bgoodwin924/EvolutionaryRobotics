from individual import INDIVIDUAL
import copy
import random
class POPULATION:
	def __init__ (self,popSize):
		self.p={}
		self.popSize= popSize	
	def Print(self):
		for i in self.p:
			if(i in self.p):
				self.p[i].Print()
		print()
	def Evaluate(self):
		for i in self.p:
			self.p[i].Start_Evaluate(True)
		for i in self.p:
			self.p[i].Computer_Fitness()
	def Evaluate2(self):
		for i in self.p:
			self.p[i].Start_Evaluate(False)
		for i in self.p:
			self.p[i].Computer_Fitness()
	def Evaluate3(self):
		self.p[0].Start_Evaluate(False)
		self.p[0].Computer_Fitness()	
	def Mutate(self):
		for i in self.p:
			self.p[i].Mutate()
	def ReplaceWith(self, other):
		for i in self.p:
			if(self.p[i].fitness < other.p[i].fitness):
				self.p[i] = other.p[i]
	def Initialize(self):
		for i in range(0,self.popSize):
			self.p[i]=INDIVIDUAL(i)
	def Fill_From(self , other):
		self.Copy_Best_From(other)
		#self.Print()
		self.Collect_Children_From(other)
		#self.Print()
	def Copy_Best_From(self,other):
		index=0
		best=0
		for i in range(0,self.popSize):
			if(best < other.p[i].fitness):
				best= other.p[i].fitness
				index=i
		cop=copy.deepcopy(other.p[index])
		self.p[0]=cop
		
	def Collect_Children_From(self, other):
		for i in range(1,self.popSize):
			#cop=copy.deepcopy(other.p[i])
			#self.p[i]=cop
			winner=other.Winner_Of_Tournament_Selection()
			cop=copy.deepcopy(winner)
			self.p[i]=cop
			self.p[i].Mutate()
	def Winner_Of_Tournament_Selection(other):
		p1=random.randint(0,len(other.p)-1)
		p2=random.randint(0,len(other.p)-1)
		while(p1==p2):
			p2=random.randint(0,len(other.p)-1)
		if(other.p[p1].fitness > other.p[p2].fitness):
			return other.p[p1]
		else:
			return other.p[p2]
		
			

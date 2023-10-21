import random
from random import randrange
import robby

rw = robby.World(10, 10)
rw.graphicsOff(message="")

#Calculating the fitness of a genome
def fitness(g):
	score = 0
	#Testing the strategy for 100 different scenarios
	for j in range(0, 100):
		rw.distributeCans(density=0.50)
		for i in range(0, 200):			
			current = rw.getPerceptCode()
			if(g[current] == '0'):
				score+=rw.performAction("MoveNorth")
			elif(g[current] == '1'):				
				score+=rw.performAction("MoveSouth")
			elif(g[current] == '2'):				
				score+=rw.performAction("MoveEast")
			elif(g[current] == '3'):				
				score+=rw.performAction("MoveWest")
			elif(g[current] == '4'):
				score+=rw.performAction("StayPut")
			elif(g[current] == '5'):
				score+=rw.performAction("PickUpCan")
			elif(g[current] == '6'):				
				score+=rw.performAction("MoveRandom")

	#average score over 100 different runs
	score = score/100
	return score

#Sort individuals in the population by fitness
def sortByFitness(genomes):
    tuples = [(fitness(g), g) for g in genomes]
    tuples.sort()
    sortedFitnessValues = [f for (f, g) in tuples]
    sortedGenomes = [g for (f, g) in tuples]
    return sortedGenomes, sortedFitnessValues

def main():

	#Number of individuals
	N = 200
	#Number of generations
	G = 500
	strategy =[]

	#Creating the initial population
	initial_population =[]
	for j in range(0, N):
		for i in range(0,243):
			strategy.append(str(random.randint(0,6)))
		initial_population.append(strategy)
		strategy = []
    
	#Calculate sum of the series 1, 2,... 200.
	sumofranks = (N+1)*N/2
	prob_list = []
	#Calculating the probability of choosing an individual based on rank. Rank 1 is stored at position 0 in the list.
	for i in range (0, N):
		prob_list.append((i+1)/sumofranks)


	for k in range(0, G):		
		#Create a new population based on the previous generation
		new_population = []
		x, y = sortByFitness(initial_population)
		#Creating the new population
		for i in range(0, 100):
			#Choosing new parents based on linear rank selection
			choice1, choice2 = random.choices(x, weights=prob_list, k=2)
			#Single point crossover
			#Choosing a crossover point
			point = randrange(0, 242)
			#Creating 2 new individuals
			new_genome1 = choice1[point:] + choice2[:point]
			new_genome2 = choice2[point:] + choice1[:point]

			#Mutation with rate 0.0005
			for j in range(0,243):

				probability_mutation1 = random.random()
				if(probability_mutation1<=0.0005):
					new_genome1[j] = str(randrange(0, 6))

				probability_mutation2 = random.random()
				if(probability_mutation2<=0.0005):
					new_genome2[j] = str(randrange(0, 6))
			#Adding to the genomes to the new population
			new_population.append(new_genome1)
			new_population.append(new_genome2)
		#Calculating the average fitness value of the parent population (stored in initial_population)
		average_fitnessvalue=0
		for i in range(0,200):
			average_fitnessvalue = average_fitnessvalue+y[i]
		print(k, '\t', average_fitnessvalue/200)
		initial_population = new_population
		#Storing the generation number, average fitness value of the population, best strategy of the population and the fitness value of the best
		#strategy of the population in the file GAoutput.txt.
		if((k+1)%10 == 0):
			with open("GAoutput.txt","a") as variable_name:
				data_to_write = str(j) + " " + str(average_fitnessvalue) + " " + str(y[199])+ " "+str(x[199])+"\n"
				variable_name.write(data_to_write)



if __name__ == "__main__":
    main()

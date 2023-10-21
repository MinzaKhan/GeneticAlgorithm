# GeneticAlgorithm
Implemented a genetic algorithm to evolve control strategies for Robby the Robot, as described in Chapter 9 of Complexity: A Guided Tour by Melanie Mitchell. 

To run the code, download the file robby.zip Download robby.zipand unzip it. This will create a folder named robby. Put this folder in the same location as the Python program robby.py. IMPORTANT: do not put the Python file or any other files inside the folder; just make sure the folder is in the same location as the program file. You should not modify any of the code in this folder. 

A control strategy is represented as a string of characters that code for the following robot actions:

0 = MoveNorth
1 = MoveSouth
2 = MoveEast
3 = MoveWest
4 = StayPut
5 = PickUpCan
6 = MoveRandom

The Genetic Algorithm maintains a population of genomes representing control strategies. Each genome is a 243-character string specifying the action that Robby should take for every possible situation he might find himself in. Robby's "situation" is encoded as a 5-character percept string specifying what Robby currently sees in his immediate vicinity. For example, the string 'WECWC' means there is a wall to the north, an empty grid cell to the south, a soda can to the east, another wall to the west, and a soda can in Robby's own grid cell. Each percept string corresponds to a unique code number in the range 0-242, which indicates the (0-based) index number of the situation. 

The job of the Genetic Algorithm is to evolve a good control strategy that maximizes Robby's average cumulative reward as he collects empty soda cans for 200 time steps. I have used rank selection for selecting genomes for mutation. The crossover rate is 1.0. The mutation rate is 0.0005 per locus. 

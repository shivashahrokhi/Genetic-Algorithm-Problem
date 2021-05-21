import random

class Genetic:
    #Get an object of game to apply genetic algorithm to each levels
    def __init__(self, game):

        self.game = game
        #A list for saving current population at any state of the algorithm
        self.population = []
        #A list for saving score of each chromosome in current population
        self.scores = []
        #A list for saving average score of each population
        self.average_scores = []

    #Generate initilize population randomly with more chance for zeros in each chromosom
    def initilize_population(self):
        for i in range(200):
            chromosome = ""
            for j in range(len(self.game.current_level_len)):
                random_number = random.randint(0,3)
                chromosome.append(str(random_number%3))
            self.population.append(chromosome)

    #Calculate the averge score of current population 
    def calculate_averae_score(self):
        sum = 0
        for chromosome in self.population:
            sum += self.game.get_score(chromosome)
        average = sum/(len(self.population))
        self.average_scores.append(average)
        return average
        
    #Select some chromosome to pass for crossover level  
    def selection(self):
        pass

    def crossover(self):
        pass

    def mutation(self):
        pass

    def GA(self):

        self.initilized_population()
        last_average_score = self.calculate_averae_score()
        self.selection()
        self.crossover()
        self.mutation()
        new_average_score = self.calculate_averae_score()
#####here we need to hanle the situation thet algorithm gets stuck in the local optimums
        while last_average_score - new_average_score > 0.000000001:
            last_average_score = new_average_score
            self.selection()
            self.crossover()
            self.mutation()
            new_average_score = self.calculate_averae_score()
        
        return max(self.scores)

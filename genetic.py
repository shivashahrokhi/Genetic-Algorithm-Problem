import random


class Genetic:
    # Get an object of game to apply genetic algorithm to each levels
    def __init__(self, game):

        self.game = game
        # A list for saving current population at any state of the algorithm
        self.population = []
        # A list for saving score of each chromosome in current population
        self.scores = []
        # A list for saving average score of each population
        self.average_scores = []

    # Generate initialise population randomly with more chance for zeros in each chromosome
    def initialise_population(self):
        for i in range(200):
            chromosome = ""
            for j in range(self.game.current_level_len):
                random_number = random.randint(0, 3)
                chromosome += (str(random_number % 3))
            self.population.append(chromosome)

    def initialize_scores(self):
        for chromosome in self.population:
            self.scores.append(self.game.get_score(chromosome))

    # Calculate the score of each chromosome
    def update_scores(self):
        for i in range(len(self.population)):
            self.scores[i] = self.game.get_score(self.population[i])

    # Calculate the average score of current population
    def calculate_average_score(self):
        average = sum(self.scores) / (len(self.population))
        self.average_scores.append(average)
        return average

    # Select some chromosome to pass for crossover level randomly
    # and update the population with better chromosome
    def selection(self):
        self.population = random.choices(self.population, weights=tuple(self.scores), k=len(self.population))
        self.update_scores()

    # One point crossover
    # warning: length of population should be even
    def crossover(self):
        new_population = []
        while len(self.population) != 0:
            parent_one = self.population.pop(random.randint(0, len(self.population) - 1))
            parent_two = self.population.pop(random.randint(0, len(self.population) - 1))
            random_number = random.randint(0, self.game.current_level_len - 1)
            child_one = parent_one[:random_number] + parent_two[random_number:]
            child_two = parent_two[:random_number] + parent_one[random_number:]
            new_population.append(child_one)
            new_population.append(child_two)
        self.population = new_population

    # Change one random gene of each chromosome to zero
    def mutation(self):
        for chromosome in self.population:
            random_number = random.randint(0, len(chromosome) - 1)
            if chromosome[random_number] != 0:
                new_chromosome = chromosome[:random_number - 1] + "0" + chromosome[random_number + 1:]
                self.population.remove(chromosome)
                self.population.append(new_chromosome)

    def ga(self):

        self.initialise_population()
        self.initialize_scores()
        last_average_score = self.calculate_average_score()
        self.selection()
        self.crossover()
        self.mutation()
        self.update_scores()
        new_average_score = self.calculate_average_score()
        # here we need to handle the situation the algorithm gets stuck in the local optimums
        while abs(last_average_score - new_average_score) > 0.0000000000001:
            last_average_score = new_average_score
            self.selection()
            self.crossover()
            self.mutation()
            self.update_scores()
            new_average_score = self.calculate_average_score()

        return max(self.scores)

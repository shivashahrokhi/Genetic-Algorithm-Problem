import random


class Genetic:
    def __init__(self, game):
        """
        Initialises this class
        :param game: An object of game to apply genetic algorithm to each levels
        """
        self.game = game
        # A list for saving current population at any state of the algorithm
        self.population = []
        # A list for saving score of each chromosome in current population
        self.scores = []
        # A list for saving average score of each population
        self.average_scores = []
        # A parameter determining the population size of
        self.population_size = 200

    def initialise_population(self):
        """
        Generate the initial population randomly with more chance for zeros in each chromosome
        """
        self.population = []
        for i in range(self.population_size):
            chromosome = ""
            for j in range(self.game.current_level_len):
                random_number = random.randint(0, 3) % 3
                chromosome += (str(random_number))
            self.population.append(chromosome)

    def initialise_scores(self):
        self.average_scores = []
        self.scores = []
        for chromosome in self.population:
            self.scores.append(self.game.get_score(chromosome))

    def update_scores(self):
        """
        Calculate the score of each chromosome
        """
        for i in range(len(self.population)):
            self.scores[i] = self.game.get_score(self.population[i])

    def calculate_average_score(self):
        """
        Calculate the average score of current population
        :return: A float containing the average score of the current generation
        """
        average = sum(self.scores) / (len(self.population))
        self.average_scores.append(average)
        return average

    def selection(self):
        """
        Select some chromosome to pass for crossover level randomly
        and update the population with better chromosome
        """
        self.population = random.choices(self.population, weights=tuple(self.scores), k=len(self.population))
        self.update_scores()

    def crossover(self):
        """
        Performs one point crossover
        warning: length of population should be even
        """
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

    def mutation(self):
        """
        Change one random gene of each chromosome to zero
        """
        for chromosome in self.population:
            random_number = random.randint(0, len(chromosome) - 1)
            random_char_number = random.randint(0, 3) % 3
            mutation_string = str(random_char_number)
            new_chromosome = chromosome[:random_number] + mutation_string + chromosome[random_number + 1:]
            self.population.remove(chromosome)
            self.population.append(new_chromosome)

    def ga(self):
        self.initialise_population()
        self.initialise_scores()
        last_average_score = self.calculate_average_score()
        self.selection()
        self.crossover()
        self.mutation()
        self.update_scores()
        new_average_score = self.calculate_average_score()
        # Here we need to handle the situation the algorithm gets stuck in the local optimums
        generation_number = 0
        while abs(last_average_score - new_average_score) > 0.000001 and generation_number < 3000:
            last_average_score = new_average_score
            self.selection()
            self.crossover()
            self.mutation()
            self.update_scores()
            new_average_score = self.calculate_average_score()
            generation_number += 1
        return self.average_scores

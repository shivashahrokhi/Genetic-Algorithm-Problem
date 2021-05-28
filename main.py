from game import Game
from genetic import Genetic


def main():
    levels = list(input().split())
    game = Game(levels)
    genetic = Genetic(game)
    for i in range(len(levels)):
        game.load_next_level()
        game.initialise_solutions()
        genetic.ga()
        if game.max_solutions_rating[i] == -1:
            print("No solution was found for level", i)
        else:
            print("Level", i)
            print("Best solution:", game.level_solutions[i])
            print("Rating:", game.max_solutions_rating[i])


if __name__ == '__main__':
    main()

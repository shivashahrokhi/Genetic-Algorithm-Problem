from game import Game
from genetic import Genetic
from matplotlib import pyplot as plotter
from matplotlib import style


def main():
    style.use('dark_background')
    levels = list(input().split())
    game = Game(levels)
    genetic = Genetic(game)
    for i in range(len(levels)):
        print("Working on level " + str(i + 1) + "...")
        game.load_next_level()
        game.initialise_solutions()
        average_scores = genetic.ga()
        if game.max_solutions_rating[i] == -1:
            print("No solution was found for level " + str(i))
        else:
            print("Level " + str(i))
            print("Best solution: " + game.level_solutions[i])
            print("Rating: " + str(game.max_solutions_rating[i]))
        title = "Average Scores for level " + str(i + 1) + "    Level:" + game.levels[i]
        plotter.title(title)
        plotter.plot(average_scores)
        plotter.show()


if __name__ == '__main__':
    main()

from game import Game
from genetic import Genetic


def main():
    levels = list(input().split())
    game = Game(levels)
    genetic = Genetic(game)
    for i in range(len(levels)):
        game.load_next_level()
        print(genetic.ga())


if __name__ == '__main__':
    main()

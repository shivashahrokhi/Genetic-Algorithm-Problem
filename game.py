class Game:
    def __init__(self, levels):
        """
        Initialises this class
        Gets a list of strings as levels.
        :param levels: A list of strings as levels
        """
        self.levels = levels
        self.level_solutions = []
        self.max_solutions_rating = []
        self.current_level_index = -1
        self.current_level_len = 0

    def initialise_solutions(self):
        for i in range(len(self.levels)):
            self.level_solutions.append("")
            self.max_solutions_rating.append(-1)

    def load_next_level(self):
        self.current_level_index += 1
        self.current_level_len = len(self.levels[self.current_level_index])

    def get_steps(self, actions):
        """
        Gets an action sequence and returns maximum steps that can be passed without lost.
        :param actions: A string representing the sequence of actions taken.
        :return: An integer denoting the maximum steps.
        """
        lengths = []
        current_level = self.levels[self.current_level_index]
        start = 0
        end = 0
        if current_level[0] != "_" and current_level[0] != "M":
            lengths.append(0)
            start = 1
            end = 1
        while end != self.current_level_len:
            current_step = current_level[end]
            if current_step == '_' or current_step == 'M' or (current_step == 'G' and (actions[end - 1] == '1' or
                (end > 1 and actions[end - 2] == '1'))) or (current_step == 'L' and actions[end - 1] == '2'):
                end += 1
            else:
                lengths.append(end - start)
                end += 1
                start = end
        if end == self.current_level_len and current_level[self.current_level_len - 1]:
            lengths.append(end - start)
        max_length = max(lengths)
        return max_length, max_length == self.current_level_len

    def get_additional_points(self, actions):
        """
        Rates each solution based on the criteria of mushrooms collected, enemies killed
        and if the agent jumps in the last place
        :param actions: A string of actions the agent takes
        :return: A float having the overall points
        """
        current_level = self.levels[self.current_level_index]
        location = 0
        additional_rating = 0
        if current_level[location] == 'M':
            additional_rating += 1
            location += 1
        while location != self.current_level_len:
            if current_level[location] == 'M' and location > 0 and actions[location - 1] != '1':
                additional_rating += 2
            if current_level[location] == 'G' and location > 1 and actions[location - 2] == '1':
                additional_rating += 2.25
            if actions[location] == '1':
                additional_rating -= 0.25
            location += 1
        if actions[self.current_level_len - 1] == '1':
            additional_rating += 2.25
        return additional_rating

    def get_score(self, actions):
        """
        Get an action sequence and determine the steps taken/score
        :param actions: A string denoting the actions the agent takes
        :return: The score of this action if it was taken as a solution
        """
        max_steps, level_pass = self.get_steps(actions)
        additional_points = self.get_additional_points(actions)
        overall_score = max_steps + additional_points + (5 if level_pass else 0)
        if level_pass:
            if self.max_solutions_rating[self.current_level_index] == -1:
                self.level_solutions[self.current_level_index] = actions
                self.max_solutions_rating[self.current_level_index] = overall_score
            elif self.max_solutions_rating[self.current_level_index] < overall_score:
                self.level_solutions[self.current_level_index] = actions
                self.max_solutions_rating[self.current_level_index] = overall_score
        return overall_score

class Game:
    def __init__(self, levels):
        # Get a list of strings as levels
        # Store level length to determine if a sequence of action passes all the steps

        self.levels = levels
        self.current_level_index = -1
        self.current_level_len = 0

    def load_next_level(self):
        self.current_level_index += 1
        self.current_level_len = len(self.levels[self.current_level_index])

    # Get an action sequence and returns maximum steps that can be passed without lost
    def get_steps(self, actions):
        lengths = []
        current_level = self.levels[self.current_level_index]
        start = 0
        end = 0
        if current_level[0] != "_":
            lengths.append(0)
            start = 1
            end = 1
        while end != self.current_level_len:
            current_step = current_level[end]
            if current_step == '_' or current_step == 'M' or (current_step == 'G' and (actions[end - 1] == '1' or actions[end - 2] == '1'))\
                    or (current_step == 'L' and actions[end - 1] == '2'):
                end += 1
            else:
                lengths.append(end - start)
                end += 1
                start = end
        if end == self.current_level_len and current_level[self.current_level_len - 1]:
            lengths.append(end - start)
        max_length = max(lengths)
        return max_length, max_length == self.current_level_len

    # Get an action sequence and returns additional ratings
    def get_additional_points(self, actions):
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

    # It need to change a lot
    def get_score(self, actions):
        # Get an action sequence and determine the steps taken/score
        # Return a tuple, the first one indicates if these actions result in victory
        # and the second one shows the steps taken
        max_steps, level_pass = self.get_steps(actions)
        additional_points = self.get_additional_points(actions)
        return max_steps + additional_points + (5 if level_pass else 0)

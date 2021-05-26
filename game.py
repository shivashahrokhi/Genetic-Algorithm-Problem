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
    def get_steps(self,actions):

        lengths = []
        current_level = self.levels[self.current_level_index]
        start = 0
        end = 0
        if current_level[0] != "_":
            lengths.append(0)
            start = 1
            end = 1
        while end != self.current_level_len - 1:
            current_step = current_level[end]
            if current_step == '_' or (current_step == 'G' and actions[end - 1] == '1') or (current_step == 'L' and actions[end - 1] == '2'):
                end += 1
            else:
                lengths.append(end - start)
                end += 1
                start = end
        if end == self.current_level_len - 1 and current_level[self.current_level_len - 1]:
            lengths.append(end - start)

        return max(lengths)

    # It need to change a lot
    def get_score(self, actions):
        # Get an action sequence and determine the steps taken/score
        # Return a tuple, the first one indicates if these actions result in victory
        # and the second one shows the steps taken

        current_level = self.levels[self.current_level_index]
        steps = 0
        for i in range(self.current_level_len - 1):
            current_step = current_level[i]
            if current_step == '_':
                steps += 1
            elif current_step == 'G' and actions[i - 1] == '1':
                steps += 1
            elif current_step == 'L' and actions[i - 1] == '2':
                steps += 1
            else:
                break
        return steps == self.current_level_len - 1, steps

import random


class Participant:
    def __init__(self, nrPreferences, nrProjects):
        self.nrPreferences = nrPreferences
        self.nrProjects = nrProjects

        self.preferences = []
        self.project = 0
        self.score = 0

    def generate_preferences(self):
        while len(self.preferences) < self.nrPreferences:
            tmp = random.randrange(0, self.nrProjects, 1)
            if tmp not in self.preferences:
                self.preferences.append(tmp)
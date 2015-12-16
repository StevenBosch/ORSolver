'''
The problem is the following:
Given a number of projects with limited available places, distribute a number of participants over those projects,
using their preferences for project placement.
'''

import random
import participant as part
import project as proj


# Recursively
def solve_rec(nrParticipants):
    # Base case
    if nrParticipants == 1:
        pass

    for participant in range(0, nrParticipants):
        return solve_rec(nrParticipants-1)


# Iteratively
def solve(projectMax, projects, nrParticipants, preferences):
    distribution = [0] * 5
    score = 0

    for i in range(0, nrParticipants):
        for j in range(0, len(projects)):
            if projects[preferences[i][j]] < projectMax[preferences[i][j]]:
                projects[preferences[i][j]] += 1
                # distribution[i] = preferences[i][j]
                score += len(projects) - j
                break

    print(projects)
    print(score)
    return distribution

if __name__ == "__main__":
    # Parameters
    nrProjects = 5
    nrParticipants = 13
    nrPreferences = 3

    projects = [proj.Project(5)] * nrProjects
    participants = [part.Participant(nrPreferences, nrProjects)] * nrParticipants
    for participant in participants:
        participant.generate_preferences()


    # distribution = solve(projectMax, projects, nrParticipants, preferences)

from constraint import *


def free_that_time(S, M, P, Time):
    simona_free = (13, 14, 16, 19)
    marija_free = (14, 15, 18)
    petar_free = (12, 13, 16, 17, 18, 19)

    if S == 1 and Time in simona_free:
        if M == 1 and Time in marija_free:
            if P == 1 and Time in petar_free:
                return True
            elif P == 0:
                return True
        else:
            if P == 1 and Time in petar_free:
                if M == 0:
                    return True

    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    domain = [i for i in range(12, 21)]

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Simona_prisustvo", [1, ])
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", domain)

    variables = ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"]
    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(free_that_time, variables)
    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]

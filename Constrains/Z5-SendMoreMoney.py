from constraint import *


def equession(S, E, N, D, M, O, R, Y):
    if D + E != Y:
        if D + E > 9:
            if (D + E) % 10 != Y:
                return False
        else:
            return False

    ostatok = int((D + E) / 10)

    if N + R + ostatok != E:
        if N + R + ostatok > 9:
            if (N + R + ostatok) % 10 != E:
                return False
        else:
            return False

    ostatok = int((N + R + ostatok)/10)

    if E + O + ostatok != N:
        if E + O + ostatok > 9:
            if (E + O + ostatok) % 10 != N:
                return False
        else:
            return False

    ostatok = int((E + O + ostatok) / 10)

    if S + M + ostatok != O:
        if S + M + ostatok > 9:
            if (S + M + ostatok) % 10 != O:
                return False
        else:
            return False
    ostatok = int((S + M + ostatok) / 10)

    if ostatok != M:
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(equession, variables)
    # ----------------------------------------------------

    print(problem.getSolution())
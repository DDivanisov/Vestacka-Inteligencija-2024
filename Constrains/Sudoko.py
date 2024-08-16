from constraint import *

def printD(res):
    rez = dict(sorted(res.items()))
    for i in [1, 5, 9, 13]:
        print(str(i) + ":" + str(rez[i]) + " " + str(i + 1) + ":" + str(rez[i + 1]) + " " + str(i + 2) + ":" + str(
            rez[i + 2]) + " " + str(i + 3) + ":" + str(rez[i + 3]))


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = [i for i in range(1, 17)]
    domain = [i for i in range(1, 5)]

    for variable in variables:
        problem.addVariable(variable, domain)

    for i in range(1, 5):
        problem.addConstraint(AllDifferentConstraint(), [i, i + 4, i + 8, i + 12])

    for i in [1, 5, 9, 13]:
        problem.addConstraint(AllDifferentConstraint(), [i, i + 1, i + 2, i + 3])

    for i in [1, 3, 9, 11]:
        problem.addConstraint(AllDifferentConstraint(), [i, i + 1, i + 4, i + 5])

    printD(problem.getSolution())

from constraint import *


# kukurasu game
def printD(res):
    rez = dict(sorted(res.items()))
    for i in [1, 5, 9, 13]:
        print(str(i) + ":" + str(rez[i]) + " " + str(i + 1) + ":" + str(rez[i + 1]) + " " + str(i + 2) + ":" + str(
            rez[i + 2]) + " " + str(i + 3) + ":" + str(rez[i + 3]))


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = [(i, j) for i in range(1, 5) for j in range(1, 5)]

    # print(vars)

    domain = [0, 1]
    problem.addVariables(variables, domain)
    # constraints
    row_sums = [7, 7, 4, 5]
    col_sums = [1, 2, 12, 8]
    j = 0
    for col in range(1,5):
        col_vars = [(row, col) for row in range(1, 5)]
        problem.addConstraint(ExactSumConstraint(1), col_vars)

    solution = problem.getSolution()
    print(solution)

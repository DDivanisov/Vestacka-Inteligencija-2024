from constraint import *


def num_papers_per_term(*args):
    T1, T2, T3 = 0, 0, 0
    T4 = 0
    for paper in args:
        if paper == "T1":
            T1 += 1
        if paper == "T2":
            T2 += 1
        if paper == "T3":
            T3 += 1
        if paper == "T4":
            T4 += 1
    if T1 > 4 or T2 > 4 or T3 > 4 or T4 > 4:
        return False
    return True


def print_function(rez, var):
    for v in var:
        print(v + ": " + rez[v])


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Дефинирање на термините
    terms = [f'T{i + 1}' for i in range(num)]

    # Дефинирање на променливите (трудовите) и нивните домени
    variables = []
    variables_AI = []
    variables_ML = []
    variables_NLP = []

    for key in papers.keys():
        variables.append(key + " (" + papers[key] + ")")
        if papers[key] == "AI":
            variables_AI.append(key + " (" + papers[key] + ")")
        if papers[key] == "ML":
            variables_ML.append(key + " (" + papers[key] + ")")
        if papers[key] == "NLP":
            variables_NLP.append(key + " (" + papers[key] + ")")

    domain = terms

    problem = Problem(BacktrackingSolver())

    # Додавање на променливите и нивните домени
    problem.addVariables(variables, domain)

    # Ограничувања
    problem.addConstraint(num_papers_per_term, variables)

    if 4 >= variables_AI.__len__() > 0:
        problem.addConstraint(AllEqualConstraint(), variables_AI)
    if 4 >= variables_ML.__len__() > 0:
        problem.addConstraint(AllEqualConstraint(), variables_ML)
    if 4 >= variables_NLP.__len__() > 0:
        problem.addConstraint(AllEqualConstraint(), variables_NLP)
    result = problem.getSolution()

    # Печатење на резултатот
    print_function(result, variables)

from constraint import *


def diffHoursML(*vars):
    for i in range(vars.__len__()):
        for j in range(vars.__len__()):
            if i != j:
                h1 = int(vars[i].split("_")[1])
                h2 = int(vars[j].split("_")[1])
                if h1 == h2:
                    return False
    return True


def diff(*vars):
    for i in range(vars.__len__()):
        for j in range(vars.__len__()):
            if i != j:
                h1 = int(vars[i].split("_")[1])
                h2 = int(vars[j].split("_")[1])
                d1 = vars[i].split("_")[0]
                d2 = vars[j].split("_")[0]
                if d1 == d2:
                    if abs(h1 - h2) < 2:
                        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    variables = []
    variablesML = []
    # ---Tuka dodadete gi promenlivite--------------------
    for i in range(0, int(casovi_AI)):
        variables.append("AI_cas_" + str(i + 1))
        problem.addVariable("AI_cas_" + str(i + 1), AI_predavanja_domain)

    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    variables.append("AI_vezbi")

    for i in range(0, int(casovi_ML)):
        variables.append("ML_cas_" + str(i + 1))
        variablesML.append("ML_cas_" + str(i + 1))
        problem.addVariable("ML_cas_" + str(i + 1), ML_predavanja_domain)

    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    variables.append("ML_vezbi")
    variablesML.append("ML_vezbi")

    for i in range(0, int(casovi_R)):
        variables.append("R_cas_" + str(i + 1))
        problem.addVariable("R_cas_" + str(i + 1), R_predavanja_domain)

    for i in range(0, int(casovi_BI)):
        variables.append("BI_cas_" + str(i + 1))
        problem.addVariable("BI_cas_" + str(i + 1), BI_predavanja_domain)

    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    variables.append("BI_vezbi")

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(diff, variables)
    problem.addConstraint(diffHoursML, variablesML)
    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)

# {'ML_vezbi': 'Thu_14', 'ML_cas_1': 'Fri_15', 'BI_vezbi': 'Thu_11'
# , 'AI_vezbi': 'Tue_13', 'AI_cas_1': 'Fri_12', 'BI_cas_1': 'Fri_10', 'R_cas_1': 'Wed_15'}

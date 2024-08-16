from searching_framework import Problem, astar_search


class Labyrinth(Problem):

    def __init__(self, initial, _walls, _area, goal=None):
        super().__init__(initial, goal)
        self.walls = _walls
        self.area = _area

    def goal_test(self, state):
        return state[0] == state[1]

    def successor(self, state):
        possibility = {}

        person = state[0]
        house = state[1]

        new_person = move_up(person, self.walls, self.area)
        if new_person != person:
            possibility["Gore"] = (new_person, house)

        new_person = move_down(person, self.walls, self.area)
        if new_person != person:
            possibility["Dolu"] = (new_person, house)

        new_person = move_left(person, self.walls, self.area)
        if new_person != person:
            possibility["Levo"] = (new_person, house)

        new_person = move_right_n(person, self.walls, self.area, int(2))
        if new_person != person:
            possibility["Desno 2"] = (new_person, house)

        new_person = move_right_n(person, self.walls, self.area, int(3))
        if new_person != person:
            possibility["Desno 3"] = (new_person, house)

        return possibility

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        sum = 0
        sum = sum + mhd(node.state[0], node.state[1])
        return sum


def mhd(one, two):
    x1, y1 = one
    x2, y2 = two

    return max(abs(x1 - x2), abs(y1 - y2))/3


def move_up(person, walls, area):
    new_person = (person[0], person[1] + 1)

    if is_valid(new_person, walls, area):
        return new_person
    return person


def move_right_n(person, walls, area, n):
    new_person = (person[0] + 1, person[1])

    if is_valid(new_person, walls, area):
        new_person = (person[0] + 2, person[1])
        if is_valid(new_person, walls, area):
            if n == 2:
                return new_person
            else:
                new_person = (person[0] + 3, person[1])
                if is_valid(new_person, walls, area):
                    return new_person
    return person


def move_left(person, walls, area):
    new_person = (person[0] - 1, person[1])

    if is_valid(new_person, walls, area):
        return new_person
    return person


def move_down(person, walls, area):
    new_person = (person[0], person[1] - 1)

    if is_valid(new_person, walls, area):
        return new_person
    return person


def is_valid(person, walls, area):
    if person not in walls and person in area:
        return True
    return False


if __name__ == '__main__':

    n = int(input())
    area = [(i, j) for i in range(n) for j in range(n)]

    wall_num = int(input())
    walls = []
    for i in range(wall_num):
        wall = input().split(",")
        wall = (int(wall[0]), int(wall[1]))
        walls.append(wall)

    person = input().split(",")
    house = input().split(",")

    person = (int(person[0]), int(person[1]))
    house = (int(house[0]), int(house[1]))

    labyrinth = Labyrinth((person, house), walls, area)
    _node = astar_search(labyrinth)
    if _node is not None:
        print(_node.solution())

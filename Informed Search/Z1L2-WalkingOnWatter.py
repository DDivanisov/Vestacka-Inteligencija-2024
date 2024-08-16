from searching_framework import Problem, astar_search


class WalkingOnWater(Problem):

    def __init__(self, initial, _allowed, goal=None):
        super().__init__(initial, goal)
        self.allowed = _allowed

    def goal_test(self, state):
        return state[0] == state[1]

    def successor(self, state):
        possibility = {}

        person = state[0]
        house = state[1]
        _direction = state[2]

        new_state = wait(person, house, _direction)
        possibility["Stoj"] = new_state

        new_state = move_up_n(person, house, _direction, self.allowed, int(1))
        if new_state[0] != person:
            possibility["Gore 1"] = new_state

        new_state = move_up_n(person, house, _direction, self.allowed, int(2))
        if new_state[0] != person:
            possibility["Gore 2"] = new_state

        new_state = move_up_right_n(person, house, _direction, self.allowed, int(1))
        if new_state[0] != person:
            possibility["Gore-desno 1"] = new_state

        new_state = move_up_right_n(person, house, _direction, self.allowed, int(2))
        if new_state[0] != person:
            possibility["Gore-desno 2"] = new_state

        new_state = move_up_left_n(person, house, _direction, self.allowed, int(1))
        if new_state[0] != person:
            possibility["Gore-levo 1"] = new_state

        new_state = move_up_left_n(person, house, _direction, self.allowed, int(2))
        if new_state[0] != person:
            possibility["Gore-levo 2"] = new_state

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

    return (y2 - y1)/2


def wait(person, house, _direction):
    new_house = move_houes(house, _direction)[0]
    new_direction = move_houes(house, _direction)[1]
    new_state = (person, new_house, new_direction)
    return new_state


def move_up_n(person, house, _direction, _allowed, n):
    new_person = (person[0], person[1] + n)
    same_state = (person, house, _direction)
    new_house = move_houes(house, _direction)[0]
    new_direction = move_houes(house, _direction)[1]

    if is_valid(new_person, _allowed, new_house):
        new_state = (new_person, new_house, new_direction)
        return new_state
    return same_state


def move_up_right_n(person, house, _direction, _allowed, n):
    new_person = (person[0] + n, person[1] + n)
    same_state = (person, house, _direction)
    new_house = move_houes(house, _direction)[0]
    new_direction = move_houes(house, _direction)[1]

    if is_valid(new_person, _allowed, new_house):
        new_state = (new_person, new_house, new_direction)
        return new_state
    return same_state


def move_up_left_n(person, house, _direction, _allowed, n):
    new_person = (person[0] - n, person[1] + n)
    same_state = (person, house, _direction)
    new_house = move_houes(house, _direction)[0]
    new_direction = move_houes(house, _direction)[1]

    if is_valid(new_person, _allowed, new_house):
        new_state = (new_person, new_house, new_direction)
        return new_state
    return same_state


def is_valid(person, _allowed, house):
    area = [(i, j) for i in range(5) for j in range(9)]
    if person in _allowed or person == house:
        if person in area:
            return True
    return False


def move_houes(house, _direction):
    if _direction == "desno":
        if house == (4, 8):
            new_direction = "levo"
            new_house = (house[0] - 1, house[1])
            house_state = (new_house, new_direction)
            return house_state
        else:
            new_house = (house[0] + 1, house[1])
            house_state = (new_house, _direction)
            return house_state
    else:
        if house == (0, 8):
            new_direction = "desno"
            new_house = (house[0] + 1, house[1])
            house_state = (new_house, new_direction)
            return house_state
        else:
            new_house = (house[0] - 1, house[1])
            house_state = (new_house, _direction)
            return house_state


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    position_person = input().split(",")
    position_house = input().split(",")
    direction = input()

    position_person = (int(position_person[0]), int(position_person[1]))
    position_house = (int(position_house[0]), int(position_house[1]))

    person_house = (position_person, position_house, direction)
    walkingonwaterproblem = WalkingOnWater(person_house, allowed)

    _node = astar_search(walkingonwaterproblem)
    if _node is not None:
        print(_node.solution())

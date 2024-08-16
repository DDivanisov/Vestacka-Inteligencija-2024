from searching_framework import *


class Boxes(Problem):
    def __init__(self, initial, N, boxes, goal=None):
        super().__init__(initial, goal)
        self.N = N
        self.boxes = boxes

    def successor(self, state):
        actions = {}
        man, boxess = state
        new_state = move_Up(man, boxess, self.N, self.boxes)
        if new_state != state:
            actions["Gore"] = new_state

        new_state = move_Right(man, boxess, self.N, self.boxes)
        if new_state != state:
            actions["Desno"] = new_state

        return actions

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        if state[1].__len__() == 0:
            return True
        return False


def move_Up(man, boxes, N, allBoxes):
    old_state = (man, boxes)
    new_man = (man[0], man[1] + 1)
    new_state = (new_man, boxes)
    if nearBox(new_man, boxes) is not None:
        nearboxes = nearBox(new_man, boxes)
        boxes = list(boxes)
        for box in nearboxes:
            boxes.remove(box)
        new_state = (new_man, tuple(boxes))
    if valid(man, allBoxes, N):
        return new_state
    return old_state


def move_Right(man, boxes, N, allBoxes):
    old_state = (man, boxes)
    new_man = (man[0] + 1, man[1])
    new_state = (new_man, boxes)
    if nearBox(new_man, boxes) is not None:
        nearboxes = nearBox(new_man, boxes)
        boxes = list(boxes)
        for box in nearboxes:
            boxes.remove(box)
        new_state = (new_man, tuple(boxes))
    if valid(man, allBoxes, N):
        return new_state
    return old_state


def valid(man, boxes, N):
    area = [(i, j) for i in range(N) for j in range(N)]
    if man in area:
        if man not in boxes:
            return True
    return False


def nearBox(man, boxes):
    nearbox = []
    for box in boxes:
        if box == (man[0] + 1, man[1] + 1) or box == (man[0] + 1, man[1]) or box == (man[0] + 1, man[1] - 1):
            nearbox.append(box)
        elif box == (man[0] - 1, man[1] + 1) or box == (man[0] - 1, man[1]) or box == (man[0] - 1, man[1] - 1):
            nearbox.append(box)
        elif box == (man[0], man[1] + 1) or box == (man[0], man[1] - 1):
            nearbox.append(box)

    if nearbox.__len__() == 0:
        return None
    return nearbox


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    boxes = []
    for i in range(M):
        line = input()
        split = line.split(",")
        boxes.append((int(split[0]), int(split[1])))
    boxes = tuple(boxes)
    state = ((0, 0), boxes)
    boxesProblem = Boxes(state, N, boxes)

    solution = breadth_first_graph_search(boxesProblem)

    if solution is not None:
        print(solution.solution())
    else:
        print("No Solution!")

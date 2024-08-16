from searching_framework import Problem, astar_search


class GhostOnSkates(Problem):
    def __init__(self, initial, walls, n, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.n = n

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(state, walls, n):
        area = [(i, j) for i in range(n) for j in range(n)]
        if state in area:
            if state not in walls:
                return True
        return False

    def successor(self, state):
        successors = dict()

        new_state = move_up_n(state, self.walls, self.n, 1)
        if new_state != state:
            successors["Gore 1"] = new_state

        new_state = move_up_n(state, self.walls, self.n, 2)
        if new_state != state:
            successors["Gore 2"] = new_state

        new_state = move_up_n(state, self.walls, self.n, 3)
        if new_state != state:
            successors["Gore 3"] = new_state

        new_state = move_right_n(state, self.walls, self.n, 1)
        if new_state != state:
            successors["Desno 1"] = new_state

        new_state = move_right_n(state, self.walls, self.n, 2)
        if new_state != state:
            successors["Desno 2"] = new_state

        new_state = move_right_n(state, self.walls, self.n, 3)
        if new_state != state:
            successors["Desno 3"] = new_state

        return successors

    def h(self, node):
        sum = 0

        sum = sum + (abs(node.state[0] - self.n - 1) + abs(node.state[1] - self.n - 1)) / 3

        return sum


def move_up_n(ghost, walls, area, n):
    new_state = (ghost[0], ghost[1] + n)
    if GhostOnSkates.check_valid(new_state, walls, area):
        return new_state
    return ghost


def move_right_n(ghost, walls, area, n):
    new_state = (ghost[0] + n, ghost[1])
    if GhostOnSkates.check_valid(new_state, walls, area):
        return new_state

    return ghost


if __name__ == '__main__':
    n = int(input())
    ghost_pos = (0, 0)
    goal_pos = (n - 1, n - 1)

    num_holes = int(input())
    holes = list()
    for _ in range(num_holes):
        holes.append(tuple(map(int, input().split(','))))

    problem = GhostOnSkates(ghost_pos, holes, n, goal_pos)
    solution = astar_search(problem)
    if problem is not None:
        print(solution.solution())

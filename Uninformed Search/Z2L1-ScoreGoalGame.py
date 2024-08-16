from searching_framework import Problem, breadth_first_graph_search


class ScoreGoal(Problem):
    def __init__(self, initial, opponent_area, goal_pos, goal=None):
        super().__init__(initial, goal)
        self.opponent_area = opponent_area
        self.goal_pos = goal_pos

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):

        return self.successor(state)[action]

    def goal_test(self, state):

        return state[1] in self.goal_pos

    def successor(self, state):
        possibility = {}
        player = state[0]
        ball = state[1]

        new_state = move_player_or_ball_up(player, ball, self.opponent_area, 0)
        if new_state[0] != state[0]:
            possibility["Pomesti coveche gore"] = new_state

        new_state = move_player_or_ball_down(player, ball, self.opponent_area, 0)
        if new_state != state:
            possibility["Pomesti coveche dolu"] = new_state

        new_state = move_player_or_ball_right(player, ball, self.opponent_area, 0)
        if new_state != state:
            possibility["Pomesti coveche desno"] = new_state

        new_state = move_player_or_ball_up_right(player, ball, self.opponent_area, 0)
        if new_state != state:
            possibility["Pomesti coveche gore-desno"] = new_state

        new_state = move_player_or_ball_down_right(player, ball, self.opponent_area, 0)
        if new_state != state:
            possibility["Pomesti coveche dolu-desno"] = new_state

        new_state = move_player_or_ball_up(player, ball, self.opponent_area, 1)
        if new_state != state:
            possibility["Turni topka gore"] = new_state

        new_state = move_player_or_ball_down(player, ball, self.opponent_area, 1)
        if new_state != state:
            possibility["Turni topka dolu"] = new_state

        new_state = move_player_or_ball_right(player, ball, self.opponent_area, 1)
        if new_state != state:
            possibility["Turni topka desno"] = new_state

        new_state = move_player_or_ball_up_right(player, ball, self.opponent_area, 1)
        if new_state != state:
            possibility["Turni topka gore-desno"] = new_state

        new_state = move_player_or_ball_down_right(player, ball, self.opponent_area, 1)
        if new_state != state:
            possibility["Turni topka dolu-desno"] = new_state

        return possibility


def move_player_or_ball_up(player, ball, opps, who):
    new_player = (player[0], player[1] + 1)
    if who == 0:
        if is_valid(new_player, ball, opps):
            new_state = (new_player, ball)
            return new_state
    else:
        new_ball = (ball[0], ball[1] + 1)
        if is_valid(new_player, new_ball, opps) and new_player == ball:
            new_state = (new_player, new_ball)
            return new_state
    old_state = (player, ball)
    return old_state


def move_player_or_ball_down(player, ball, opps, who):
    new_player = (player[0], player[1] - 1)
    if who == 0:
        if is_valid(new_player, ball, opps):
            new_state = (new_player, ball)
            return new_state
    else:
        new_ball = (ball[0], ball[1] - 1)
        if is_valid(new_player, new_ball, opps) and new_player == ball:
            new_state = (new_player, new_ball)
            return new_state
    old_state = (player, ball)
    return old_state


def move_player_or_ball_right(player, ball, opps, who):
    new_player = (player[0] + 1, player[1])
    if who == 0:
        if is_valid(new_player, ball, opps):
            new_state = (new_player, ball)
            return new_state
    else:
        new_ball = (ball[0] + 1, ball[1])
        if is_valid(new_player, new_ball, opps) and new_player == ball:
            new_state = (new_player, new_ball)
            return new_state
    old_state = (player, ball)
    return old_state


def move_player_or_ball_up_right(player, ball, opps, who):
    new_player = (player[0] + 1, player[1] + 1)
    if who == 0:
        if is_valid(new_player, ball, opps):
            new_state = (new_player, ball)
            return new_state
    else:
        new_ball = (ball[0] + 1, ball[1] + 1)
        if is_valid(new_player, new_ball, opps) and new_player == ball:
            new_state = (new_player, new_ball)
            return new_state
    old_state = (player, ball)
    return old_state


def move_player_or_ball_down_right(player, ball, opps, who):
    new_player = (player[0] + 1, player[1] - 1)
    if who == 0:
        if is_valid(new_player, ball, opps):
            new_state = (new_player, ball)
            return new_state
    else:
        new_ball = (ball[0] + 1, ball[1] - 1)
        if is_valid(new_player, new_ball, opps) and new_player == ball:
            new_state = (new_player, new_ball)
            return new_state
    old_state = (player, ball)
    return old_state


def is_valid(player, ball, opps_area):
    opps_pos = [(3, 3), (5, 4)]
    area = [(i, j) for i in range(8) for j in range(6)]

    if player in area and ball in area:
        if player not in opps_pos and ball not in opps_area:
            if player != ball:
                return True

    return False


if __name__ == '__main__':
    player_position = input().split(",")
    player_position = (int(player_position[0]), int(player_position[1]))

    ball_position = input().split(",")
    ball_position = (int(ball_position[0]), int(ball_position[1]))

    score_goal_problem = ScoreGoal((player_position, ball_position), (
        (2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3), (4, 4), (4, 5),
        (5, 3), (5, 4), (5, 5), (6, 3), (6, 4), (6, 5)), ((7, 2), (7, 3)))
    node = breadth_first_graph_search(score_goal_problem)
    if node is not None:
        print(node.solution())

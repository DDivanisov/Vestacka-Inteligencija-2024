from searching_framework import Problem, breadth_first_graph_search


class Snake(Problem):

    def __init__(self, initial, red_apples, goal=None):
        super().__init__(initial, goal)
        self.red_apples = red_apples

    def successor(self, state):
        possibility = dict()

        snake, green_apples, direction_snake = state

        new_state = self.keep_straight(snake, green_apples, self.red_apples, direction_snake)
        if new_state[0] is not snake:
            possibility['ProdolzhiPravo'] = new_state

        new_state = self.turn_left(snake, green_apples, self.red_apples, direction_snake)
        if new_state[0] is not snake:
            possibility['SvrtiLevo'] = new_state

        new_state = self.turn_right(snake, green_apples, self.red_apples, direction_snake)
        if new_state[0] is not snake:
            possibility['SvrtiDesno'] = new_state

        return possibility

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0



    @staticmethod
    def keep_straight(snake, green_apples, red_apples, direction_snake):
        head = snake[-1]
        if direction_snake == 'down':
            if head[1] - 1 >= 0 and (head[0], head[1] - 1) not in red_apples and (head[0], head[1] - 1) not in snake:
                snake = list(snake)
                snake.append((head[0], head[1] - 1))

                if (head[0], head[1] - 1) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)
        elif direction_snake == 'up':
            if head[1] + 1 < 10 and (head[0], head[1] + 1) not in red_apples and (head[0], head[1] + 1) not in snake:
                snake = list(snake)
                snake.append((head[0], head[1] + 1))

                if (head[0], head[1] + 1) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)
        elif direction_snake == 'right':
            if head[0] + 1 < 10 and (head[0] + 1, head[1]) not in red_apples and (head[0] + 1, head[1]) not in snake:
                snake = list(snake)
                snake.append((head[0] + 1, head[1]))

                if (head[0] + 1, head[1]) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)
        elif direction_snake == 'left':
            if head[0] - 1 >= 0 and (head[0] - 1, head[1]) not in red_apples and (head[0] - 1, head[1]) not in snake:
                snake = list(snake)
                snake.append((head[0] - 1, head[1]))

                if (head[0] - 1, head[1]) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)

        new_state = (snake, green_apples, direction_snake)
        return new_state

    @staticmethod
    def turn_left(snake, green_apples, red_apples, direction_snake):
        head = snake[-1]
        if direction_snake == 'left':
            if head[1] - 1 >= 0 and (head[0], head[1] - 1) not in red_apples and (head[0], head[1] - 1) not in snake:
                snake = list(snake)
                snake.append((head[0], head[1] - 1))

                if (head[0], head[1] - 1) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)
                direction_snake = 'down'
        elif direction_snake == 'right':
            if head[1] + 1 < 10 and (head[0], head[1] + 1) not in red_apples and (head[0], head[1] + 1) not in snake:
                snake = list(snake)
                snake.append((head[0], head[1] + 1))

                if (head[0], head[1] + 1) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)
                direction_snake = 'up'
        elif direction_snake == 'down':
            if head[0] + 1 < 10 and (head[0] + 1, head[1]) not in red_apples and (head[0] + 1, head[1]) not in snake:
                snake = list(snake)
                snake.append((head[0] + 1, head[1]))

                if (head[0] + 1, head[1]) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)
                direction_snake = 'right'
        elif direction_snake == 'up':
            if head[0] - 1 >= 0 and (head[0] - 1, head[1]) not in red_apples and (head[0] - 1, head[1]) not in snake:
                snake = list(snake)
                snake.append((head[0] - 1, head[1]))

                if (head[0] - 1, head[1]) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)
                direction_snake = 'left'

        new_state = (snake, green_apples, direction_snake)
        return new_state

    @staticmethod
    def turn_right(snake, green_apples, red_apples, direction_snake):
        head = snake[-1]
        if direction_snake == 'right':
            if head[1] - 1 >= 0 and (head[0], head[1] - 1) not in red_apples and (head[0], head[1] - 1) not in snake:
                snake = list(snake)
                snake.append((head[0], head[1] - 1))

                if (head[0], head[1] - 1) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)
                direction_snake = 'down'
        elif direction_snake == 'left':
            if head[1] + 1 < 10 and (head[0], head[1] + 1) not in red_apples and (head[0], head[1] + 1) not in snake:
                snake = list(snake)
                snake.append((head[0], head[1] + 1))

                if (head[0], head[1] + 1) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)
                direction_snake = 'up'
        elif direction_snake == 'up':
            if head[0] + 1 < 10 and (head[0] + 1, head[1]) not in red_apples and (head[0] + 1, head[1]) not in snake:
                snake = list(snake)
                snake.append((head[0] + 1, head[1]))

                if (head[0] + 1, head[1]) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)
                direction_snake = 'right'
        elif direction_snake == 'down':
            if head[0] - 1 >= 0 and (head[0] - 1, head[1]) not in red_apples and (head[0] - 1, head[1]) not in snake:
                snake = list(snake)
                snake.append((head[0] - 1, head[1]))

                if (head[0] - 1, head[1]) in green_apples:
                    green_apples = eat_apple(snake, green_apples)
                else:
                    snake = snake[1:]
                snake = tuple(snake)
                direction_snake = 'left'
        new_state = (snake, green_apples, direction_snake)
        return new_state


def eat_apple(snake, green_apples):
    green_apples = list(green_apples)
    green_apples = [x for x in green_apples if x not in snake]
    return tuple(green_apples)


if __name__ == '__main__':
    snake = ((0, 9), (0, 8), (0, 7))
    direction_snake = 'down'

    n = int(input())
    green_apples = []
    i = 0

    while i < n:
        apple = input().split(',')
        apple = [int(apple[0]), int(apple[1])]
        green_apples.append(tuple(apple))
        i += 1

    m = int(input())
    red_apples = []
    i = 0

    while i < m:
        apple = input().split(',')
        apple = [int(apple[0]), int(apple[1])]
        red_apples.append(tuple(apple))
        i += 1

    snake_problem = Snake((snake, tuple(green_apples), direction_snake), tuple(red_apples))
    node = breadth_first_graph_search(snake_problem)
    if node is not None:
        print(breadth_first_graph_search(snake_problem).solution())


import matplotlib.animation as animation
import matplotlib.pyplot as plt
from random import randint
from functools import wraps
import numpy as np
import time
import copy

SIZE = 128
GENERATIONS = 128
history = []
index = 0


def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"{func.__name__} has {time.time() - start} seconds execution time.")

    return wrapper


def generate_field():
    field = []
    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            row.append(randint(0, 1))
        field.append(row)
    return field


def get_neighbours_count(field, i, j):
    neighbours = 0

    for row in range(i - 1, i + 2):
        for column in range(j - 1, j + 2):
            if row != i or column != j:
                neighbours += field[row % SIZE][column % SIZE]

    return neighbours


def game_step(field, field_copy):
    for i in range(SIZE):
        for j in range(SIZE):
            neighbours = get_neighbours_count(field_copy, i, j)
            if neighbours == 3:
                field[i][j] = 1
            else:
                field[i][j] = min(int(neighbours == 2), field[i][j])


def game(field, field_copy):
    for _ in range(GENERATIONS):
        game_step(field, field_copy)


@execution_time
def python(field: list):
    field_copy = copy.deepcopy(field)
    game(field, field_copy)


@execution_time
def numpy(field: np.array):
    field_copy = np.array(field)
    game(field, field_copy)


def create_history(lst):
    for _ in range(GENERATIONS):
        history.append(copy.deepcopy(lst))
        game_step(lst, copy.deepcopy(lst))
    history.append(lst)


def animate(*args, **kwargs):
    global index
    plt.imshow(history[index])
    index += 1

    if index > GENERATIONS:
        exit(0)


def test():
    """
    Result: Using python array execution time lesser than using numpy array.
    """
    field = generate_field()
    python(copy.deepcopy(field))
    numpy(np.array(copy.deepcopy(field)))

    # animation
    create_history(field)
    fig = plt.figure()
    anim = animation.FuncAnimation(fig, animate, frames=GENERATIONS, interval=0)
    plt.show()


if __name__ == "__main__":
    test()

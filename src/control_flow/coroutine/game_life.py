'''
https://effectivepython.com/2015/03/10/consider-coroutines-to-run-many-functions-concurrently
'''
import collections

ALIVE = '*'
EMPTY = '-'

Query = collections.namedtuple('Query', ('y', 'x'))
Transition = collections.namedtuple('Transition', ('y', 'x', 'state'))


def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)  # North
    ne = yield Query(y + 1, x + 1)  # Northeast
    e_ = yield Query(y + 0, x + 1)
    se = yield Query(y - 1, x + 1)
    s_ = yield Query(y - 1, x + 0)
    sw = yield Query(y - 1, x - 1)
    w_ = yield Query(y + 0, x - 1)
    nw = yield Query(y + 1, x - 1)
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    print(count)
    return count


def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY     # Die: Too few
        elif neighbors > 3:
            return EMPTY     # Die: Too many
    else:
        if neighbors == 3:
            return ALIVE     # Regenerate
    return state


def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)


TICK = object()


def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK


class Grid:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def __str__(self):
        return str(self.rows)

    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state


def live_a_generation(grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)
    return progeny


class ColumnPrinter:
    def __init__(self):
        self.grids = []

    def append(self, grid):
        self.grids.append(grid)

    def __str__(self):
        return str(self.grids)


if __name__ == "__main__":
    columns = ColumnPrinter()
    grid = Grid(5, 9)
    ys = [0, 1, 2, 2, 2]
    xs = [3, 4, 2, 3, 4]
    for y, x in zip(ys, xs):
        grid.assign(y, x, ALIVE)
    sim = simulate(grid.height, grid.width)
    for _ in range(2):
        columns.append(str(grid))
        grid = live_a_generation(grid, sim)
    print(columns)

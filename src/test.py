from logic import Grid


def test_neighbours():
    print("test_neighbours")
    grid = Grid(4, [(0, 1), (1, 1), (2, 1)])
    print(grid.get_neighbours_states(1, 1))
    print(grid.get_neighbours_states(1, 0))
    print(grid.get_neighbours_states(2, 2))


def test_step():
    print("test_step")
    grid = Grid(4, [(0, 1), (1, 1), (2, 1)])
    print(grid)
    grid.step()
    print(grid)


def test_get_new_state():
    print("test_get_new_state")
    grid = Grid(4, [(0, 1), (1, 1), (2, 1)])
    print(grid)


def test_create_grid():
    grid = Grid(4)
    grid = Grid.create_grid_from_state(grid, 4, [(0, 1), (1, 1), (2, 1)])
    print(grid)


def run_tests():
    test_neighbours()
    test_step()
    test_create_grid()


if __name__ == "__main__":
    run_tests()

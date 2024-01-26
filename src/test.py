from logic import Grid


def test_neighbours():
    grid = Grid(4, [(0, 1), (1, 1), (2, 1)])
    assert grid.get_neighbours_states(1, 1) == [
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
    ], "test_neighbours_1"
    assert grid.get_neighbours_states(1, 0) == [
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        1,
    ], "test_neighbours_2"
    assert grid.get_neighbours_states(1, 1) == [
        1,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
    ], "test_neighbours_3"


def test_step():
    grid = Grid(4, [(0, 1), (1, 1), (2, 1)])
    assert grid.grid == [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ], "test_step_pre"
    grid.step()
    assert grid.grid == [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ], "test_step_post"


def test_get_new_state():
    print()
    grid = Grid(4, [(0, 1), (1, 1), (2, 1)])
    print(grid)
    # assert grid == , "test_get_new_state"


def test_create_grid():
    grid = Grid(4)
    grid = Grid.create_grid_from_state(grid, 4, [(0, 1), (1, 1), (2, 1)])
    assert grid == [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
    ], "test_create_grid"


def run_tests():
    test_neighbours()
    test_step()
    test_create_grid()


if __name__ == "__main__":
    run_tests()

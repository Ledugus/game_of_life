class Grid:
    def __init__(self, size, init_state=[]) -> None:
        self.size = size
        self.grid = self.create_grid(size, init_state)

    def create_grid(self, size, init_state):
        grid = []
        for _ in range(size):
            ligne = []
            for _ in range(size):
                ligne.append(0)
            grid.append(ligne)
        for x, y in init_state:
            grid[x][y] = 1
        return grid

    def get_square_value(self, x, y):
        return self.grid[x][y]

    def step(self):
        new_grid = self.grid[:]
        for x in range(self.size):
            for y in range(self.size):
                new_grid[x][y] = self.get_new_state(x, y)
        self.grid = new_grid

    def get_new_state(self, x, y):
        somme = sum(self.get_neighbours_states(x, y))
        if somme == 3:
            return 1
        if somme == 2:
            return self.grid[x][y]
        return 0

    def get_neighbours_states(self, x, y):
        neighbours = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        liste = []
        for rel_x, rel_y in neighbours:
            liste.append(self.grid[(x + rel_x) % self.size][(y + rel_y) % self.size])
        return liste

    def __str__(self) -> str:
        return "\n".join([str(self.grid[i]) for i in range(self.size)])

from utils import rand_state
import pygame as p


class Grid:
    def __init__(self, size, init_state=[], density=0.5) -> None:
        self.size = size
        if init_state == []:
            self.grid = self.create_random_grid(density)
        else:
            self.grid = self.create_grid_from_state(size, init_state)
        self.colors = [p.Color("white"), p.Color("black")]

    def create_grid_from_state(
        self, size: int, init_state: list[tuple]
    ) -> list[list[int]]:
        grid = []
        for _ in range(size):
            ligne = []
            for _ in range(size):
                ligne.append(0)
            grid.append(ligne)
        for x, y in init_state:
            grid[x][y] = 1
        return grid

    def create_random_grid(self, density: float):
        grid = []
        for _ in range(self.size):
            ligne = []
            for _ in range(self.size):
                ligne.append(rand_state(density))
            grid.append(ligne)
        return grid

    def get_square_value(self, x, y):
        return self.grid[x][y]

    def step(self):
        new_grid = [line[:] for line in self.grid]
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

    def toggle_state_cell(self, x: int, y: int):
        self.grid[x][y] = 1 - self.grid[x][y]

    def render(self, screen, pos: tuple[int, int], win_size: int):
        square_size = win_size // self.size
        for x in range(self.size):
            for y in range(self.size):
                p.draw.rect(
                    screen,
                    self.colors[self.get_square_value(x, y)],
                    p.Rect(
                        pos[0] + x * square_size,
                        pos[1] + y * square_size,
                        square_size,
                        square_size,
                    ),
                )

    def __str__(self) -> str:
        return "\n".join([str(self.grid[i]) for i in range(self.size)])

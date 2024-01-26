from math import floor
from time import perf_counter
import pygame as p
from logic import Grid
from window import Window

INIT_STATE = [(1, 1), (2, 1), (0, 1)]
FPS = 10


class Game(Window):
    def __init__(self, app, grid_size, density) -> None:
        super().__init__(app)
        self.grid = Grid(grid_size, density=density)
        self.colors = [p.Color("white"), p.Color("black")]
        self.auto_play = False
        self.last_step_time = perf_counter()
        self.square_size = self.width / grid_size

    def render(self):
        self.screen.fill(self.colors[0])
        for x in range(self.grid.size):
            for y in range(self.grid.size):
                p.draw.rect(
                    self.screen,
                    self.colors[self.grid.get_square_value(x, y)],
                    p.Rect(
                        x * self.square_size,
                        y * self.square_size,
                        self.square_size,
                        self.square_size,
                    ),
                )

    def update(self, events):
        if self.auto_play and (perf_counter() - self.last_step_time) > (1 / FPS):
            self.grid.step()
            self.last_step_time = perf_counter()
        for e in events:
            if e.type == p.MOUSEBUTTONDOWN:
                if e.button == 1:
                    self.change_cell_from_click(p.mouse.get_pos())
            if e.type == p.KEYDOWN:
                if e.key == p.K_SPACE:
                    self.auto_play = not self.auto_play
                if e.key == p.K_RIGHT:
                    self.grid.step()
                if e.key == p.K_ESCAPE:
                    self.exit_state()

    def change_cell_from_click(self, mouse_pos):
        x = floor(mouse_pos[0] / self.square_size)
        y = floor(mouse_pos[1] / self.square_size)
        self.auto_play = False
        self.grid.toggle_state_cell(x, y)

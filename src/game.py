from math import floor
from time import perf_counter
import pygame as p
from gol import Grid
from window import Window

FPS = 10


class Game(Window):
    def __init__(self, app, grid: Grid) -> None:
        super().__init__(app)
        self.grid = grid
        self.auto_play = False
        self.last_step_time = perf_counter()
        self.square_size = self.width / grid.size

    def render(self):
        self.grid.render(self.screen, (0, 0), self.width)

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

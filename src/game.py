# import the p modul
import pygame as p
from logic import Grid

WIN_SIZE = 600
SIZE = 60
SQUARE_SIZE = WIN_SIZE / SIZE
INIT_STATE = [(1, 1), (2, 1), (0, 1)]
DENSITY = 0.5


class Game:
    def __init__(self) -> None:
        self.background_colour = (255, 255, 255)
        self.screen = p.display.set_mode((WIN_SIZE, WIN_SIZE))
        p.display.set_caption("Game of Life")
        self.running = True
        self.grid = Grid(SIZE, density=DENSITY)
        self.colors = [p.Color("white"), p.Color("black")]

    def game_loop(self):
        while self.running:
            self.display(self.screen)
            self.update()
            self.get_events()

    def display(self, screen):
        for x in range(self.grid.size):
            for y in range(self.grid.size):
                p.draw.rect(
                    screen,
                    self.colors[self.grid.get_square_value(x, y)],
                    p.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )
        p.display.flip()

    def update(self):
        # self.grid.step()
        pass

    def get_events(self):
        for e in p.event.get():
            if e.type == p.QUIT:
                self.running = False
            if e.type == p.KEYDOWN:
                if e.key == p.K_ESCAPE:
                    self.running = False
                if e.key == p.K_RIGHT:
                    self.grid.step()


if __name__ == "__main__":
    game = Game()
    game.game_loop()

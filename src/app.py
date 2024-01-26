import pygame as p
from menu import Menu


class App:
    def __init__(self) -> None:
        p.init()
        p.display.set_caption("Game of Life")
        self.width = 1000
        self.height = 1000
        self.screen = p.display.set_mode((self.width, self.height))
        self.font = p.font.Font("freesansbold.ttf", 20)
        self.running = True
        self.current_window = Menu(self)
        self.state_stack = [self.current_window]

    def get_events(self):
        return p.event.get()

    def check_for_quit(self, events):
        for e in events:
            if e.type == p.QUIT:
                self.running = False

    def run(self):
        while self.running:
            events = self.get_events()
            self.check_for_quit(events)
            self.state_stack[-1].update(events)
            self.state_stack[-1].render()
            p.display.flip()


if __name__ == "__main__":
    app = App()
    app.run()

from abc import abstractmethod, ABC


class Window(ABC):
    def __init__(self, app) -> None:
        self.app = app
        self.screen = app.screen
        self.width, self.height = self.screen.get_size()

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def update(self, events):
        pass

    def enter_state(self, window):
        self.app.state_stack.append(window)

    def exit_state(self):
        self.app.state_stack.pop()

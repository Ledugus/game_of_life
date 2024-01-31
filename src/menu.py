import pygame as p
import pygame_widgets
from pygame_widgets.button import Button
from slider_combo import SliderCombo
from window import Window
from game import Game
from gol import Grid


class Menu(Window):
    """Menu principal"""

    def __init__(self, app) -> None:
        super().__init__(app)
        self.title = self.app.font.render(
            "Bienvenue au jeu de la vie !", True, "#b68f40"
        )
        self.begin_game_button = Button(
            self.screen,
            self.width // 2,
            100,
            170,
            30,
            text="Lancer la partie",
            onClick=self.launch_game,
            colour=(182, 127, 117),
            textColour=(10, 10, 10),
            borderThickness=1,
            radius=3,
        )

        self.size_text = self.app.font.render("Taille de la grille", True, (0, 0, 0))

        self.size_slider_combo = SliderCombo(
            self.screen, self.width / 2 - 100, 300, 10, 100, self.reload_preview
        )
        self.density_text = self.app.font.render(
            "Densité de la grille (%)", True, (0, 0, 0)
        )
        self.density_slider_combo = SliderCombo(
            self.screen, self.width / 2 - 100, 400, 0, 100, self.reload_preview
        )
        self.reload_preview()

    def render(self):
        self.game_grid.render(
            self.screen, (self.width // 2 - 150, self.height - 400), 300
        )
        self.screen.blit(self.size_text, (self.width / 2 - 300, 300))
        self.screen.blit(self.density_text, (self.width / 2 - 300, 400))
        self.screen.blit(self.title, (self.width // 2, 30))

    def update(self, events):
        self.screen.fill(p.Color("white"))
        pygame_widgets.update(events)
        self.size_slider_combo.update()
        self.density_slider_combo.update()

    def reload_preview(self):
        self.game_grid = Grid(
            self.size_slider_combo.get_value(),
            density=self.density_slider_combo.get_value() / 100,
        )

    def launch_game(self):
        game = Game(self.app, self.game_grid)
        self.enter_state(game)

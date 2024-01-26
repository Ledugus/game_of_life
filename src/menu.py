import pygame as p
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from slider_combo import SliderCombo
from window import Window
from game import Game


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
            self.screen, self.width / 2 - 100, 300, 0, 100
        )
        self.density_text = self.app.font.render(
            "Densité de la grille (%)", True, (0, 0, 0)
        )
        self.density_slider_combo = SliderCombo(
            self.screen, self.width / 2 - 100, 400, 0, 100
        )

    def render(self):
        self.screen.blit(self.size_text, (self.width / 2 - 300, 300))
        self.screen.blit(self.density_text, (self.width / 2 - 300, 400))
        self.screen.blit(self.title, (self.width // 2, 30))

    def update(self, events):
        self.screen.fill(p.Color("white"))
        pygame_widgets.update(events)
        self.size_slider_combo.update()
        self.density_slider_combo.update()

    def launch_game(self):
        game = Game(
            self.app,
            self.size_slider_combo.get_value(),
            self.density_slider_combo.get_value() / 100,
        )
        self.enter_state(game)

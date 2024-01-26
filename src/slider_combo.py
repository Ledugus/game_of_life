from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox


class SliderCombo:
    def __init__(self, screen, x, y, min: int, max: int, init_value=None) -> None:
        self.textbox = TextBox(
            screen, x + 110, y, 150, 50, onSubmit=self.set_slider_from_text_box
        )
        self.slider = Slider(screen, x, y, 100, 10, min=min, max=max)
        self.max = max
        self.min = min
        self.half = self.min + (self.max - self.min) // 2
        if init_value is None:
            self.textbox.setText(self.half)
            self.slider.setValue(self.half)
        else:
            self.textbox.setText(init_value)
            self.slider.setValue(init_value)

    def set_slider_from_text_box(self):
        try:
            number = int(self.textbox.getText())
        except ValueError:
            return
        if self.min <= number <= self.max:
            self.slider.setValue(number)

    def get_value(self):
        return self.slider.getValue()

    def update(self):
        if self.slider.selected:
            self.textbox.setText(self.slider.getValue())

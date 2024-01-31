from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox


class SliderCombo:
    def __init__(
        self, screen, x, y, min: int, max: int, on_value_change, init_value=None
    ) -> None:
        self.textbox = TextBox(
            screen, x + 110, y, 150, 50, onSubmit=self.set_value_from_text_box
        )
        self.slider = Slider(screen, x, y, 100, 10, min=min, max=max)
        self.max = max
        self.min = min
        self.init_value = (
            init_value if init_value else self.min + (self.max - self.min) // 2
        )
        self.slider.setValue(self.init_value)
        self.textbox.setText(self.init_value)
        self.previous_value = self.init_value
        self.on_value_change = on_value_change

    def set_value_from_text_box(self):
        try:
            number = int(self.textbox.getText())
        except ValueError:
            return
        if self.min <= number <= self.max:
            if number != self.slider.getValue():
                self.slider.setValue(number)
                self.on_value_change()

    def get_value(self):
        return self.slider.getValue()

    def update(self):
        if self.slider.selected:
            try:
                if int(self.textbox.getText()) != self.slider.getValue():
                    self.textbox.setText(self.slider.getValue())
                    self.on_value_change()
            except ValueError:
                self.textbox.setText(self.slider.getValue())

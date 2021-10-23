from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def on_button_click(self, value):
        result = self.model.calculate(value)
        self.view.input_value.set(result)

    def main(self):
        self.view.main()


if __name__ == '__main':
    controller = Controller()
    controller.main()
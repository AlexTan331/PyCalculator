import tkinter
from tkinter import *


# model
class Model:
    def __init__(self):
        self.operation_queue = [''] * 3

    def _clear_all(self):
        self.operation_queue = [''] * 3

    def calculate(self, value):
        if value == "clear":
            self._clear_all()
            return ""
        if not self.operation_queue[1]:
            if value == '.' and value in self.operation_queue[0]:
                pass
            elif value.isdigit() or (value == '.' and value not in self.operation_queue[0]):
                self.operation_queue[0] += value
            elif value == '+/-':
                operand = self.operation_queue[0]
                self.operation_queue[0] = operand[1:] if operand[0] == '-' else '-' + operand
            elif value == '=':
                pass
            else:
                if self.operation_queue[0]:
                    self.operation_queue[1] = value
        else:
            if value.isdigit() or (value == '.' and value not in self.operation_queue[2]):
                self.operation_queue[2] += value
            elif value == '+/-':
                operand = self.operation_queue[2]
                self.operation_queue[2] = operand[1:] if operand[0] == '-' else '-' + operand
            elif value == '=' and self.operation_queue[2]:
                result = str(eval("".join(self.operation_queue)))
                self._clear_all()
                self.operation_queue[0] = result

        print(self.operation_queue)
        return ''.join(self.operation_queue)


# view
class View(tkinter.Tk):
    PAD = 20

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.num_pad = [['clear', '%', '+/-', '/'],
                        ['7', '8', '9', '*'],
                        ['4', '5', '6', '-'],
                        ['1', '2', '3', '+'],
                        ['0', '.', '=']]
        self.input_value = tkinter.StringVar()
        self._build_gui()

    def _create_title(self):
        self.title('Calculator v0.1')

    def _create_frame(self):
        self.main_frame = tkinter.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)

    def _create_input_box(self):
        frame = tkinter.Frame(self.main_frame)
        frame.pack(fill=X, padx=self.PAD // 10, pady=self.PAD // 2)
        input_ = tkinter.Entry(frame, state='disabled', justify='right', textvariable=self.input_value, width=40)
        input_.pack(side=LEFT, fill=X, ipady=10)
        exit_button = tkinter.Button(frame, text='Exit', command=self.destroy)
        exit_button.pack(fill=X, padx=2, ipady=6)

    def _create_buttons(self):
        for row_idx, rows in enumerate(self.num_pad):
            frame = tkinter.Frame(self.main_frame)
            frame.pack()
            for column_idx, val in enumerate(rows):
                btn = tkinter.Button(frame, text=val, width=10,
                                     command=lambda v=val: self.controller.on_button_click(v))
                btn.pack(side=LEFT, fill=X, padx=self.PAD // 10, pady=self.PAD // 10)

    def _build_gui(self):
        self._create_title()
        self._create_frame()
        self._create_input_box()
        self._create_buttons()
        self._center_window()

    def _center_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')

    def main(self):
        self.mainloop()


# controller
class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def on_button_click(self, value):
        result = self.model.calculate(value)
        self.view.input_value.set(result)

    def main(self):
        self.view.main()


if __name__ == "__main__":
    my_calculator = Controller()
    my_calculator.main()

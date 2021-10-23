import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    PAD = 20

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.num_pad = [['clear', '%', '+/-', '/'],
                        ['7', '8', '9', '*'],
                        ['4', '5', '6', '-'],
                        ['1', '2', '3', '+'],
                        ['0', '.', '=']]
        self.input_value = tk.StringVar()
        self._build_gui()

    def _create_title(self):
        self.title('Calculator v0.1')

    def _create_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)

    def _create_input_box(self):
        frame = ttk.Frame(self.main_frame)
        frame.pack(fill='x', padx=self.PAD // 10, pady=self.PAD // 2)
        input_ = ttk.Entry(frame, state='disabled', justify='right', textvariable=self.input_value, width=40)
        input_.pack(side='left', fill='x', ipady=10)
        exit_button = ttk.Button(frame, text='Exit', command=self.destroy)
        exit_button.pack(fill='x', padx=2, ipady=6)

    def _create_buttons(self):
        for row_idx, rows in enumerate(self.num_pad):
            frame = ttk.Frame(self.main_frame)
            frame.pack()
            for column_idx, val in enumerate(rows):
                btn = ttk.Button(frame, text=val, width=10,
                                 command=lambda v=val: self.controller.on_button_click(v))
                btn.pack(side='left', fill='x', padx=self.PAD // 10, pady=self.PAD // 10)

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

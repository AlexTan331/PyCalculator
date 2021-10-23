import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    PAD = 10

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.num_pad = [[('clear', 'Mis.TButton'), ('%', 'Mis.TButton'), ('+/-', 'Mis.TButton'), ('/', 'Mis.TButton')],
                        [('7', "Digit.TButton"), ('8', 'Digit.TButton'), ('9', 'Digit.TButton'), ('*', 'Mis.TButton')],
                        [('4', 'Digit.TButton'), ('5', 'Digit.TButton'), ('6', 'Digit.TButton'), ('-', 'Mis.TButton')],
                        [('1', 'Digit.TButton'), ('2', 'Digit.TButton'), ('3', 'Digit.TButton'), ('+', 'Mis.TButton')],
                        [('0', 'Digit.TButton'), ('.', 'Mis.TButton'), ('=', 'Equal.TButton')]]
        self.geometry('500x280')
        self.config(bg='black')
        self._config_button_style()
        self.input_value = tk.StringVar()
        self._build_gui()

    @staticmethod
    def _config_button_style():
        style = ttk.Style()
        # theme: ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        style.theme_use('clam')

        # style for digit buttons
        style.configure('Digit.TButton', foreground='black', background='#edf2f4', font=("Arial", 10))

        # style for exit button
        style.configure('Exit.TButton', width=5, foreground='red', background='white', font=("Arial", 15, 'underline'))

        # style for operation buttons
        style.configure('Mis.TButton', foreground='black', background='#f8f9fa', font=("Arial", 10))

        # style for equal sign button
        style.configure('Equal.TButton', foreground='black', background='green', font=("Arial", 10))

    def _create_title(self):
        self.title('Calculator v0.1')

    def _create_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD // 5, pady=self.PAD // 5)

    def _create_input_box(self):
        frame = ttk.Frame(self.main_frame)
        frame.pack(fill='x', padx=self.PAD // 10, pady=self.PAD // 2)

        exit_button = ttk.Button(frame, text='Exit', command=self.destroy, style='Exit.TButton')
        exit_button.pack(side='left', padx=2)

        input_box = tk.Entry(frame, state='disabled', justify='right', textvariable=self.input_value)
        input_box.pack(fill='x', ipady=10)

    def _create_buttons(self):
        for row_idx, rows in enumerate(self.num_pad):
            frame = ttk.Frame(self.main_frame)
            frame.pack(fill='x')
            for column_idx, val in enumerate(rows):
                label, style = val
                if label == '=':
                    fill = 'x'
                    expand = 1
                else:
                    fill = 'none'
                    expand = 0

                btn = ttk.Button(frame, text=label, width=15,
                                 command=lambda v=label: self.controller.on_button_click(v), style=style)
                btn.pack(side='left', fill=fill, expand=expand, ipady=5, padx=self.PAD // 10, pady=self.PAD // 10)

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

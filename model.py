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

    
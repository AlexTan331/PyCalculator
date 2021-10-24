class Model:
    OPERATORS = ['/', '*', '-', '+']

    def __init__(self):
        self._init_queue()

    def _init_queue(self):
        self.operation_queue = [''] * 99
        self.idx = 0

    def calculate(self, value):
        if value == 'clear':
            self._init_queue()
            return ""

        if self.idx % 2 == 0:
            if value.isdigit() or (value == '.' and value not in self.operation_queue[self.idx]):
                self.operation_queue[self.idx] += value
            elif value == "%" and self.idx == 0 and self.operation_queue[0]:
                self.operation_queue[0] = str(eval(f'{self.operation_queue[0]} / 100'))
            elif value in self.OPERATORS and self.operation_queue[self.idx] and self.idx + 1 < len(self.operation_queue):
                self.idx += 1
                self.operation_queue[self.idx] = value
            elif value == '+/-' and self.operation_queue[self.idx]:
                operand = self.operation_queue[self.idx]
                self.operation_queue[self.idx] = operand[1:] if operand[0] == '-' else '-' + operand
            elif value == '=':
                result = str(eval("".join(self.operation_queue)))
                self._init_queue()
                self.operation_queue[0] = result
        else:
            if value in self.OPERATORS:
                self.operation_queue[self.idx] = value
            elif value.isdigit() or (value == '.' and value not in self.operation_queue[self.idx + 1]):
                self.idx += 1
                self.operation_queue[self.idx] = value

        return ''.join(self.operation_queue)
import math

class Functions:
    def __init__(self, fg):
        self.fg = fg

    def calculate(self, name, values):
        function = getattr(self, name)
        return function(values)

    def f1(self, values):
        x1 = values["x1"]
        x2 = values["x2"]

        F1 = {(0, 0): -0.9,
              (0, 1): 0.1,
              (1, 0): -0.1,
              (1, 1): -1.1,
              }

        value = F1[(x1, x2)]
        return value

    def f2(self, values):
        x1 = values["x1"]
        x2 = values["x2"]
        x3 = values["x3"]

        F2 = {(0, 0, 0): -2.1,
              (0, 0, 1): -1.1,
              (0, 1, 0): 0.1,
              (0, 1, 1): -0.9,
              (1, 0, 0): -1.1,
              (1, 0, 1): -0.1,
              (1, 1, 0): -0.9,
              (1, 1, 1): -1.9
              }

        value = F2[(x1, x2, x3)]

        return value

    def f3(self, values):
        x2 = values["x2"]
        x3 = values["x3"]

        F3 = {(0, 0): -1.1,
              (0, 1): 0.1,
              (1, 0): -0.1,
              (1, 1): -0.9,
              }

        value = F3[(x2, x3)]
        return value

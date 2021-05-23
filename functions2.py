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

        F1 = {(0, 0): 10,
              (0, 1): 5,
              (0, 2): 5,
              (1, 0): 2,
              (1, 1): 2,
              (1, 2): 2,
              (2, 0): 0,
              (2, 1): 0,
              (2, 2): 0,
              }

        value = F1[(x1, x2)]
        return value

    def f2(self, values):
        x1 = values["x1"]
        x2 = values["x2"]

        F2 = {(0, 0): 0,
              (0, 1): 1,
              (0, 2): 0,
              (1, 0): 7,
              (1, 1): 10,
              (1, 2): 7,
              (2, 0): 2,
              (2, 1): 2,
              (2, 2): 2,
              }

        value = F2[(x1, x2)]

        return value

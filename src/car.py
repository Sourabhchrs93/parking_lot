class Car:
    def __init__(self, reg_no, colour):
        self._reg_no = reg_no
        self._colour = colour

    def get_reg_no(self):
        return self._reg_no

    def get_colour(self):
        return self._colour

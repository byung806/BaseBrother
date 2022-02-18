class ScreenManager():
    START, CHOOSER, CONVERSIONS, OPERATIONS = 0,1,2,3

    def __init__(self):
        self.active_screen = self.START

    def switch_screen(self, type):
        self.active_screen = type

    def reset(self):
        self.switch_screen(self.START)

    def current(self):
        return self.active_screen
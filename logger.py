class Logger:
    def __init__(self) -> None:
        self.green = "\033[38;2;00;255;65m"
        self.default = "\033[39m"

    def log(self, *args):
        print(*args)

    def set_color(self):
        print(self.green, end='')

    def reset_color(self):
        print(self.default, end='')

class Sut:
    def __init__(self, a):
        self.a = a

    def get(self):
        return self.a

    def get_prefix(self, prefix):
        return f"{prefix}{self.a}"

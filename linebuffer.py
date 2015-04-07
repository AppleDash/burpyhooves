class LineBuffer:
    def __init__(self, data=""):
        self.data = data

    def append(self, data):
        self.data += data

    def has_line(self):
        return "\n" in self.data

    def pop_line(self):
        try:
            line, self.data = self.data.split("\n", 1)
        except ValueError:
            return None
        return line.strip()

    def flush(self):
        data, self.data = self.data, ""
        return data

    def __iter__(self):
        return self

    def __next__(self):
        line = self.pop_line()
        if line:
            return line
        raise StopIteration()

    next = __next__ # __next__() in Python 3; next() in Python 2

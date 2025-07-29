class OpenFile:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with OpenFile("test.txt", "w") as f:
    f.write("Custom context manager!")

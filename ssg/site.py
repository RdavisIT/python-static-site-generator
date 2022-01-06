from pathlib import path


class Site:

    def __init__(self, source, dest):
        self.source = path(source)
        self.dest = path(dest)

    def create_dir(self, path):
        directory = self.dest / path(relative_to(self.source))

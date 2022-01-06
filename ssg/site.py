<<<<<<< Updated upstream
from pathlib import Path
=======
from pathlib import path
>>>>>>> Stashed changes


class Site:

    def __init__(self, source, dest):
<<<<<<< Updated upstream
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
=======
        self.source = path(source)
        self.dest = path(dest)

    def create_dir(self, path):
        directory = self.dest
>>>>>>> Stashed changes

import typer
from ssg.site import Site

source = "content"
dest = "dist"

def main(source, dest):
    config = {"source": source,
              "dest": dest}
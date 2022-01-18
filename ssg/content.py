import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content:
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)
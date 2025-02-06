import os

from os import PathLike
from pathlib import Path
from typing import Union, Literal

def create_file(path: Union[str, PathLike, Path] = None, text: str = None, mode: Literal["w", "wb", "a", "ab"] = None) -> None:
    if mode is None:
        mode = "w"

    if text is None:
        text = "This is a test text"

    if not os.path.splitext(path):
        raise TypeError("Invalid path structure")
    else:
        dirname = os.path.dirname(path)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

    with open(path, mode) as f:
        f.write(text)
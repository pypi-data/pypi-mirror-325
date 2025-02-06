import os
import glob

from os import PathLike
from pathlib import Path

from typing import List, Union, Tuple

def classify_paths(paths: List[Union[str, Path, PathLike]] = None) -> Tuple[List[Union[str, Path, PathLike]], List[Union[str, Path, PathLike]]]:
    """
        Put folders in folders list and files in files list

        Params:
        ----------
            - paths: a list that contains a jumble of paths (could be file paths and/or folder paths)

        Return:
        ----------
        A tuple contains file paths list and folder paths list
    """
    filepaths = []
    folderpaths = []

    for path in paths:
        if os.path.isfile(path):
            filepaths.append(path)
        else:
            folderpaths.append(path)

    return filepaths, folderpaths

def versatile_glob(paths: List[Union[str, Path, PathLike]] = None, exts: str = None) -> List[Union[str, Path, PathLike]]:
    """
        versatile_glob() helps its user searching for file paths with many specific extensions easier.

        Params:
        ----------
            - paths: a list that contains a jumble of paths (could be file paths and/or folder paths)
            - exts: extensions of files to look for in each folder of _paths_ parameter

        Return:
        ----------
            - filepaths: a list of found file paths
    """
    filepaths, folderpaths = classify_paths(paths)

    for folderpath in folderpaths:
        for ext in exts:
            looking_for_path = os.path.join(folderpath, f"*{ext}")
            globbed_paths = glob.glob(looking_for_path)

            filepaths.extend(globbed_paths)    

    return filepaths
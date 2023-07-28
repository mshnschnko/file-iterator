import os
import pathlib
import re
from typing import Generator, Any

class FileSystemIterator:

    
    def __init__(self, root: str = "./", only_files: bool = False, only_dirs: bool = False, pattern: str = None) -> None:
        if not os.path.exists(root):
            raise FileNotFoundError
        self.__root = root
        self.__only_files = only_files
        self.__only_dirs = only_dirs
        self.__pattern = pattern
        self.__generator = self.__get_generator()


    def __iter__(self) -> 'FileSystemIterator':
        return self


    def __next__(self) -> pathlib.Path:
        return next(self.__generator)
    

    def __get_iteration(self, root: str, gen):
        for f in gen:
            if not self.__pattern is None and re.search(self.__pattern, f) is None:
                continue
            yield pathlib.Path(root) / pathlib.Path(f)


    def __get_generator(self):
        for root, dirs, files in os.walk(self.__root):
            if self.__only_files and self.__only_dirs:
                raise ValueError
            if self.__only_files:
                yield from self.__get_iteration(root=root, gen=files)
            elif self.__only_dirs:
                yield from self.__get_iteration(root=root, gen=dirs)
            else:
                yield from self.__get_iteration(root=root, gen=dirs)
                yield from self.__get_iteration(root=root, gen=files)

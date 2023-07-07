import os
import re

class FileSystemIterator:
    
    def __init__(self, root: str = "./", only_files: bool = False, only_dirs: bool = False, pattern: str = None) -> None:
        self.__root = root
        self.__only_files = only_files
        self.__only_dirs = only_dirs
        self.__pattern = pattern


    def __iter__(self) -> str:
        if self.__only_files:
            dir = next(os.walk(self.__root))
            for file in dir[2]:
                if not self.__pattern is None and re.search(self.__pattern, file) is None:
                    continue
                yield os.path.join(dir[0], file)
        else:
            for root, dirs, files in os.walk(self.__root):
                if self.__only_dirs:
                    for dir in dirs:
                        if not self.__pattern is None and re.search(self.__pattern, dir) is None:
                            continue
                        yield os.path.join(root, dir)
                else:
                    for file in files:
                        if not self.__pattern is None and re.search(self.__pattern, file) is None:
                            continue
                        yield os.path.join(root, file)
    

    def __next__(self) -> str:
        return next(iter(self))
    
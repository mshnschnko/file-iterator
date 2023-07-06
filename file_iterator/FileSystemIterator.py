import os


class FileSystemIterator:
    
    def __init__(self, root: str = "./", only_files: bool = False, only_dirs: bool = False, pattern: str = None) -> None:
        self.__root = root
        self.__only_files = only_files
        self.__only_dirs = only_dirs
        self.__pattern = pattern

    def __iter__(self):
        if self.__only_files:
            dir = next(os.walk(self.__root))
            for file in dir[2]:
                yield os.path.join(dir[0], file)
            # yield os.path.join(root, file)
        else:
            for root, dirs, files in os.walk(self.__root):
                if self.__only_dirs:
                    for dir in dirs:
                        yield os.path.join(root, dir)
                else:
                    for file in files:
                        yield os.path.join(root, file)
    
    def __next__(self):
        for root, dirs, files in os.walk(self.__root):
            print()
            print('in next')
            yield files
        return StopIteration
from file_iterator import FileSystemIterator
import os


if __name__ == "__main__":

    print(next(FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=False, pattern=r"(f\d)")))
    print(next(FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=False)))
    print(next(FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=True)))
    print(next(FileSystemIterator(root="tests\\tmp", only_files=True, only_dirs=False)))
    print("="*20)

    fi = iter(FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=True, pattern=r"(tmp[3-5])"))
    print(next(fi))
    print(next(fi))
    print(next(fi))
    print("="*20)

    for flfl in FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=False, pattern=None):
        print(flfl)

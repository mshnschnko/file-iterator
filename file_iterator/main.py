from FileSystemIterator import FileSystemIterator
import os

def iterations(path):
    for root, dirs, files in os.walk(path):
        # print(root, dirs, files, sep='\n')
        # print()
        yield files

def f():
    r = 0
    for i in range(10):
        r += 1
        yield r

if __name__ == "__main__":
    # for root, dirs, files in os.walk('tmp'):
    #     print(root, dirs, files, sep='\n')
    #     print()
    

    # fi = FileSystemIterator(root="tmp")
    # i = 0

    # print(fi.__next__())
    # print(fi.__next__())

    # it = iterations(path='tmp')
    for flfl in FileSystemIterator(root="tmp"):
        print(flfl)


    # for item in fi:
    #     print(item)
    #     i += 1
    #     if (i==10):
    #         break
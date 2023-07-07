import pytest

from file_iterator import FileSystemIterator


def test_case_0():
    with pytest.raises(StopIteration):
        next(FileSystemIterator(root="non-existent folder", only_files=False, only_dirs=False, pattern=None))


def test_case_1():
    assert (
        next(FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=False, pattern=None))
        == r"tests\tmp\fil1.txt"
    )
    assert (
        next(FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=True, pattern=None))
        == r"tests\tmp\tmp2"
    )
    assert (
        next(FileSystemIterator(root="tests\\tmp", only_files=True, only_dirs=False, pattern=None))
        == r"tests\tmp\fil1.txt"
    )
    assert (
        next(FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=False, pattern=r"(f\d)"))
        == r"tests\tmp\tmp3\f3"
    )


def test_case_2():
    fi = iter(FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=False, pattern=None))
    assert (
        next(fi)
        == r"tests\tmp\fil1.txt"
    )
    assert (
        next(fi)
        == r"tests\tmp\file2.txt"
    )
    assert (
        next(fi)
        == r"tests\tmp\tmp2\file1_1.txt"
    )


def test_case_3():
    fi = iter(FileSystemIterator(root="tests\\tmp", only_files=True, only_dirs=False, pattern=None))
    assert (
        next(fi)
        == r"tests\tmp\fil1.txt"
    )
    assert (
        next(fi)
        == r"tests\tmp\file2.txt"
    )
    with pytest.raises(StopIteration):
        next(fi)


def test_case_4():
    fi = iter(FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=True, pattern=None))
    assert (
        next(fi)
        == r"tests\tmp\tmp2"
    )
    assert (
        next(fi)
        == r"tests\tmp\tmp3"
    )
    assert (
        next(fi)
        == r"tests\tmp\tmp3\tmp4"
    )


def test_case_5():
    fi = iter(FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=False, pattern=r"(file)"))
    assert (
        next(fi)
        == r"tests\tmp\file2.txt"
    )
    assert (
        next(fi)
        == r"tests\tmp\tmp2\file1_1.txt"
    )
    with pytest.raises(StopIteration):
        next(fi)


def test_case_6():
    fi = iter(FileSystemIterator(root="tests\\tmp", only_files=True, only_dirs=False, pattern=r"(file)"))
    assert (
        next(fi)
        == r"tests\tmp\file2.txt"
    )
    with pytest.raises(StopIteration):
        next(fi)


def test_case_7():
    fi = iter(FileSystemIterator(root="tests\\tmp", only_files=False, only_dirs=True, pattern=r"(tmp[3-5])"))
    assert (
        next(fi)
        == r"tests\tmp\tmp3"
    )
    assert (
        next(fi)
        == r"tests\tmp\tmp3\tmp4"
    )
    assert (
        next(fi)
        == r"tests\tmp\tmp3\tmp4\tmp5"
    )
    with pytest.raises(StopIteration):
        next(fi)
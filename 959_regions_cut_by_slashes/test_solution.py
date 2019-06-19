from solution import regions_by_slashes_using_union_find


def test_sample_1():
    grid = [" /",
            "/ "]  # yapf: disable
    assert 2 == regions_by_slashes_using_union_find(grid)


def test_sample_2():
    grid = [" /",
            "  "]  # yapf: disable
    assert 1 == regions_by_slashes_using_union_find(grid)


def test_sample_3():
    grid = ["\\/",
            "/\\"]  # yapf: disable
    assert 4 == regions_by_slashes_using_union_find(grid)


def test_sample_4():
    grid = ["/\\",
            "\\/"]  # yapf: disable
    assert 5 == regions_by_slashes_using_union_find(grid)


def test_sample_5():
    grid = ["//",
            "/ "]  # yapf: disable
    assert 3 == regions_by_slashes_using_union_find(grid)
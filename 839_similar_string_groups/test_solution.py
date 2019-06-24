from solution import num_similiar_groups_using_union_find


def test_sample_1():
    assert 2 == num_similiar_groups_using_union_find(
        ["tars", "rats", "arts", "star"])

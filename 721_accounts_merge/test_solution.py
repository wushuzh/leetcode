from solution import accounts_merge_using_union_find


def test_sample():
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]]  # yapf: disable
    expected = [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
                ["John", "johnnybravo@mail.com"],
                ["Mary", "mary@mail.com"]]  # yapf: disable

    assert expected == accounts_merge_using_union_find(accounts)
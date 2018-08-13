import pytest
from random import randint

from solution import twoSum2_cache, twoSum2_binary_search


@pytest.fixture(params=[twoSum2_cache, twoSum2_binary_search])
def diff_solution(request):
    return request.param


def test_1_even_with_many_odd(diff_solution):
    chk_iter = 1000
    for _ in range(chk_iter):
        len_a = randint(2, chk_iter)
        even_i = randint(0, len_a-1)

        input_a = [2*i-1 for i in range(0, even_i)]
        input_a.append(2*even_i)
        input_a += [2*i-1 for i in range(even_i+1, len_a)]

        odd_j = randint(0, len_a-1)
        while odd_j == even_i:
            odd_j = randint(0, len_a-1)

        expect_i = [even_i+1, odd_j+1]
        expect_i.sort()

        m, n = diff_solution(input_a, input_a[even_i] + input_a[odd_j])
        assert [m, n] == expect_i

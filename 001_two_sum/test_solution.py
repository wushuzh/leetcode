from random import randint
from solution import two_sum


def test_two_sum(random_chk=1000):
    for _ in range(random_chk):
        len_a = randint(3, 100)
        input_a = [randint(0, 10) for _ in range(len_a)]

        m = randint(50, 60)
        n = randint(70, 80)

        m_idx = randint(0, len_a)
        n_idx = randint(0, len_a)

        input_a.insert(m_idx, m)
        input_a.insert(n_idx, n)

        if m_idx >= n_idx:
            m_idx += 1

        i, j = two_sum(input_a, m + n)
        assert input_a[i] + input_a[j] == m + n
        assert {i, j} == {m_idx, n_idx}

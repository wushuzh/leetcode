def chunk(xs, n):
    '''Split the list, xs, into n chunks
    '''
    L = len(xs)
    assert 0 < n <= L
    s = L//n
    return [xs[p:p+s] for p in range(0, L, s)]

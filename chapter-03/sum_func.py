sum_1k = lambda m: sum(1/x for x in range(1, m+1))
m = 3
print (sum_1k(m))

def test_sum_1k():
    """Test calculation of harmonic series """
    ep = 1e-14
    exact = 1 + 1/2 + 1/3
    calc = sum_1k(3)
    success = abs(exact - calc) < ep
    msg = 'Expected: %g, Result: %g' % (exact, calc)
    assert success, msg

test_sum_1k()
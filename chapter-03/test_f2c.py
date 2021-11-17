def test_F_C():
    """Test conversion of temperature units between C and F degrees """
    ep = 1e-14
    x = 10
    exact = C(F(x)) - F(C(x))
    success = abs(exact) < ep
    msg = 'F(C(x)): %g, C(F(x)): %g' % (F(C(x)), C(F(x)))
    assert success, msg

test_F_C()
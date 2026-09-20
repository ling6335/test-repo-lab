from testpkg.tribonacci import tribonacci


def test_tribonacci_zero():
    assert tribonacci(0) == 0


def test_tribonacci_base_cases():
    assert [tribonacci(n) for n in range(4)] == [0, 1, 1, 2]


def test_tribonacci_recurrence():
    for n in range(3, 10):
        assert tribonacci(n) == sum(tribonacci(n - offset) for offset in range(1, 4))


def test_tribonacci():
    assert tribonacci(1) == 1
    assert tribonacci(10) == 149

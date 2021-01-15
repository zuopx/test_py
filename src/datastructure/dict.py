d = {}
k = 'key'
v = 'value'


def test_setdefault():
    d.setdefault(k, []).append(v)
    assert v in d[k]

test_setdefault()


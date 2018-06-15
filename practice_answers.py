def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    return l

assert f(2) == [0, 1]
assert f(3,[3,2,1]) == [3, 2, 1, 0, 1, 4]
assert f(3) == [0, 1, 0, 1, 4] # because the 2nd time around we supplied our own list, it did not affect anything
#but this time, it will use the l already stored in memeory so the [0, 1] from the first time is already here

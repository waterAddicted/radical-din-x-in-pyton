
def radical(x):
    st = float(0)
    dr = float(x)
    mij = (st + dr) / 2
    while abs(mij * mij - x) > eps:
        if mij * mij < x:
            st = mij
        else:
            dr = mij
        mij = (st + dr)/2
    return mij

x = float(input())
eps = 0.0001
print(radical(x))
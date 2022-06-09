d = [1,2,3]

ss = []
res = []

def f(i):
    if i >= len(d):
        ss.append(res.copy())
        return
    res.append(d[i])
    f(i + 1)

    res.pop()
    f(i + 1)

f(0)
return ss

s = []
N = 16
for b in range(1, 10**(N//2)):
    n = len(str(b))
    delta = 10 ** (2*n) - 4*b*(10**n - 1)
    if delta >= 0:
        sq_delta = delta ** 0.5
        if int(sq_delta) != sq_delta:
            continue
        sq_delta = int(sq_delta)
        aa = 10**n // 2 - b
        if delta == 0 and aa > 0:
            print(aa * 10**n + b)
            s.append(aa * 10**n + b)
        elif delta > 0 and sq_delta % 2 == 0:
            aa1 = aa - sq_delta // 2
            if aa1 > 0:
                s.append(aa1 * 10**n + b)

            aa2 = aa + sq_delta // 2
            s.append(aa2 * 10**n + b)

print(sum(s))

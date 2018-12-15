
def clock(l, n, t):
	if len(l) == 2**n :
		if check_final(l, n):
			t += int(''.join([str(v) for v in l]), 2)
			return l, t
		else:
			return l, t

	if check(l, n):
		l.append(0)
		l, t = clock(l, n, t)
		l = l[:-1]

		l.append(1)
		l, t = clock(l, n, t)
		l = l[:-1]

	return l, t

def check_final(l, n):
	loop = l + l[:n-1]
	numb = []
	for i in range(2**n):
		to_add = ''.join(str(v) for v in loop[i:i+n])
		if to_add in numb:
			return False
		numb.append(to_add)
	return True


def check(l, n):
	numb = []
	for i in range(len(l) - n + 1):
		short = []
		while len(short) < n:
			short.append(l[(i+len(short)) % len(l)])
		to_add = ''.join([str(v) for v in short])
		if to_add in numb:
			return False
		numb.append(to_add)
	return True

# n = int(raw_input('n ?'))
n = 5
_, total =  clock([0]*n, n, 0)
print total
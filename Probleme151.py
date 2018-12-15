import numpy as np

compte = [[('1 1 1 1', 1.0)]] 
single = 0

for batch in xrange(15):
	tt = []
	for papers, proba in compte[batch]:
		papers = map(int, papers.split())
		t = float(sum(papers))
		if t==1:single+=proba

		if papers[0]:
			temp = [papers[0]-1, papers[1]+1, papers[2]+1, papers[3]+1]
			tt.append((' '.join(map(str, temp)), proba * papers[0] / t))
		if papers[1]:
			temp = [papers[0], papers[1]-1, papers[2]+1, papers[3]+1]
			tt.append((' '.join(map(str, temp)), proba * papers[1] / t))
		if papers[2]:
			temp = [papers[0], papers[1], papers[2]-1, papers[3]+1]
			tt.append((' '.join(map(str, temp)), proba * papers[2] / t))
		if papers[3]:
			temp = [papers[0], papers[1], papers[2], papers[3]-1]
			tt.append((' '.join(map(str, temp)), proba * papers[3] / t))

	temp = {}
	for papers, proba in tt:
		if papers in temp.keys():
			temp[papers] += proba
		else:
			temp[papers] = proba
	compte.append(zip(temp.keys(), temp.values()))

print single-1
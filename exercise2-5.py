import Pmf

def PmfMean(pmf):
	mean = 0
	for i in pmf.Items():
		mean += i[0] * i[1]
	return mean
def PmfVar(pmf,mean):
	var = 0
	for i in pmf.Items():
		var += i[1] * (i[0] - mean)**2
	return var

if __name__ == '__main__':
	pmf = Pmf.MakePmfFromList([2,4,6,8,10,12,14,16,18,20,22,24])
	mean = PmfMean(pmf)
	var = PmfVar(pmf,mean)
	print "Mean:" ,mean, "amswer",pmf.Mean()
	print "Var:" ,var, "answer",pmf.Var()
import Pmf

def PmfRemainingLifeTime(pmf,duration):

	newPmf = Pmf.Pmf()
	for y in pmf.Values():
		if y > duration:
			newPmf.Set(y - duration,pmf.Prob(y))

	newPmf.Normalize()
	return newPmf

if __name__ == '__main__':
	pmf = Pmf.MakePmfFromList([2,4,6,8,10,12,14,16,18,20,22,24])
	pmf = PmfRemainingLifeTime(pmf,15)
	for i in pmf.Items():
		print i[0], ":", i[1]
	
	
import Pmf
from operator import itemgetter

def Mode(hist):
	mode = 0
	maxFreq = 0
	for val,freq in hist.Items():
		if freq > maxFreq:
			maxFreq = freq
			mode = val
	return mode

def AllMode(hist):
	modelist = []
	for h in sorted(hist.Items(),key=itemgetter(1),reverse = True):
		modelist.append(h)
	return modelist


if __name__ == '__main__':
	hist = Pmf.MakeHistFromList([1,2,2,3,3,4,4,4,4,4,5,5,5])
	print "Mode:",Mode(hist)
	print "AllMode:",AllMode(hist)
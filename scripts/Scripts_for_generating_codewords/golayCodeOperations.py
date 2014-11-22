# This class contains general coding theory operations

def hammingDistanceKey( key1, key2 ):
	if key1 - key2 == 0:
		return 0
	else:
		return 1

def hammingDistanceCodewords( code1, code2 ):
	distance = 0
	for i in range( len( code1 ) ):
		distance += hammingDistanceKey( code1[i], code2[i] )
	return distance

def weightOfTrit( trit ):
	if trit == 0 or trit == '0':
		return 0
	else:
		return 1

def weight( code ):
	weight = 0
	for i in range( len( code ) ):
		weight += weightOfTrit( code[i] )
	return weight

def distanceCheck( List, minD, maxD = 1000 ):
	result = List
	answer = []
	i = 0
	smallResult = []
	while len( result ) > 0:
		newResult = []
		answer.append ( result[i] )
		for j in range( 1, len( result ) ):
			d = hammingDistanceCodewords( result[i], result[j] )
			if d >= minD and d <= maxD:
				newResult.append( result[j] )
		result = newResult
	return answer
'''		
	nineCount = 0
	sixCount = 0
	fiveCount = 0
	zeroCount = 0
	for i in range( len( answer ) ):
		print answer[i] , weight( answer[i] )
		if weight( answer[i] ) == 9:
			nineCount += 1
		elif weight( answer[i] ) == 6:
			sixCount += 1
		elif weight( answer[i] ) == 0:
			zeroCount += 1
		else:
			print "Buggy in weight"
	for i in range( len( smallResult ) ):
		print smallResult[i], weight( smallResult[i] )		
		if weight( smallResult[i] ) == 5:
			fiveCount += 1
		else:
			print "Buggy weight"

	print "W0", zeroCount
	print "W5", fiveCount
	print "W6", sixCount
	print "W9", nineCount
'''

def genWeightOfBinaryCodes():
	l = [0] * 9
	i = 256
	for j in range( i ):
		code = bin(j)[2:].zfill(8)
		print code, weight( list(code) )
		l[ weight( list(code) )] += 1

	for i in range( len( l ) ):
		print "Weight ", i , " : ", l[i]

#distanceCheck()
#genWeightOfBinaryCodes()

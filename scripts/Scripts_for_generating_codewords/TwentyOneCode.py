#This code generates ternary code [21, 6, 11]

import golayCodeOperations

def multiply ( mul, array ):
        temp = []
        for i in range( len( array ) ):
                temp.append( array[i] * mul )
        return temp

def add ( array1, array2, array3, array4, array5, array6, array7 ):
        temp = []
        for i in range( len( array1 ) ):
                sum = ( array1[i] + array2[i] + array3[i] + array4[i] + array5[i] + array6[i] + array7[i] ) % 3
                temp.append( sum )
        return temp

def generate():

	# Generator matrix for ternary code [23, 7, 12]
	r0 = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	r1 = [ 1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
	r2 = [ 2, 0, 0, 0, 1, 2, 2, 0, 1, 2, 2, 0, 1, 2, 0, 0, 1, 1, 1, 0, 0, 0, 0]
	r3 = [ 2, 1, 2, 0, 0, 2, 0, 0, 2, 1, 2, 0, 0, 1, 2, 0, 1, 2, 0, 1, 0, 0, 0]
	r4 = [ 2, 2, 0, 0, 0, 0, 1, 1, 0, 1, 2, 0, 1, 2, 1, 0, 2, 2, 0, 0, 1, 0, 0]
	r5 = [ 0, 2, 1, 2, 2, 2, 1, 2, 1, 0, 2, 0, 1, 2, 2, 0, 2, 1, 0, 0, 0, 1, 0]
	r6 = [ 0, 1, 0, 2, 0, 1, 2, 1, 1, 2, 2, 0, 0, 2, 2, 0, 0, 2, 0, 0, 0, 0, 1]
	
	result = []
	for i in range(3):
		code0 = multiply( i, r0[:22])
		for j in range(3):
			code1 = multiply( j, r1[:22])
			for k in range(3):
				code2 = multiply( k, r2[:22])
				for l in range(3):
					code3 = multiply( l, r3[:22] )
					for m in range(3):
						code4 = multiply( m, r4[:22])
						for n in range(3):
							code5 = multiply( n, r5[:22])
							for o in range(3):
								code6 = multiply( o, r6[:22])
								code = add( code0, code1, code2, code3, code4, code5, code6 )
								if code[21] == 0 :
									result.append(code[:21])
	return result

def generate21():
	L = generate()
	K = golayCodeOperations.distanceCheck( L, 11 )
        K0 = golayCodeOperations.distanceCheck( K, 12)

        for i in range( len( K ) ):
                if not K[i] in K0 and not len(K0) == 256 :
                        K0.append(L[i])
        return K0


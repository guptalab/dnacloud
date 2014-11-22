
#This code generates all codewords of Ternary code [26, 6, 15]

import golayCodeOperations

def multiply ( mul, array ):
        temp = []
        for i in range( len( array ) ):
                temp.append( array[i] * mul )
        return temp

def add ( array1, array2, array3, array4, array5, array6, array7, array8 ):
        temp = []
        for i in range( len( array1 ) ):
                sum = ( array1[i] + array2[i] + array3[i] + array4[i] + array5[i] + array6[i] + array7[i] + array8[i] ) % 3
                temp.append( sum )
        return temp

def generate():
	
	r0 = [ 1, 1, 1, 2, 0, 0, 1, 2, 1, 0, 2, 0, 1, 1, 1, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0]
	r1 = r0[27:] + r0[:27]
        r2 = r1[27:] + r1[:27]
        r3 = r2[27:] + r2[:27]
        r4 = r3[27:] + r3[:27]
        r5 = r4[27:] + r4[:27]
        r6 = r5[27:] + r5[:27]
        r7 = r6[27:] + r6[:27]
	
	result = []
	for i in range(3):
		code0 = multiply( i, r0)
		for j in range(3):
			code1 = multiply( j, r1)
			for k in range(3):
				code2 = multiply( k, r2)
				for l in range(3):
					code3 = multiply( l, r3)
					for m in range(3):
						code4 = multiply( m, r4)
						for n in range(3):
							code5 = multiply( n, r5)
							for o in range(3):
								code6 = multiply( o, r6)
								for p in range(3):
									code7 = multiply( p, r7)
									code = add( code0, code1, code2, code3, code4, code5, code6, code7 )
									if code[26] == 0 and code[27] == 0:
										result.append(code[:26])
	return result

def generate26():
        L = generate()
        K = golayCodeOperations.distanceCheck( L, 15)
	K0 = golayCodeOperations.distanceCheck( K, 16)

        for i in range( len( K ) ):
                if not K[i] in K0 and not len(K0) == 256 :
                        K0.append(L[i])
        return K0

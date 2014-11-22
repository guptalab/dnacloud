
import golayCodeOperations

def multiply ( mul, array ):
        temp = []
        for i in range( len( array ) ):
                temp.append( array[i] * mul )
        return temp

def add ( array1, array2, array3, array4, array5, array6, array7, array8, array9, array10, array11, array12 ):
        temp = []
        for i in range( len( array1 ) ):
                sum = ( array1[i] + array2[i] + array3[i] + array4[i] + array5[i] + array6[i] + array7[i] + array8[i] + array9[i] + array10[i] + array11[i] + array12[i] ) % 3
                temp.append( sum )
        return temp

def generate():

	r0 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 2, 2, 1, 1, 1]
	r1 = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 2, 1, 2, 1, 1, 0, 1, 0, 0]
	r2 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 2, 1, 2, 1, 1, 0, 1, 0]
	r3 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 2, 0, 2, 2]
	r4 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 1, 1, 1, 0, 2, 0, 1, 0]
	r5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 2, 0, 1, 2, 1, 1, 2, 2]
	r6 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 0, 0, 0, 1, 2, 2, 0]
	r7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 1, 0, 2, 0, 0, 2, 2, 2, 0, 1]
	r8 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 2, 1, 0, 2, 0, 0, 2, 2, 2, 1]
	r9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 2, 0, 1, 1, 2, 2, 2, 0, 0, 2]
	r10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 2, 0, 1, 1, 2, 2, 2, 0, 2]
	r11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 2, 0, 1, 1, 2, 2, 2, 2]

	result = []
	for a in range(3):
		code0 = multiply( a, r0)
		for b in range(3):
			code1 = multiply( b, r1)
			for c in range(3):
				code2 = multiply( c, r2)
				for d in range(3):
					code3 = multiply( d, r3)
					for e in range(3):
						code4 = multiply( e, r4)
						for f in range(3):
							code5 = multiply( f, r5)
							for g in range(3):
								code6 = multiply( g, r6)
								for h in range(3):
									code7 = multiply( h, r7)
									for i in range(3):
										code8 = multiply( i, r8)
										for j in range(3):
											code9 = multiply( j, r9)
											for k in range(3):
												code10 = multiply( k, r10)
												for l in range(3):
													code11 = multiply( l, r11)
													code = add( code0, code1, code2, code3, code4, code5, code6, code7, code8, code9, code10, code11 )
													if code[18] == 0 and code[19] == 0 and code[20] == 0 and code[21] ==0 and code[22] == 0 and code[23] == 0:
														result.append(code[:18])

	return result 

def generate18():
	L = generate()
	K = golayCodeOperations.distanceCheck( L, 9)
	K0 = golayCodeOperations.distanceCheck( K, 10)

        for i in range( len( K ) ):
                if not K[i] in K0 and not len(K0) == 256 :
                        K0.append(L[i])

        return K0



#This code generates all codewords of Ternary Golay Code i.e. [11, 6, 5] and [15, 6, 7]

import golayCodeOperations

def multiply ( mul, array ):
        temp = []
        for i in range( len( array ) ):
                temp.append( array[i] * mul )
        return temp

def add ( array1, array2, array3, array4, array5, array6 ):
        temp = []
        for i in range( len( array1 ) ):
                sum = ( array1[i] + array2[i] + array3[i] + array4[i] + array5[i] + array6[i] ) % 3
                temp.append( sum )
        return temp

def generate15():
        r1 = [ 1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        r2 = [ 0, 1, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 0, 0, 0]
        r3 = [ 0, 0, 1, 0, 0, 0, 1, 2, 1, 2, 0, 0, 2, 2, 0]
        r4 = [ 0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 1, 2, 1, 2, 0]
        r5 = [ 0, 0, 0, 0, 1, 0, 2, 1, 0, 1, 2, 0, 2, 0, 2]
        r6 = [ 0, 0, 0, 0, 0, 1, 1, 0, 2, 1, 2, 1, 1, 0, 2]

	L = generate( r1, r2, r3, r4, r5, r6)
	K = golayCodeOperations.distanceCheck( L, 7)
	K0 = golayCodeOperations.distanceCheck( K, 8)
	
	for i in range( len( K ) ):
                if not K[i] in K0 and not len(K0) == 256 :
                        K0.append(L[i])

        return K0


def generate11():
        # Generator matrix for [11, 6, 5] over GF(3)
        r1 = [ 2, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0]
        r2 = [ 0, 2, 0, 1, 2, 1, 1, 0, 0, 0, 0]
        r3 = [ 0, 0, 2, 0, 1, 2, 1, 1, 0, 0, 0]
        r4 = [ 0, 0, 0, 2, 0, 1, 2, 1, 1, 0, 0]
        r5 = [ 0, 0, 0, 0, 2, 0, 1, 2, 1, 1, 0]
        r6 = [ 0, 0, 0, 0, 0, 2, 0, 1, 2, 1, 1]
	
	L = generate( r1, r2, r3, r4, r5, r6)
	K = golayCodeOperations.distanceCheck( L, 5)
	K0 = golayCodeOperations.distanceCheck( K, 6)

        for i in range( len( K ) ):
                if not K[i] in K0 and not len(K0) == 256 :
                        K0.append(L[i])
      
        return K0

def generate( r1, r2, r3, r4, r5, r6):
        result = []

        for i in range(3):
                code1 = multiply( i, r1)
                for j in range(3):
                        code2 = multiply( j, r2)
                        for k in range(3):
                                code3 = multiply( k, r3)
                                for l in range(3):
                                        code4 = multiply( l, r4)
                                        for m in range(3):
                                                code5 = multiply( m, r5)
                                                for n in range(3):
                                                        code6 = multiply( n, r6)
                                                        result.append( add ( code1, code2, code3, code4, code5, code6 ) )
        return result


# This code generates all [9,6,3] codewords

import golayCodeOperations

def generateAll():
	List = []

	for i in range( 3 ):
		for j in range( 3 ):
			for k in range( 3 ):
				for l in range( 3 ):
					for m in range( 3 ):
						for n in range( 3 ):
							for o in range( 3 ):
								for p in range( 3 ):
									for q in range( 3 ):
										code = []
										code.append( i );
										code.append( j );
										code.append( k );
                                                                                code.append( l );
                                                                                code.append( m );
                                                                                code.append( n );
                                                                                code.append( o );
                                                                                code.append( p );
                                                                                code.append( q );
										List.append( code );

	return List

def generate():
	L = generateAll();
	K = golayCodeOperations.distanceCheck( L, 3);
	return K

def generate9():
	L = generate()
	K = golayCodeOperations.distanceCheck( L, 4)

	for i in range( len(L) ):
		if not L[i] in K and not len(K) == 256 :
			K.append(L[i])

	return K

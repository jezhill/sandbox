all = [
	'Baz',
]


def Baz( *pargs ):
	return '-'.join( str( arg ) for arg in pargs )

	
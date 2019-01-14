#import os,sys; sys.path.append(os.getcwd())  # only need this if running locally (without pip install .)


# pytest looks for test_*.py and *_test.py files like this one...


import Foo

def test_Baz0():  # ...and looks for test_*()  functions within the files it finds. (NB: it will not find methods, unless they belong to a class whose name begins with Test and which has no __init__.)
	assert Foo.Bar.Baz() == '' # In most cases you should use one assertion per function because, within any given function pytest won't go past the first failure.
	
def test_Baz1():
	assert Foo.Bar.Baz( 1 ) == '1'
	
def test_Baz3():
	assert Foo.Bar.Baz( 1, 2, 3 ) == '1-2-3'


if __name__ == '__main__':
	# pytest doesn't go here, but we could set things up to run this script
	# directly/explicitly if pytest is unavailable, as it is in python 3.0--3.3
	# (of course, we would need to call a wrapper script to detect that fact).
	# Note that this route will capture less detail about assertion failures.
	
	import sys
	objects = list( globals().items() )
	for name, func in objects:
		if not name.startswith( 'test_' ): continue
		if not callable( func ): continue
		try:
			func()
		except AssertionError:
			sys.stderr.write( func.__name__ + ' FAILED:\n' )
			sys.excepthook( *sys.exc_info() )
			sys.stderr.write( '\n' )
		else:
			sys.stderr.write( func.__name__ + ' PASSED\n' )

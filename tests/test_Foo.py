
import Foo

def test_Baz():
	assert Foo.Bar.Baz() == ' '
	assert Foo.Bar.Baz( 1 ) == '1 '
	assert Foo.Bar.Baz( 1, 2, 3 ) == '1-2-3 '
	
if __name__ == '__main__':
	test_Baz()

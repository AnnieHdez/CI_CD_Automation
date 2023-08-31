def test_f_ex():
	assert "hello"=="hello"

def f_function_to_test(val):
	return 123

def test_f_function_to_test():
	assert 123==f_function_to_test(123), "This is not 123"
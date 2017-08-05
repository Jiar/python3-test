import functools

def log1(func):
	def wrapper(*args, **kw):
		print('log1 %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
	
@log1
def aaa():
	print('aaa def')

aaa()
print(aaa.__name__)
print()


def log2(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
	
@log2('log2')
def bbb():
	print('bbb def')
	
bbb()
print(bbb.__name__)
print()


def log3(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('log3 %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log3
def ccc():
	print("ccc def")
	
ccc()
print(ccc.__name__)
print()


def log4(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log4('log4')
def ddd():
	print("ddd def")
	
ddd()
print(ddd.__name__)
print()

def log(*args):
	text = args[0] if isinstance(args[0],str) else 'log'
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s before %s():' % (text, func.__name__))
			result = func(*args, **kw)
			print('%s after %s():' % (text, func.__name__))
			return result
		return wrapper
	return decorator if isinstance(args[0],str) else decorator(args[0])

# 直接是修饰方法
@log
def test1():
	print('test1')
test1()
print()
	
# log('custom') 方法的返回值才是修饰方法
@log('custom')
def test2():
	print('test2')
test2()
print()




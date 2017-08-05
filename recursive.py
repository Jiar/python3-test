def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)
	
# 栈溢出
fact(1000)
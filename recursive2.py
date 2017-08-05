def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

# 栈溢出 python没有针对尾递归进行优化
print(fact_iter(1000, 1))
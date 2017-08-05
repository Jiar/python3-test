# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000

# a,b:必选参数、c:默认参数、hh:可变参数、d:命名关键字参数、kw:关键字参数
def f2(a, b, c=0, *hh, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'hh =', hh, 'd =', d, 'kw =', kw)
	
args = (1, 2, 3, 4, 5)
kw = {'d': 99, 'x': '#'}

f2(*args, **kw)
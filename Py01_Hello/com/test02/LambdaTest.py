hap = lambda a, b : a + b
print(hap(1, 5))

gob = lambda a, b : a * b
print(gob(4, 5))

min = (lambda x, y : x if x < y else y)(10, 20)
print(min)

max = (lambda x, y : x if x > y else y)
print(max(10, 20))

a = [(1,'one', 6), (2,'two', 7), (3,'three', 8), (4,'four', 9)]
a.sort(key = lambda a:a[1])
print(a)

b = lambda x : (lambda newx : x + newx)
c = b(100)
print(c)
d = c(90)
print(d)
print(b(100)(90))

e = lambda x : bool(x % 5)
five = [i for i in range(1, 100) if not e(i)]
print(five)

f = lambda x : x if(x % 5 != 0) else None
res = [i for i in range(1,100) if not f(i)]
print(res)
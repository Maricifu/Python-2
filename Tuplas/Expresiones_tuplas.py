a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27, 3), 9)
z, w = x
v = (x, a)

# True
# 12
# (27, 3, 2, 10, 1991)
# 2
# 10
# D
# 27 9
# (2, 10, 1991, 12, 1990)
# (10, 1991, 25, 12)
# 19911990
# 3981
# 1991


print(a<b)
print(y+w)
print(x+a)
print(len(v))
print(v[1][1])
print(c[0][0])
print(z,y)
print(a+b[1:5])
print((a+b)[1:5])
print(str(a[2])+str(b[2]))
print(str(a[2]+b[2]))
print(str((a+b)[2]))
print(str(a+b)[2])

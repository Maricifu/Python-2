a = {5, 2, 3, 9, 4}
b = {3, 1}
c = {7, 5, 5, 1, 8, 6}
d = [6, 2, 4, 5, 5, 3, 1, 3, 7, 8]
e = {(2, 3), (3, 4), (4, 5)}
f = [{2, 3}, {3, 4}, {4, 5}]

# len(c)= 5
# len(set(d))=8
# a&(b|c)={3, 5}
# (a&b)|c={1, 3, 5, 6, 7, 8}
# c-a={8, 1, 6, 7}
# max(e)=(4, 5)
# f[0]<a=true
# set(range(4))&a=4={2, 3}
# (set(range(4))&a)in f=true
# len(set('perro'))=4
# len({'perro'})=1

print(len(c))
print(len(set(d)))
print(a&(b|c))
print((a&b)|c)
print(c-a)
print(max(e))
print(f[0]<a)
print(set(range(4))&a)
print((set(range(4))&a)in f)
print(len(set('perro')))
print(len({'perro'}))

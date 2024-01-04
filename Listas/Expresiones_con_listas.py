# >>> a = [5, 1, 4, 9, 0]
# >>> b = list(range(3, 10)) + list(range(20, 23))
# >>> c = [[1, 2], [3, 4, 5], [6, 7]]
# >>> d = ['perro', 'gato', 'jirafa', 'elefante']
# >>> e = ['a', a, 2 * a]

# - a[2]= 4- si
# - b[9]= 21- no /22
# - c[1][2]= [3, 4, 5]= 5 - si
# - e[0] == e[1]= a - no/false
# - len(c[0])= 2 - si
# - len(e)= 3 - si
# - c[-1]= 6, 7  - si
# - c[-1][+1]= 7 - si
# - c[2:] + d[2:]= 6, 7 , jirafa / elefante
# - a[3:10]= [9, 0]
# - a[3:10:2]= 9, 0, 5, 1, 4, 9, 0, 4 - no / [9]
# - d.index('jirafa')= 2 - si
# - e[c[0][1]].count(5)= 8 - no/2
# - sorted(a)[2]= 4 - si
# - complex(b[0], b[1])= nose / (3+4j)

a = [5, 1, 4, 9, 0]
b = list(range(3, 10)) + list(range(20, 23))
c = [[1, 2], [3, 4, 5], [6, 7]]
d = ['perro', 'gato', 'jirafa', 'elefante']
e = ['a', a, 2 * a]

print(complex(b[0],b[1]))



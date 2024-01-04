def todos_iguales(lista):
    return all(elemento == lista[0] for elemento in lista)

def todos_distintos(lista):
    return len(set(lista)) == len(lista)

# Ejemplos de uso
print(todos_iguales([6, 6, 6]))       # True
print(todos_iguales([6, 6, 1]))       # False
print(todos_iguales([0, 90, 1]))      # False

print(todos_distintos([6, 6, 6]))      # False
print(todos_distintos([6, 6, 1]))      # False
print(todos_distintos([0, 90, 1]))     # True

print(todos_iguales([7, 7, 7, 7, 7, 7, 7, 7, 7]))             # True
print(todos_distintos(list(range(1000))))                     # True
print(todos_iguales([12]))                                    # True
print(todos_distintos(list('hiperblanduzcos')))              # True


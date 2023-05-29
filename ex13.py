def multiplicação(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def par(a):
    return a % 2 == 0
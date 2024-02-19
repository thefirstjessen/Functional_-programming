def dobro(x):
    return x * 2


def quadrado(x):
    return x**2

if __name__ == '__main__':
    #retornar alternadamente o dobro ou quadrado nos numeros de 1 a 10.
    funcs = [dobro,quadrado] * 5
    for func, numero in zip(funcs, range(1,11)):
        print(f'O {func.__name__} de {numero} e {func(numero)}')  
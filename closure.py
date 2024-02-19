def multiply(x):
    def calculate(y):
        return x * y
    return calculate


if __name__ == '__main__':
    the_double = multiply(2)
    the_triple = multiply(3)
    print(the_double,the_triple)
    print(f'The triple of 3 is {the_triple(3)}')
    print(f'The double of 7 is {the_double(7)}')

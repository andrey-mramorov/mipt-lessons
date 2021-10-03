import sys, argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n')
    parser.add_argument('N', nargs='?')

    return parser

def Fib(n):
    if n in (1, 2):
        return 1
    return Fib(n - 1) + Fib(n - 2)

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.n == None and namespace.N != None:
        print(Fib(int(namespace.N)))
    elif namespace.N == None:
        print(Fib(int(namespace.n)))
    else:
        raise ValueError
    
    #print(namespace)
    #print(Fib(int(namespace.n)))

import matrix 
def main():
    a=matrix.Matrix(2,3)
    print('a =')
    print(a)
    b=matrix.Matrix(3,2)
    print('b =')
    print(b)
    print('a+1 = ')
    print(a+1)
    print('a-2 = ')
    print(a-2)
    print('a+b = ')
    print(a+b)
    print('a-b = ')
    print(a-b)
    print('a+a = ')
    print(a+a)
    print('b-b = ')
    print(b-b)
    print('a*2 = ')
    print(a*2)
    print('a*b = ')
    print(a*b)
    print('a.transpose = ')
    print(a.transpose())
    print('a*(b.transpose) = ')
    print(a*(b.transpose()))
    a=matrix.Matrix(4)
    print('a =')
    print(a)
    print('a.determinate = ',a.determinate())

main()
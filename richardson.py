import numpy
import math



def richardson( f, x, n, h ,formula):

    d = numpy.array( [[0] * (n + 1)] * (n + 1), float )
    for i in range( n + 1 ):
        d[i,0] =formula(f,x,h)
        p= 1
        for j in range( 1, i + 1 ):
            p = 4 * p
            d[i,j] = d[i,j-1] + ( d[i,j-1] - d[i-1,j-1] ) / ( p - 1 )
        h =  h/2

    return d[n][n]


if __name__ == '__main__':
    f=lambda x : math.exp(-x) + math.sin(x) + math.pow(x,3)
    x=1.2
    h=0.4
    n=4
    formula = lambda f,x,h:0.5 * (f( x + h ) - f( x - h )) / h
    d = richardson(f, x, n, h,formula)
    print(d)

    f2=lambda x : math.exp(x) * x
    h2=0.2
    x2=2.0
    n2=6
    d = richardson(f2, x2, n2, h2, formula)
    print(d)
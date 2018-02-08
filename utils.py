# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

def fact(n):
    try :
        if n<0:
            fact="/"
            return fact
        fact=n
        while n>1:
        fact = fact*(n-1)
        n-=1
        return fact

                
    except :
        pass
        
def roots(a, b, c):
    
    delta = b**2-4*a*c
        if delta < 0:
            roots=('/')
        elif delta > 0:
            roots=((-b-sqrt(delta))/(2*a),(-b+sqrt(delta))/(2*a))

        elif delta == 0:
            roots=(-b/(2*a))
        return roots
    
    pass
def ff(x):
    return (x**2-1)

def integrate(function, lower, upper):
    m = (lower+upper)/2
    fa = function(lower)
    fb = function(upper)
    fm = function(m)

    return ((upper-lower)/6)*(fa + 4*fm*fb)
    
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    pass

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))

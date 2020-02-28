""" Hi! Welcome to my math library. Why would you use this?
    There's a perfectly good built in one? 
    Oh well, thanks for coming, good luck deciphering what 
    I've coded: I am a fan of dense code. Also, I'm bad at this
    so my code is all over the place. 

    But I am pretty proud of my matrix and polynom classes,
    so thats something. Enjoy your stay. 

    Peace. 

    Miah - jmiah120@gmail.com
"""
###############################################################
## To-do : [ ] Make multinomial class
##         [ ] Finish multivar numint
##         [ ] Make multivar derivative?
##         [X] Make lambda integral (definite)
##         [ ] polynom roots      
##         [ ] eigen nonsense      
##         [X] column space        
##         [X] null space          
##         [ ] vec span          
##         [ ] polynom truediv
##         [ ] Rational class
##         [ ] Diagonalization
##         [X] Multinomial function (diff than class)
##         [X] Gamma func (yeah it counts as math, shut up) 
##         [X] Error function
##         [X] Beta function
##         [ ] Evaluation w work
##              ( ) In written work
##              ( ) In tex format
##         [ ] Make long class
##         [ ] Make recursive functions more robust 
##         [ ] Make generator for different arrangements of a set
##         [ ] Fix matrix/vector nonsense
##         [ ] Etc.
##

import Miahrand as _r

## ------------------------- Some Important Numbers ------------------------- ##

e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977209310141692836819025515108657463772111252389784425056953696
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703
ln2 = 0.69314718055994530941723212145817656807550013436025
LN15 = 0.4054651081081644

## --------------------------- Numeric Functions ---------------------------- ##

def ciel(x,places=0) -> int:
    """ ciel(x:iterable, places) -> iterable
        Returns ceiling of a real number x.
        If x is an iterable, it wil return the
        ceiling of each of its elements.
    """
    assert type(places) is int, f'places arg must be int not {places}'
    k = 10**places
    if type(x) in (float,int):
        return int(k*x)//k if int(x) == x else int(k*x)//k+1
    elif type(x) in (iter,tuple,set,list): return list(ciel(i) for i in x)
    else: raise TypeError('Bro, idk what to do with that')

def floor(x,places=0) -> int:
    """ floor(x:iterable, places) -> iterable 
        Returns floor of a real number x.
        If x is an iterable, it wil return the
        floor of each of its elements.
    """
    assert type(places) is int, f'places arg must be int not {places}'
    k = 10**places
    if type(x) in (float,int): return int(k*x)//k
    elif type(x) in (iter,tuple,set,list): return list(floor(i) for i in x)
    else: raise TypeError('Bro, idk what to do with that')

def fact(n:int) -> int:
    """ Returns n! for non-negative integer n
    """
    assert type(n) is int, 'Argument must be an int. Use gamma for non-ints'
    return ifint(prod(i+1 for i in range(n)))

def perm(n:int, r:int) -> int:
    """ Returns nPr for non-negative integers
        n and r, where n>=r
    """
    assert (type(n) is int) and (type(r) is int), 'Both arguments must be ints'
    assert n >= r,  f'n:{n} must be >= than r:{r}'
    return ifint(prod(i+1 for i in range(n-r,n)))

def choose(n:int, r:int) -> int:
    """ Returns nCr for non-negative integers
        n and r, where n>=r
    """
    assert (type(n) is int) and (type(r) is int), 'Both arguments must be ints'
    assert n >= r,  f'n:{n} must be >= than r:{r}'
    return ifint(perm(n,r)//fact(r))

def multinom(n:int,*rs) -> int:
    """ Returns a multinomial with n and r1,r2,r3...
        Assumes a final r to have sum(r's)=n.
        Note: r's must sum to n or less.
    """
    assert type(n) is int, f'n must be int not {n}'
    for i,r in enumerate(rs):
        assert type(r) is int, f"r's must be integers not {r} (rs[{i}])" 
    rs += (n-sum(rs),)
    return fact(n)//prod(fact(i) for i in rs)
    
def lcm(n:int, m:int) -> int:
    """ Returns the lowest common multiple of
        non-negative integers n and m
    """
    assert (type(n) is int) or (type(m) is int), 'Both arguments must be ints'
    assert n >= 0, f'n:{n} must be >= than 0'
    assert m >= 0, f'm:{m} must be >= than 0'
    nults = [n*(i+1) for i in range(m)]
    mults = [m*(j+1) for j in range(n) if m*(j+1) in nults]
    return min(mults)

def gcd(n:int, m:int) -> int:
    """ Returns the greates common factor of
        integers n and m
    """
    assert (type(n) is int) and (type(m) is int), 'Both arguments must be ints'
    n, m = sorted([abs(m), abs(n)])
    while 0 not in [n, m, n-m]: m, n = n, m % n
    else: return m

def isPrime(n:int) -> bool:
    """ Returns True if n is prime, else False
    """
    if type(n) is not int: raise TypeError('Argument must be int')
    return pfactor(n) == [n] 

def isCoprime(m:int, n:int) -> bool:
    """ Returns True if n is coprime with m,
        else False
    """
    assert (type(n) is int) or (type(r) is int), 'Both arguments must be ints'
    return gcd(n, m) == 1 

def ifint(x):
    """ Returns int form of x if no decimals, else just x
    """
    return int(x) if int(x) == x else x

def isint(x:float) -> bool:
    """ Returns True if x has no decimals, else False
    """
    return int(x) == x 

def dist(x1:float, y1:float, x2:float, y2:float) -> float:
    """ Returns euclidean distance between two points in 2d space
        Use ndist for n-dimensional space
    """
    for i in [x1, y1, x2, y2]:
        assert type(i) in [float, int], f'args must be numbers not {i}'
    return sqrt((x1-x2)**2+(y1-y2)**2)

def ndist(*args) -> float:
    """ Returns euclidean distance between two points in n-d space
    """
    for i in args:
        assert type(i) in [float, int], f'args must be numbers not {i}'
    dim = len(args)//2 #split args in half (x1, y1, z1...)(x2, y2, z2...)
    vec1, vec2 = vec(*args[:dim]), vec(*args[dim:])
    return (vec1 - vec2).mag

    
def prod(seq) -> float:
    """ Returns the product of the elements of seq
    """
    p = 1
    if type(seq) in (int,float): return seq
    for i in seq:
        assert type(i) in (int, float, iter, list, set,
                           tuple), f'Elements must be numbers, dummy. Not {i}'
        p *= prod(i)
    return p

def sqrt(x:float) -> float:
    """ Returns the square root of x
    """
    assert type(x) in (int,float), f'Argument must be a number, not {x}'
    return x**(0.5)

def wsqrt(x:float) -> float:
    """ Same as sqrt, but won't give complex answers
    """
    assert type(x) in (int,float), f'Argument must be a number, not {x}'
    assert x >= 0, f'No real root of {x}'
    return x**(0.5)

def pfactor(n:int) -> list:
    """ Returns prime factorization as a list
        with repeats such that prod(pfactor(n)) == n
        ... theoretically. Breaks down for large numbers
        for unknown reasons.
    """
    assert type(n) is int, 'Argument must be an integer'
    ## Turns out, optimizing to skip known composites doesn't actiually
    ## provide a speed increase 
    for i in range(2, ciel(sqrt(n)) + 1):
        if n % i == 0: return [i] + pfactor(int(n//i))
    return [] if n == 1 else [n] 

def ufactor(n:int) -> list:
    """ Returns a list of prime factors of n such that each
        element in the list is unique. *IN PROGRESS*
    """
    assert type(n) is int, 'Argument must be an integer'
    ret = list(set(pfactor(n)))
    return ret 

def factors(n:int) -> list:
    """ Returns all factors of an integer n
        as a sorted list
    """
    assert type(n) is int, 'Argument must be an integer'
    nults = [n//i for i in range(1, ciel(sqrt(n)) + 1) if n % i == 0]
    mults = [i for i in range(1, ciel(sqrt(n)) + 1) if n % i == 0]
    return sorted(mults + nults)

def isPerfect(n:int) -> bool:
    """ Returns true if an integer n is
        perfect, else false. 
    """
    assert type(n) is int, 'Argument must be an integer'
    return sum(factors(n)) == 2 * n   

def isAbundant(n:int) -> bool:
    """ Returns true if an integer n is
        abundant, else false
    """
    assert type(n) is int, 'Argument must be an integer'
    return sum(factors(n)) > 2 * n    

def isDeficient(n:int) -> bool:
    """ Returns true if an integer n is
        deficient, else false
    """
    assert type(n) is int, 'Argument must be an integer'
    return sum(factors(n)) < 2 * n 

def isPerf(n:int) -> str:
    """ Returns 'Perfect' if n is perfect,
        'Abundant' if n is abundant, or
        'Deficient' if n is deficient
    """
    assert type(n) is int, 'Argument must be an integer'
    if  isDeficient(n): return "Abundant"
    elif  isPerfect(n): return "Perfect"
    elif isAbundant(n): return "Deficient"

def isPower2(x: float) -> bool:
    """ Returns true if x=2^n for some int n
        else false
    """
    assert type(x) in [float, int], f'x must be number not {x}'
    return isint(log(abs(x), base=2))

def isPowern(x:float, n:float) -> bool:
    """ Returns true if x=n^m for some int m
        else false
    """
    assert type(x) in [float, int], f'x must be number not {x}'
    assert type(n) in [float, int], f'n must be number not {n}'
    return isint(log(abs(x), base=n))

def binomexp(a:float, b:float, n:int) -> list:
    """ Returns the expansion of (a+b)^n as a list.
        a and b can be str,int,or float. Let a=b=1 for
        list of coeffs
    """
    if type(a)==type(b)==str:
        return [f"{choose(n,i)}({a}^{n-i})({b}^{i})" for i in range(n+1)]
    elif type(a)==str:
        return [f"{choose(n,i)*(b**(i))}({a}^{n-i})" for i in range(n+1)]
    elif type(b)==str:
        return [f"{choose(n,i)*(a**(n-i))}({b}^{i})" for i in range(n+1)]
    else:
        return [ifint(choose(n,i)*(a**(n-i))*(b**i)) for i in range(n+1)]
    
def quadform(a:float, b:float, c:float) -> tuple:
    """ Returns 0's of the parabola ax^2+bx+c
    """
    try: z1 = (-b - wsqrt(b**2 - 4 * a * c))/(2 * a)
    except: z1 = None
    try: z2 = (-b + wsqrt(b**2 - 4 * a * c))/(2 * a)
    except: z2 = None
    return (ifint(z1), ifint(z2))

def minmax(MIN:float, MAX:float, *args) -> float:
    """ Returns MAX if there exists an arg above MAX
        else MIN if all args are below MIN
        else the max value of args
    """
    return min(max(*args, MIN), MAX)

def maxmin(MIN:float, MAX:float, *args) -> float:
    """ Returns MIN if there exists an arg below MIN
        else MAX if all args are above MAX
        else the min value of args
    """
    return max(min(*args, MAX), MIN)

def Map(thing:float, whichisfrom:float, to:float, \
        From:float, To:float) -> float:
    """ Maps 'thing', which is in the range 'whichisfrom : to'
        to the range 'From : To.'
    """
    destRange = To - From
    srceRange = to - whichisfrom
    thingZ    = (thing - whichisfrom)/srceRange 
    thingEnd  = float(thingZ*destRange + From)
    return thingEnd

def inv_mod(n:int, mod:int) -> int:
    """ Returns the multiplicative inverse of a number n within
        the given modulus.
    """
    v1, v2 = vec(mod, 1, 0), vec(n, 0, 1)
    while v2.x != 0: v1, v2 = v2, v1 - (v1.x//v2.x) * v2
    if v1.x == 1: return v1.z % mod
    else: raise ValueError(f'No inverse found for {n} mod {mod}. :(')

## -------------------------- Exponential Nonsense -------------------------- ##

def scinot(x:float) -> tuple:
    """ Returns x as a tuple (A,n)
        where x = A * 10^n
    """
    A, n = x, 0
    while A >= 10: A, n = A/10, n+1
    while A < 1: A, n = A*10, n-1
    return (A, n)

def binscinot(x:float) -> tuple:
    """ Returns x as a tuple (A,n)
        where x = A * 2^n
    """
    n = 0
    while x >= 1024: x, n = x/1024, n+10
    while x >= 2: x, n = x/2, n+1
    while x < 1: x, n = x*2, n-1
    return (x, n)

def ln(x:float) -> float:
    """ Returns natural log of x
        accurate to about 14 decimal places
    """
    assert x >= 0, 'No real log for x < 0'
    if x > 1.5: 
        n = 0
        while x >= 4.065611775352152e+17: x,n = x/4.065611775352152e+17,n+100
        while x >= 57.6650390625: x,n = x/57.6650390625,n+10
        while x >= 1.5: x,n = x/1.5,n+1
        return n*LN15+ln(x)
    elif x>1:
        a = x+2*((x-(e**x))/(x+(e**x)))
        a += 2*((x-(e**a))/(x+(e**a)))
        return a+2*((x-(e**a))/(x+(e**a)))
    elif x in {1,0}: return {1:0,0:-inf()}[x]
    else: return -ln(1/x)

def log(x:float, base:float=10) -> float:
    "Returns log base [base] of x"
    assert type(x) in (int, float), f'x must be a number not {x}'
    assert type(base) in (int, float), f'base must be a number not {base}'
    assert x >= 0, f'x must be greater than 0 not {x}' 
    assert base >= 0, f'base must be greater than 0 not {base}' 
    return ln(x)/ln(base)

## ------------------------ Trigonometric Functions ------------------------- ##

######################################
## Todo (Trig):
##      [ ] arcsin
##      [ ] arccos
##      [ ] arctan
##      [ ] arccsc
##      [ ] arcsec
##      [ ] arccot
##      [ ] archsin
##      [ ] archcos
##      [ ] archtan
##      [ ] archcsc
##      [ ] archsec
##      [ ] archcot
##
##

def sin(x:float, precision:int = 20) -> float:
    """ Returns sin(x) for a real number x in radians
    """
    assert type(x) in (int, float), f'x must be a number not {x}'
    x %= (2 * pi) # x = x % (2*pi)
    return sum(((-1)**i) * (x**(2 * i + 1))/fact(2 * i + 1)
               for i in range(0, precision))

def cos(x:float, precision:int = 20) -> float:
    """ Returns cos(x) for a real number x in radians
    """
    x %= (2 * pi)
    return sum((-1)**i * x**(2 * i)/fact(2 * i) for i in range(0, precision))

def tan(x:float) -> float:
    """ Returns tan(x) for a real number x in radians
    """
    x %= pi
    return inf() if cos(x) == 0 else sin(x) / cos(x)

def csc(x:float) -> float:
    """ Returns csc(x) for a real number x in radians
    """
    return inf() if sin(x) == 0 else 1 / sin(x)

def sec(x:float) -> float:
    """ Returns sec(x) for a real number x in radians
    """
    return inf() if cos(x) == 0 else 1 / cos(x)

def cot(x:float) -> float:
    """ Returns cot(x) for a real number x in radians
    """
    return inf() if sin(x) == 0 else cos(x) / sin(x)

def sinh(x:float) -> float:
    """ Returns sinh(x) for a real number x
    """
    return 0.5 * (e**x - e**(-x))

def cosh(x:float) -> float:
    """ Returns cosh(x) for a real number x
    """
    return 0.5 * (e**x + e**(-x))

def tanh(x:float) -> float:
    """ Returns tanh(x) for a real number x
    """
    return inf() if cosh(x) == 0 else sinh(x) / cosh(x)

def csch(x:float) -> float:
    """ Returns csch(x) for a real number x
    """
    return inf() if sinh(x) == 0 else 1 / sinh(x)

def sech(x:float) -> float:
    """ Returns sech(x) for a real number x
    """
    return inf() if cosh(x) == 0 else 1 / cosh(x)

def coth(x:float) -> float:
    """ Returns coth(x) for a real number x
    """
    return inf() if sinh(x) == 0 else cosh(x)/sinh(x)

def arcsin(x):
    "Returns arcsin(x) in radians for a real number x Doesn't work rn "
    if x < 0: return -arcsin(-x)
    elif x == 1: return pi/2
    nults = [(2*i-1)**2 for i in range(2,n)]
    mults = (x**(2 * n + 1))*prod(nults/fact(2 * n + 1) for n in range(85))
    return sum(mults)

## --------------------- Some Other Important Functions --------------------- ##
    ## aka: "I can code that? no i cant but I put
    ## it in anyway cause better to have a shitty
    ## thing done by me than a good thing I have to
    ## rely on someone else for" t.m.

def numint(func, a:float, b:float, n:int=1000, rule:str='simp') -> float:
    """ Returns the integral of func from a to b
        with n rects/trapz/parabs.
    """
    delta = (b-a)/n
    if   rule == 'simp' :
        return delta/6 * (2 * sum(func(a + delta * x * 0.5)
                        for x in range(1, 2*n, 2)) + 4 * sum(func(a + delta * x * 0.5)
                        for x in range(2, 2*n, 2)) + sum((func(a), func(b))))
    elif rule == 'zoid' :
        return delta*(sum(func(a + delta * x)
                          for x in range(1, n)) + sum((func(a), func(b))) * 0.5)
    elif rule == 'mid'  :
        return delta * sum(func(a + delta*(x + 0.5)) for x in range(n))             
    elif rule == 'left' :
        return delta * sum(func(a + delta * x) for x in range(n))
    elif rule == 'right':
        return delta * sum(func(a + delta * (x + 1)) for x in range(n))
    
def gamma(z:float) -> float:
    """ Returns Gamma function of x.
        Accurate to about 13 decimal places.
    """
    qs = [75122.6331530, 80916.6278952, 36308.2951477,
          8687.24529705, 1168.92649479, 83.8676043424, 2.50662827511]
    a = sum(q * (z**n) for n, q in enumerate(qs))
    b = prod(z + n for n, q in enumerate(qs))
    c = ((z + 5.5)**(z + 0.5)) * e**(-z-5.5)
    if isint(z): return fact(abs(z - 1))
    elif z > 1.5: return (z - 1)*gamma(z - 1)
    else:
        r = ((1 - 5.234230557400197e-13) * (1 + 6.863196879500968e-15))
        return (a/b) * c / r

def beta(a:float, b:float) -> float:
    """ Returns Beta function of x
    """
    return gamma(a) * gamma(b) / gamma(a + b)

def erf(x:float) -> float:
    """ Returns the error function at x.
        Accurate to the given decimal
    """
    if x >= 0:
        p, a1, a2, = 0.3275911, 0.254829592, -.284496736,
        a3, a4, a5 = 1.421413741, -1.453152027, 1.061405429
        t = 1/(1 + p * x)
        return round(1 - (a1*t+a2*t**2+a3*t**3+a4*t**4+a5*t**5) * e**(-(x**2)), 6)
    else: return -erf(-x)

## ---------------------------- polynomial Class ---------------------------- ##
    
class polynom:
    """ Creates a polynomial object with args as the coefficients and
        term degree in ascending order (little endian)
    """
    def __init__(self, *args):
        self.args = list(args) if args != () else [0] 

    @property
    def degree(self) -> int:
        return len(self.args) - 1
        
    @property
    def func(self) -> 'function':
        return lambda x: sum(j * (x**i) for i, j in enumerate(self.args))
        
    def __add__(self, other:'polynom') -> 'polynom':
        """ (self, other:float) -> 'polynom'
            Returns self + polynom
        """
        if type(other) == polynom:
            len1, len2 = len(self.args), len(other.args)
            arg1, arg2 = self.args, other.args
            if len1 != len2:
                dif = abs(len1 - len2) 
                arg1 += (0,) * dif
                arg2 += (0,) * dif
            args = [i + j for i, j in zip(self.args, other.args)]
        elif type(other) in [int, float]:
            args = self.args
            args[0] += other
        return polynom(*args)
    
    def __sub__(self, other:'polynom') -> 'polynom':
        """ (self, other:float) -> 'polynom'
            Returns self - polynom
        """
        if type(other) == polynom:
            len1, len2 = len(self.args), len(other.args)
            arg1, arg2 = self.args, other.args
            if len1 != len2:
                dif = abs(len1 - len2) 
                arg1 += (0,) * dif
                arg2 += (0,) * dif
            args = [i - j for i, j in zip(self.args, other.args)]
        elif type(other) in [int, float]:
            args = self.args
            args[0] -= other
        return polynom(*args)

    def __mul__(self, other) -> 'polynom':
        """ (self, other:float) -> 'polynom'
            Returns self * polynom
        """
        if type(other) == polynom:
            new_arg = []
            for i, j in enumerate(self.args):
                #the 0 tuple ensures proper degree, the j*k ensures proper coefficients
                arg = [0 for k in range(i)] + [j * k for k in other.args]
                new_arg = polynom._tup_add(arg, new_arg) 
        elif type(other) in [int, float]:
            new_arg = [other * i for i in self.args]
        return polynom(*new_arg)

    def __pow__(self, n:int) -> 'polynom':
        """ Returns self**n for an integer n, returns 1 for n<=0
        """
        return prod(self for i in range(n)) if n > 0 else polynom(1)
    
    def __floordiv__(self, other:'polynom') -> 'polynom':
        """ (self, other:float) -> 'polynom'
            Returns self//polynom
        """
        if type(other) == polynom:
            arg1 = polynom._tup_strip(self.args)
            arg2 = polynom._tup_strip(other.args)
            lst = [0]*(self.degree - other.degree + 1)
            i = -1
            while len(arg1) >= len(arg2):
                i += 1
                c = arg1[-1]/arg2[-1]
                lst[i] = c
                tuptup = tuple(0 for i in range(len(arg1)-len(arg2)))
                tuptup += tuple(-c*i for i in arg2)
                arg1 = polynom._tup_add(arg1, tuptup)
                arg1 = polynom._tup_strip(arg1)
            lst.reverse()
            tup = tuple(lst)
        elif type(other) in [int, float]:
            tup = tuple(i/other for i in self.args)
        return polynom(*tup)
    
    def __truediv__(self, other:'polynom') -> 'polynom':
        """ (self, other:float) -> 'polynom'
            Returns self/n for a number n, polynom functionality coming soon
        """
        ########################
        ## do this eventually ##
        ########################
        if type(other) == polynom:
            pass
        elif type(other) in {int, float}:
            tup = tuple(i/other for i in self.args)
            return polynom(*tup)

    def __mod__(self, other:'polynom') -> 'polynom':
        """ (self, other:float) -> 'polynom'
            Returns self % polynom
        """
        p = self - ((self // other) * other)
        return polynom(*(polynom._tup_strip(p.args)))

    def __radd__(self, other:'polynom') -> 'polynom':
        """ (self, other:float) -> 'polynom'
            returns other + self
        """
        return self + other
    
    def __rsub__(self, other:'polynom') -> 'polynom':
        """ __rsub__(self, other:float) -> 'polynom'
            returns other - self
        """
        return - self + other

    def __neg__(self) -> 'polynom':
        """ Returns -self
        """
        args = [-i for i in self.args]
        return polynom(*args)

    def __rmul__(self, other:'polynom') -> 'polynom':
        """ (self, other:float) -> 'polynom'
            returns other * self
        """
        return self * other

    def __str__(self) -> str:
        """ Returns self as we'd write it
        """
        s = ""
        for i, j in enumerate(self.args):
            if i == 0 and j != 0: s += f"{j} + "
            elif i == 1: s += "x + " if j==1 else f"{j}x + " if j!=0 else ''
            else: s += f"x^{i} + " if j==1 else f"{j}x^{i} + " if j!=0 else '' 
        return s[:-3]

    def __call__(self, arg:float) -> float:
        """ Returns self(arg) => f(x)
        """
        return self.func(arg)
    
    def __repr__(self) -> str:
        """ Returns self as command
        """
        return f"polynom{tuple(self.args)}"
    
    def __eq__(self, other:'polynom') -> bool:
        """ Returns True if self=polynom else False
        """
        return self.args == other.args
    
    def __lt__(self, other:'polynom') -> bool:
        """ Returns True if self<polynom else False
        """
        return self.degree < other.degree
    
    def __le__(self, other:'polynom') -> bool:
        """ Returns True if self<=polynom else False
        """
        return self.degree <= other.degree
    
    def __ne__(self, other:'polynom') -> bool:
        """ Returns True if self!=polynom else False
        """
        return self.degree != other.degree 
    
    def __ge__(self, other:'polynom') -> bool:
        """ Returns True if self>=polynom else False
        """
        return self.degree > other.degree 
    
    def __gt__(self, other:'polynom') -> bool:
        """ Returns True if self>polynom else False
        """
        return self.degree >= other.degree
    
    def __getitem__(self, item:int) -> str:
        """ Returns the requested term
        """
        c, e = self.args[item], item 
        if c == 0: return "0"
        elif c == 1 and e != 1: return f"x^{e}"
        elif e == 1: return f"{c}x"
        elif e == 0: return f"{c}"
        else: return f"{c}x^{e}"
        
    def __or__(self, polynom):
        ## use to find intersection of two polynoms
        pass
    
    def integral(self, a:float, b:None) -> 'polynom':
        """ (self, a:float, b:float) -> float:
            Returns the integral from a to b of self, if a or b
            are none, returns polynom of indefinite integral
        """
        intfunc = lambda x: sum(j*(x**(i+1))/(i+1)
                                for i, j in enumerate(self.args))
        if a == b == None:
            new_args = (0,) + tuple(j/(i+1) for i, j in enumerate(self.args))
        elif a == None:
            new_args = (intfunc(b),) + tuple(-j/(i+1)
                                           for i, j in enumerate(self.args))
        elif b == None:
            new_args = (intfunc(a),) + tuple(j/(i+1)
                                           for i, j in enumerate(self.args))
        else:
            return intfunc(b) - intfunc(a)
        return polynom(*new_args)
    
    def ddx(self) -> 'polynom':
        """ Returns df/dx, the derivative of the polynom
        """
        new_args = tuple(j * i for i, j in enumerate(self.args))[1:]
        return polynom(*new_args)
    
    def roots(self, precision:float = 1e-10) -> tuple:
        """ Returns the 0's of the polynom
            if constant: -> bool
            if linear: -> x-value of the 0
            if quadratic: -> all real 0's
            else: -> None
        """
        if len(self.args) == 1:
            return (self.args[0] == 0,)
        elif len(self.args) == 2:
            return (-self.args[0]/self.args[1],)
        elif len(self.args) == 3:
            return quadform(*reversed(self.args))
        else:
            z = ifint(round(self.newtonsmethod(0, precision), 10))
            p = self//polynom(z, -1)
            return p.roots() + (z,)
                
    def newtonsmethod(self, x0:float, precision:float = 1e-10) -> float:
        """"""
        ddx = self.ddx()
        xn, xnp1= x0, x0 - (self(x0)/ddx(x0))
        while abs(self(xn) - self(xnp1)) >= precision:
            try:
                xnp1, xn = xnp1 - (self(xnp1)/ddx(xnp1)), xnp1
                
            except ZeroDivisionError:
                print(f'Sorry, something went wrong. Check newtonsmethod')
                print(f'polynom = {self}')
                print(f'derivative: {ddx}')
                print(f'xn = {xn}')
                return
            
            except KeyboardInterrupt:
                print(f'xn = {xn}')
                print(f'xnp1 = {xnp1}')
                return 
                
        return xnp1
        
    @classmethod
    def zero(cls) -> 'polynom':
        """ Returns the 0 polynom
        """
        return cls(0)
    
    @staticmethod
    def _tup_add(tup1:tuple, tup2:tuple) -> tuple:
        """ Adds two tuples the vector way
        """
        tup1 = tuple(tup1)
        tup2 = tuple(tup2)
        arg1 = len(tup1)
        arg2 = len(tup2)
        dif  = abs(arg1 - arg2)
        if arg1 != arg2:
            tup1 += (0,)*(dif)
            tup2 += (0,)*(dif)
        args = tuple(i+j for i,j in zip(tup1,tup2))
        return args

    @staticmethod
    def _tup_strip(tup:tuple) -> tuple:
        """ Removes trailing 0's in a tuple
        """
        try:
            while tup[-1] == 0: tup = tup[:-1]
            return tuple(tup)
        except IndexError: return (0,)

## ---------------------- Multivariable Equation Class ---------------------- ##      

class Multivar:
    """ A class for multivariable functions.
        Not currently operable. 
    """
    def __init__(self, expr, *params):
        s = ''
        for i in expr:
            s += '**' if i=='^' else i
        exec("self.func = lambda {}: {}".format(",".join(params),s))
        self.s = expr
        self.params = params
        
    def __repr__(self):
        return self.s

    def __str__(self):
        return self.s

    def numint(self,bounds,n=1000,rule='mid'):
        """ Returns the integral of func from the bounds
            with n rects per dimension. bounds should be a
            dict with key->param, val->(a,b)
        """
        pass
        ##        for i in bounds:
        ##            exec(f"delta_{i} = {(bounds[i][0]-bounds[i][0])/n}")
        ##            for x in range(*bounds[i]):
        ##                pass
        ##        elif rule == 'mid'  : return delta*sum(func(a+delta*(x+1/2)) for x in range(n))             
        ##        elif rule == 'left' : return delta*sum(func(a+delta*x) for x in range(n))
        ##        elif rule == 'right': return delta*sum(func(a+delta*(x+1)) for x in range(n))
    
#--------------------Rational Equation Class---------------------
    ## aka: "the thing that I'm totally gonna get to
    ## no trust me im definitely gonna get to it eventually
    ## no, i mean right nows not great but I'm definitely gonna
    ## get to it. " t.m.

class Rational:
    def __init__(num,denom):
        pass
    def __add__(self, polynom):
        pass
    def __sub__(self, polynom):
        pass
    def __mul__(self,polynom):
        pass
    def __pow__(self, n):
        pass
    def __floordiv__(self,polynom):
        pass
    def __truediv__(self,polynom):
        pass
    def __mod__(self,polynom):
        pass
    def __str__(self):
        pass
    def __call__(self,arg):
        pass
    def __repr__(self):
        pass
    def __eq__(self,polynom):
        pass
    def __lt__(self,polynom):
        pass
    def __le__(self,polynom):
        pass
    def __ne__(self,polynom):
        pass
    def __ge__(self,polynom):
        pass
    def __gt__(self,polynom):
        pass

#------------------ Matrix Handler Class ----------------------       

class matrix:
    """ (rows, columns, array) -> matrix
        (*vecs) -> matrix
        (2D list) -> matrix
        A class for making Matrices.
        Constructors : __init__, fromVecs, fromMatrix, zero, I, elementary
        Methods : copy, det, cofactor, concat, colelim, rowelim, inv, trans,
        --------- scale, elim, ref, rref, colspace, nulspace
        Attributes : matrix, array, rows, columns, T
    """ 
    def __init__(self, *args):
        if type(args[0]) is list:
            self.matrix = matrix.fromMatrix(list(args)).matrix
        elif type(args[0]) is vec:
            self.matrix = matrix.fromVecs(*args).matrix
        else:
            rows, columns, *array = args
            if len(array) < rows * columns:
                array += (0,)*(rows * columns - len(array))
            if type(array[0]) is list:
                array = array[0]
            self.matrix  = [list(array[ i*columns : (i+1)*columns ])
                            for i in range(rows)]

    @classmethod
    def fromVecs(cls, *vecs) -> 'matrix':
        """ Returns a matrix with the given vectors as the 
            columns of the matrix
        """
        vec_f = vecs[0]
        for vec in vecs[1:]: vec_f |= vec
        return vec_f

    @classmethod
    def fromMatrix(cls, matrix:list) -> 'matrix':
        """ Returns a matrix from a given 2-dimensional list
            eg: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        """
        ro = len(matrix)
        co = max(len(i) for i in matrix)
        ## Normalize 
        for ind, row in enumerate(matrix):
            matrix[ind] = list(row) + [0] * (co - len(row))
        ## Setup 
        args = [matrix[y][x] for y in range(ro) for x in range(co)]
        return cls(ro, co, *args)        
    
    @classmethod
    def zero(cls, n:int, m:int) -> 'matrix':
        """ Returns the zero matrix with n rows and m columns
        """
        return cls(n, m, *(0 for i in range(n * m)))
    
    @classmethod
    def I(cls, n:int) -> 'matrix':
        """ Returns the identity matrix of size n
            eg: matrix.I(3)
            >>> [1, 0, 0]
            ... [0, 1, 0]
            ... [0, 0, 1]
        """
        array = ()
        for i,j in [(i,j) for i in range(n) for j in range(n)]:
            array += (0,) if i != j else (1,)
        return cls(n,n,*array)

    @classmethod
    def elementary(cls, n:int, row:int, column:int, value:float):
        """ Returns an elementary matrix E with E[row][column]
            set to value.
        """
        E = matrix.I(n)
        E[row][column] = value
        return E

    @property
    def array(self) -> list:
        """ A one dimensional representation of the matrix
        """
        return [self[y][x] for y in  range(self.rows)
                for x in range(self.columns)]

    @property
    def rows(self) -> int:
        """ The number of rows in the matrix
        """
        return len(self.matrix)

    @property
    def columns(self) -> int:
        """ The number of columms in the matrix
        """
        return len(self.matrix[0])

    @property
    def T(self) -> 'matrix':
        """ The transpose of the matrix. Same as matrix.trans()
        """
        return self.trans()
        
    def __str__(self) -> str:
        """ Returns a formatted representaation of the matrix
        """
        ## Mess with the formatting on this, make it look better
        try:
            return "".join(f"{list(ifint(round(x,2)) for x in i)}\n" for i in self)
        except:
            return repr(self)
        
    def __repr__(self) -> str:
        """ Returns an accurate representaation of the matrix
        """
        return "".join(f"{i}\n" for i in self)

    def __add__(self, other:'matrix') -> 'matrix':
        """ Returns self + other
        """
        assert (self.columns, self.rows) == (other.columns, other.rows), "Matrices must have the same size to add them"
        new = [self[y][x] + other[y][x] for y in range(self.rows)
               for x in range(self.columns)]
        return matrix(self.rows, self.columns, *new)    

    def __sub__(self, other:'matrix') -> 'matrix':
        """ Returns self - other
        """
        assert (self.columns, self.rows) == (other.columns, other.rows), "Matrices must have the same size to subtract them"
        new = [self[y][x] - other[y][x] for y in range(self.rows)
               for x in range(self.columns)]
        return matrix(self.rows, self.columns, *new)
    
    def __rmul__(self, other:float) -> 'matrix':
        """ Returns scalar * self if other is a number
            else raises an error
        """
        if type(other) is not matrix:
            return self * other
        else:
            raise Exception('Something went wrong in matrix multiplication')
    
    def __mul__(self, other) -> 'matrix':
        """ Returns self * other
        """
        if type(other) in [float,int]:
            args = [self[y][x] * other for x in range(self.columns)
                    for y in range(self.rows)]
            return matrix(self.rows, self.columns, *args)
        elif self.columns != other.rows:
            raise ArithmeticError("Matrices not compatible for multiplication")
        new = [sum(matrix.__vec_mul(self[y], other[None][x]))
               for y in range(self.rows)
               for x in range(other.columns)]
        return matrix(self.rows, other.columns, *new)

    def __truediv__(self, val):
        """"""
        if type(val) in (int, float):
            new = [i/val for i in self.array]
            return matrix(self.rows, self.columns, new)
        else:
            raise ValueError(f'No division defined for matrices and {type(val)}')

    def __floordiv__(self, val):
        """"""
        if type(val) in (int, float):
            new = [i//val for i in self.array]
            return matrix(self.rows, self.columns, new)
        else:
            raise ValueError(f'No division defined for matrices and {type(val)}')

    @staticmethod
    def __vec_mul(V1, V2) -> list:
        """ Returns haddamard product of the given vectors
        """
        x = [i * j for i, j in zip(V1, V2)]
        return x
        
    def __pow__(self, n:int) -> 'matrix':
        """ Returns a self ** n
        """
        return prod(self for i in range(n))
    
    def __eq__(self, other:'matrix') -> bool:
        """ Returns self == other
        """
        return self.matrix == other.matrix
    
    def __ne__(self, other:'matrix') -> bool:
        """ Returns self != other
        """
        return self.matrix != other.matrix
    
    def __getitem__(self, item:int) -> list:
        """ (self, item:None) -> 'matrix'
            Use [None][:COLUMN:] to access a column
        """
        ## Work on this
        if item == None:
              return self.trans()
        else: return self.matrix[item]

    def __contains__(self, val):
        return val in self.array
        
    def __setitem__(self, entry:int, value):
        """ Sets a given entry to value *IN PLACE*
        """
        self.matrix[entry] = value
        
    def __mod__(self, value:float) -> int:
        """ Returns arg % value for arg in the matrix
        """
        if type(value) in [float, int]:
            args = [i % value for i in self.array]
            return matrix(self.rows, self.columns, *args)

    def __or__(self, other: 'matrix') -> 'matrix':
        """ Returns a matrix of self augmented with other
        """
        concatmat = [i + j for i, j in zip(self, other)]
        args      = [concatmat[j][i] for j in range(self.rows)
                     for i in range(self.columns + other.columns)]
        return matrix(self.rows, self.columns + other.columns, *args)
        pass
    
    def copy(self) -> 'matrix':
        """ Returns a copy of the matrix
        """
        return matrix(self.rows, self.columns, *self.array)
    
    def det(self) -> float:
        """ Returns the determinant of self
        """
        p = 1
        if self.columns == self.rows:
            new = self.copy()
            lim = min(new.rows, new.columns)
            for i in range(lim):
                for j in range(i + 1, lim):
                    try:
                        new = new.elim(j, i, new[j][i]/new[i][i])
                    except ZeroDivisionError:
                        new[i], new[i + 1] = new[i + 1], new[i]
                        p = -p
            return ifint(round(p * prod(new[i][i] for i in range(lim)), 5))

    def old_det(self) -> float:
        if self.columns == self.rows:
            if self.columns == 2:
                a, b, c, d = self.array
                return a * d - b * c

            return sum( [self[0][j] * (-1)**j *
                         self.cofactor(0, j).old_det()
                         for j in range(self.columns)] )
                    

    def cofactor(self, i:int, j:int) -> 'matrix':
        """ Returns a copy of the matrix with the ith row
            and jth column removed.
        """
        mat = self.copy().colelim(j).rowelim(i)
        return mat

    def concat(self, other:'matrix') -> 'matrix':
        """ Returns a matrix of self concatenated with other
        """
        concatmat = [i + j for i, j in zip(self, other)]
        args      = [concatmat[j][i] for j in range(self.rows)
                     for i in range(self.columns + other.columns)]
        return matrix(self.rows, self.columns + other.columns, *args)
    
    def colelim(self, column:int) -> 'matrix':
        """ Yeets column from the matrix
        """
        new = self.copy()
        for i in new: i.pop(column)
        return new
    
    def rowelim(self, row:int) -> 'matrix':
        """ Yeets row from the matrix
        """
        new = self.copy()
        new.matrix.pop(row)
        return new
    
    def inv(self, mod:int = None) -> 'matrix':
        """ Returns the inverse of the matrix
        """
        if self.rows != self.columns or self.det() == 0: return None # :'(
        interim = (self | matrix.I(self.rows)).rref(mod)
        for i in range(self.columns): interim = interim.colelim(0)
        return interim if mod is None else interim % mod

    def trans(self) -> 'matrix':
        """ Returns transpose matrix
        """
        new_args = [self[j][i] for i in range(self.columns)
                    for j in range(self.rows)]
        return matrix(self.columns, self.rows, *new_args)

    def scale(self, scalar:float, line:int, linewrite:int = None) -> 'matrix':
        """ Multiplies line of matrix by scalar and writes to linewrite
        """
        linewrite      = line if linewrite is None else linewrite 
        line           = self[line]
        new            = self.copy()
        new[linewrite] = [ifint(scalar * i) for i in line]
        return new

    def elim(self, linewrite:int, line:int, scalar:float = 1) -> 'matrix':
        """ Subtracts scalar*line from linewrite and writes to linewrite
        """
        line           = self[line]
        new            = self.copy()
        new[linewrite] = [i - scalar * j for i, j in zip(new[linewrite], line)]
        return new

    def ref(self, mod:int = None) -> 'matrix':
        """ Returns matrix in Roe-Echelon form
        """
        new = self.copy()
        lim = min(new.rows, new.columns)
        for i in range(lim):
            try:
                inv = 1/new[i][i] if not mod else inv_mod(new[i][i], mod)
                new = new.scale(inv, i)
            except ZeroDivisionError:
                new = new.scale(1, i)
            for j in range(i + 1, lim):
                new = new.elim(j, i, new[j][i])
        for i in range(new.rows - new.columns):
            for j in range(new.columns):
                new = new.elim(new.columns+i, j, new[new.columns+i][j])
            new = new.scale(1, new.columns+i)
        return new if mod is None else new % mod

    def rref(self, mod:int = None) -> 'matrix':
        """ Returns matrix in reduced Roe-Echelon form
        """
        ref = self.ref(mod)
        lim = min(ref.rows, ref.columns)
        for i in range(ref.rows):
            for j in range(i+1, lim):
                ref = ref.elim(i, j, ref[i][j])
            ref = ref.scale(1, i)
        return ref if mod is None else ref % mod

    def demean(self) -> 'matrix':
        """"""
        vecs = [vec(*self[None][i]) for i in range(self.columns)]
        mean = vec.zero(self.rows)
        for v in vecs: mean += v
        mean /= self.columns
        return matrix(*[v - mean for v in vecs])
    
    def colspace(self) -> int:
        """ Returns the dimension of the column space of the matrix 
        """
        interim = self.rref()
        count   = 0
        for row in interim:
            for entry in row:
                if entry != 0:
                    count += 1
                    break
        return count
    
    def nulspace(self) -> int:
        """ Returns the dimension of the null space of the matrix
        """
        return self.rows - self.colspace()

    def LU(self) -> ('matrix', 'matrix'):
        """ Returns the LU factorization of the matrix
            Not working yet
        """
        ###
        ###
        ### Come back to this 
        ###
        ###
        A = self.copy()
        elems = []
        for i in range(A.rows):
            B = self.copy()        
            for j in range(i + 1, A.rows):
                elems.append(matrix.elementary(
                    A.rows, j, i, -(B[j][i])/(B[i][i])))
            for e in elems:
                B = e * B

        return elems
        
    def eigenvalues(self) -> float:
        """"""
        A = self.copy()
        for i in range(A.rows):
            A[i][i] = polynom(A[i][i], -1)
        return A.old_det()
    
        
## -------------------------- Vector Handler Class -------------------------- ##       

class vec(matrix):
    """ A class to make vectors. There is no limit to how many arguments
        you can store, but there are only properties for x, y, and z.
        Constructors : __init__, zero, random
        Methods : cross, dot, normalize, see matrix for more.
        Attributes : x, y, z        
    """
    def __init__(self, *args):
        if len(args) == 0: args = [0]
        super().__init__(len(args), 1, *args)

    @property
    def x(self):
        """ Returns the x value of the vec
        """
        return self[0][0]

    @x.setter
    def x(self, val:float) -> None:
        """ Sets the x value of a vec
        """
        self[0][0] = val

    @property
    def y(self):
        """ Returns the y value of the vec
        """
        assert len(self) >= 2, 'No y value for this vec'
        return self[1][0]

    @y.setter
    def y(self, val:float) -> None:
        """ Sets the y value of a vec
        """
        self[1][0] = val

    @property
    def z(self):
        """ Returns the z value of the vec
        """
        assert len(self) >= 3, 'No z value for this vec'
        return self[2][0]

    @z.setter
    def z(self, val:float) -> None:
        """ Sets the z value of a vec
        """
        self[2][0] = val

    @property
    def mag(self) -> float:
        """ Returns the magnitude of the vec
        """
        return sqrt(sum(i**2 for i in self.array))

    @property
    def array(self):
        return [i[0] for i in self]
    
    @classmethod
    def zero(cls, n:int) -> 'vec':
        """ Returns an n-Dimensional 0 vector
        """
        args = [0] * n
        return cls(*args)

    @classmethod
    def random(cls, n:int) -> 'vec':
        """ Returns a random, n-Dimensional, unit vector
        """
        args = [_r.random() for _ in range(n)]
        return cls(*args).normalize()

    def __repr__(self) -> str:
        """ Returns a representation of vec
        """
        argstrs = [f'{i}' for i in self.array]
        return f'<{" ".join(argstrs)}>'

    def __str__(self):
        """ Returns a formatted representation of vec
        """
        argstrs = [f'{ifint(round(i, 2))}' for i in self.array]
        return f'<{" ".join(argstrs)}>'
    
    def __add__(self, other):
        """ Returns self + other
        """
        if type(other) is vec:
            return vec(*[i+j for i,j in zip(self.array, other.array)])
        else:
            return other + self
    
    def __sub__(self, other):
        """ Returns self - other
        """
        if type(other) is vec:
            return vec(*[i-j for i,j in zip(self.array, other.array)])
        else:
            return other + self
    
    def __mul__(self, other):
        """ self * vec -> dot product
            self * matrix -> vec
            self * number -> vec
        """
        if type(other) is vec:
            sargs = self.array + [0]*abs(len(self.array) - len(other.array))
            oargs = other.array + [0]*abs(len(self.array) - len(other.array))
            return sum([i * j for i, j in zip(sargs, oargs)])
        elif type(other) is matrix:
            return (other.T * v.T).T
        elif type(other) in (int, float):
            return vec(*[other * i for i in self.array])
        else:
            return other * self

    def __rmul__(self, other):
        if type(other) in (int, float):
            return vec(*[other * i for i in self.array])
        elif type(other) is matrix:
            mat = matrix.__mul__(other, self)
            arr = mat.array
            return vec(*arr)
        else:
            raise TypeError("I don't yet know how to handle this case, try not being a little bitch?")
    
    def __truediv__(self, val):
        """"""
        if type(val) in (int, float):
            new = [i/val for i in self.array]
            return vec(*new)
        else:
            raise ValueError(f'No division defined for matrices and {type(val)}')

    def __floordiv__(self, val):
        """"""
        if type(val) in (int, float):
            new = [i//val for i in self.array]
            return vec(*new)
        else:
            raise ValueError(f'No division defined for matrices and {type(val)}')

    def __len__(self) -> int:
        """ Returns the dimension of the vector
        """
        return len(self.array)

    def cross(self, other:'vec') -> 'vec':
        """ Returns the cross product of self and other
            only works in 3 dimensions
        """
        x, y, z, *_ = self.array
        a, b, c, *_ = other.array
        return vec((y*c-b*z), (x*c-a*z), (x*b-a*y))
    
    def dot(self, other:'vec') -> float:
        """ Returns the dot product of self and other
        """
        return sum((self * other).array)

    def normalize(self, scalar:float = 1) -> 'vec':
        """ Returns a new vec with mag = scalar
        """
        length = self.mag
        if length == 0: raise ValueError('Cannot normalize vector of length 0')
        args = [scalar * i/length for i in self.array]
        return vec(*args)
    
    @staticmethod
    def span(*vecs) -> int:
        """ Returns the dimension of the space spanned by the given vecs
        """
        checked = [vecs[0]]
        dim = len(vecs[0])
        for v in vecs:
            assert len(v) == dim, f'All vecs must have the same dimension. Offender {repr(v)}'
            for u in checked:
                if u.normalize() == v.normalize():
                    break
            else:
                checked.append(v)
        return len(checked)

    def copy(self) -> 'vec':
        """ Returns a copy of the vec
        """
        return vec(*self.array)
    
## -------------------------------- Infinity -------------------------------- ##          

class _inf:
    """ Object to represent dummy thicc numbers
    """
    def __init__(self) -> 'inf':
        self.sign = ''
        
    def __str__(self) -> str:
        return f'{self.sign}inf'
    
    def __repr__(self) -> str:
        return f'{self.sign}inf'
    
    def __neg__(self) -> str:
        ret = inf()
        ret.sign = '-'
        return ret
    
    def __pos__(self) -> str:
        ret = inf()
        ret.sign = ''
        return ret
    
    def __mul__(self, other) -> 'inf':
        return NaN() if other == 0 else self if other > 0 else -self
    
    def __truediv__(self, other) -> 'inf':
        return NaN() if type(other) is inf else self if other > 0 else -self
    
    def __floordiv__(self, other) -> 'inf':
        return NaN() if type(other) is inf else self if other > 0 else -self
    
    def __add__(self, other):
        return self if type(other) != inf \
               else self if other.sign == self.sign else NaN()

    def __sub__(self, other):
        return self if type(other) != inf \
               else NaN() if other.sign == self.sign else self
    
    def __rmul__(self, other):
        return self * other
    
    def __rtruediv__(self, other):
        return NaN() if type(other) is inf else 0
    
    def __rfloordiv__(self, other):
        return NaN() if type(other) is inf else 0
    
    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return  -self + other

    def __gt__(self, other):
        if type(other) != inf and self.sign == '': return True
        elif other.sign == '-' and self.sign == '': return True
        else: return False
        
    def __ge__(self, other):
        return self > other
    
    def __eq__(self, other):
        return False
    
    def __neq__(self, other):
        return True
    
    def __le__(self, other):
        return self < other
    
    def __lt__(self, other):
        if type(other)!=inf and self.sign=='-': return True
        elif other.sign=='' and self.sign=='-': return True
        else: return False

inf = _inf()

class NaN:
    def __init__(self):
        self.str = 'Nan'
        
    def __str__(self):
        return self.str
    
    def __repr__(self):
        return self.str
    
def test(func,mathfunc,inp,inp2=None):
    from time import perf_counter as clock
    exec(f"from math import {mathfunc} as lfunc")
    from random import random as r
    mfunc = locals()['lfunc']
    t0 = clock()
    for i in range(1,500):
        exec(f"y = {inp}")
        x = locals()['y']
        try:
            mfunc(x)
        except:
            print(x)
            break
    t1 = clock()-t0
    for i in range(1,500):
        exec(f"y = {inp}")
        x = locals()['y']
        try:
            func(x)
        except:
            print(x)
            break
    t2 = clock()-t0-t1
    print(f"math func := {t1}")
    print(f"my   func := {t2}")
    print(f"builtin {t2/t1} times as efficient as me")
    for i in range(1,20):
        try:
            if inp2==None: exec(f"i = {inp}")
            else: exec(f"i = {inp2}")
            print(f"Error = {1-(func(i)/mfunc(i))}")
        except: pass
        

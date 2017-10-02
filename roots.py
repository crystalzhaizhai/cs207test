
def linear_roots(a=1.0, b=0.0):
    if a == 0:
        raise ValueError("The linear coefficient is zero.  This is not a linear equation.")
    else:
        return ((-b / a))

def quad_roots(a=1.0, b=2.0, c=0.0):  
    import cmath # Can return complex numbers from square roots
    if a == 0:
        raise ValueError("The quadratic coefficient is zero.  This is not a quadratic equation.")
    else:
        sqrtdisc = cmath.sqrt(b * b - 4.0 * a * c)
        r1 = -b + sqrtdisc
        r2 = -b - sqrtdisc
        return (r1 / 2.0 / a, r2 / 2.0 / a)
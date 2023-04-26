import math
def prime_factors(n):
    i = 2
    factors = []
    upperbound = math.sqrt(n)
    while i<= upperbound:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors
def xgcd(a, b, s1 = 1, s2 = 0, t1 = 0, t2 = 1):
   """ 
   from Source: extendedeuclideanalgorithm.com/code
   we use Extended Euclidean Algorithm (recursive)
   to calculates the gcd and Bezout coefficients, 
   """
   if(b == 0):
      return abs(a), s1, t1
   q = math.floor(a/b)
   r = a - q * b
   s3 = s1 - q * s2
   t3 = t1 - q * t2
   return xgcd(b, r, s2, s3, t2, t3)
if __name__ =="__main__":
    N = 105
    e = 13
    factor = prime_factors(N)
    K = 1
    for f in factor:
        K *= f-1
    gcd, _,t = xgcd(K,e,1,0,0,1)
    if gcd ==1:
        print("inverse of", e, "mod", K, "is : ", t%K)
    else:
        print("no secret with","N=",N,",e=",e)




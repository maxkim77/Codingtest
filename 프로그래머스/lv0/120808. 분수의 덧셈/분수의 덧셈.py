def solution(numer1, denom1, numer2, denom2):
    # Function to find Greatest Common Divisor (GCD)
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # Function to find Least Common Multiple (LCM)
    def lcm(a, b):
        return abs(a*b) // gcd(a, b)
    
    # Find the LCM of the two denominators
    lcm_denom = lcm(denom1, denom2)
    
    # Convert the fractions to have the LCM as denominator and add
    result_numer = numer1 * (lcm_denom // denom1) + numer2 * (lcm_denom // denom2)
    
    # Simplify the fraction
    gcd_result = gcd(result_numer, lcm_denom)
    
    return [result_numer // gcd_result, lcm_denom // gcd_result]


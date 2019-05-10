"""
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    
    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), for N > 1.
    Given N, calculate F(N).
    
    
    
    Example 1:
    
    Input: 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
    Example 2:
    
    Input: 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
    Example 3:
    
    Input: 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
    
    
    Note:
    
    0 ≤ N ≤ 30.
"""
def fib(N):
    """
    :type N: int
    :rtype: int
        
    a,b = 0,1
    for _ in range(N):
    a, b = b, a+b
    return a
            
            
    if N < 2: return N
    return self.fib(N-1) + self.fib(N-2)
    """
    cache= {}
        
    def helper(n):
        if n in cache:
            return cache[n]
        if n < 2:
            return n

        result =helper(n-1)+helper(n-2)
        cache[n] = result
        return result
        
    return helper(N)

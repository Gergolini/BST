"""
funciton to calculate the factorial of n
factorial(n) = 1*2*3*...*n iterative
factorial(n) = n*factorial(n-1) recursive
"""
# iterative solution:
def fact_iter(n):
    res = 1
    for i in range(2, n+1):
        res = res*i
    return res

def fact_recur(n):
    # base case
    if n == 1: return 1
    return n*fact_recur(n-1)

print(fact_iter(4))
print(fact_recur(4))

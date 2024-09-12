from sys import stdin

"""

Goal: Repeatedly calculate the sum of its digits until the result is a single digit, which is denoted as g(n).
Input:
    -Each line contains a single positive integer n (up to 2,000,000,000).
        The input ends with n = 0, which should not be processed.
Output: output a single line containing the value of g(n)

"""

def f(n):
    ans = None
    if n == 0 : ans = 0
    else:
        ans = ( n % 10 ) + f(n // 10) 
    return ans

def g(n):
    ans = None
    if n < 10 : ans = n
    else:
        ans = g(f(n))
    return ans

def main():
    n = int(stdin.readline())
    while n != 0:
        print(g(n))
        n = int(stdin.readline())

if __name__ == "__main__":
    main()
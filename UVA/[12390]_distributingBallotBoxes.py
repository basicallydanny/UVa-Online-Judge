from sys import stdin

"""

Goal: Repeatedly calculate the sum of its digits until the result is a single digit, which is denoted as g(n).
Input:
    - Two integers: A, the number of cities, and B, the total number of ballot boxes.
        The next A lines contain the population of each city.
        The input ends with -1 -1, which should not be processed.
    - Conditions: Each city must receive at least one box.
Output: Minimized maximum number of people assigned to a single box for each test case.

"""
def processPopulation(A, B, populations):
    low, high = 1, max(populations)
    while high - low > 1:
        mid = (low + high) // 2
        C = 0
        for val in populations:
            C += (val + mid - 1) // mid
        if C <= B:
            high = mid
        else:
            low = mid
    return high

def main():
    for line in stdin:
        A, B = map(int, line.split())
        if A != -1 and B != -1:
            populations = []
            for i in range(A):
                n = int(stdin.readline().strip())
                populations.append(n)
            ans = processPopulation(A, B, populations)
            print(ans)
            
if __name__ == "__main__":
    main()
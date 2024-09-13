import heapq
from sys import stdin

"""

Goal: Determine the first k medications Tobby needs to take, based on their frequency.
Input:
    - T: Number of test cases (1 ≤ T ≤ 5). For each test case:
        n: Number of medications (1 ≤ n ≤ 3000).
        k: Number of medications Tobby must take (1 ≤ k ≤ 10000).
        For the next n lines, each contains:
            name: Name of the medication (length ≤ 15 characters).
            frequency: How often the medication should be taken (1 ≤ frequency ≤ 3000).
    - Conditions: The medications must be administered in a timely manner, following their priority order.
Output: The first k medications Tobby needs to take.

"""
def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        line = stdin.readline()
        t, m = map(int, line.split())
        medications = []
        for i in range(t):
            med = stdin.readline().split()
            name = med[0]
            frequency = int(med[1])
            nextTime = frequency
            medications.append((nextTime, i, name, frequency))
        heapq.heapify(medications)
        for _ in range(m):
            nextTime, order, name, frequency = heapq.heappop(medications)
            print(f"{nextTime} {name}")
            heapq.heappush(medications, (nextTime + frequency, order, name, frequency))

if __name__ == "__main__":
    main()
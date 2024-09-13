from sys import stdin

"""

Goal: Hippopotamuses must enter through a door and take a bow, either individually or by riding on top of one another, 
while adhering to height and time constraints.
Input:
    - An integer C, representing the number of test cases. For each test case:
        Four integers: N (number of hippopotamuses), H (door height), Ta (time for a single hippo to enter), Td (time for two hippos to enter together),
        A list of N integers representing the heights of the hippopotamuses.
Output: Minimum time in the format: Case X: M, where X is the case number, and M is the minimum time required.

"""
def hippoHeights(N, H, Ta, Td, heights):
    heights.sort(reverse=True)
    start, end, total = 0, N - 1, 0
    while start < end:
        if heights[start] + heights[end] < H:
            total += Td
            start += 1
            end -= 1
        else:
            total += Ta
            start += 1
    if start == end:
        total += Ta
    return total

def main():
    case = int(stdin.readline().strip())
    for c in range(1, case + 1):
        N, H, Ta, Td = map(int, stdin.readline().strip().split())
        heights = list(map(int, stdin.readline().strip().split()))
        ans = hippoHeights(N, H, Ta, Td, heights) 
        if ans > N * Ta:  
            print(f"Case {c}: {N * Ta}")
        else: 
            print(f"Case {c}: {ans}")

if __name__ == "__main__":
    main()
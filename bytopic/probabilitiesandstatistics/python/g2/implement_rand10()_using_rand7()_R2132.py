"""
Given the API rand7() that generates a uniform random integer in the range [1, 7],
write a function rand10() that generates a uniform random integer in the range [1, 10].
You can only call the API rand7(), and you shouldn't call any other API. Please do not
use a language's built-in random API.

Each test case will have one internal argument n, the number of times that your
implemented function rand10() will be called while testing. Note that this is not
an argument passed to rand10().

Constraints:
1 <= n <= 10^5

Follow up:
What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?

Sample Input/ Output:
Sample 1:
Input: n = 2
Output: [2,8]

Sample 2:
Input: n = 3
Output: [3,8,10]

Tag: R2132/2935
Tag: 470/2927
"""

import random


class RandMN:
    def rand7(self):
        """
        API that generates a uniform random integer in the range [1, 7].
        """
        return random.randint(1, 7)

    def randM(self, N, M):
        """
        Generalized version using the provided N generator to get 1..M.
        Note: This implementation assumes self.rand7() is the base 'N'.
        """
        # The range of N*N (7*7 = 49)
        # acceptable is the largest multiple of M within N*N
        range_limit = N * N
        acceptable = range_limit - (range_limit % M)

        curr = acceptable
        while curr >= acceptable:
            # We use rand7() here as our 'randN'
            curr = (self.rand7() - 1) * N + (self.rand7() - 1)

        return (curr % M) + 1

    def rand10(self):
        """
        Specific implementation for Rand10 using Rand7.
        """
        while True:
            # Generate a index between 0 and 48
            row = self.rand7()
            col = self.rand7()
            idx = (row - 1) * 7 + (col - 1)

            # If the index is in the range [0, 39], we return (idx % 10) + 1
            if idx < 40:
                return (idx % 10) + 1


def main():
    rand_mn = RandMN()

    # Example: Simulating the 'n' calls from your prompt
    n = 5
    results = [rand_mn.rand10() for _ in range(n)]

    print(f"Results for {n} calls to rand10():")
    print(results)

    # Testing the generalized version (N=7, M=10)
    print(f"\nSingle call to generalized randM(7, 10):")
    print(rand_mn.randM(7, 10))


if __name__ == '__main__':
    main()
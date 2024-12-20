class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True for _ in range(n + 1)]
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p*p, n+1, p):
                    primes[i] = False
            p += 1

        primes = [p for p in range(2, n + 1) if primes[p]]

        return len(primes)


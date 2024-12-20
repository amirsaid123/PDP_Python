class Solution:
    def is_prime(self, x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    def generate_palindromes(self, n):
        if 1 <= n <= 2:
            return 2
        if 3 <= n <= 11:
            return [3, 5, 7, 11][(n - 3) // 2]

        while True:
            str_n = str(n)
            if str_n == str_n[::-1] and self.is_prime(n):
                return n
            n += 1

            if len(str_n) > 1 and str_n == str_n[::-1] and len(str_n) % 2 == 0:
                n = 10 ** len(str_n) + 1

    def primePalindrome(self, n: int) -> int:
        return self.generate_palindromes(n)






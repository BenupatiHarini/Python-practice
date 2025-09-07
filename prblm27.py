class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(num: int) -> int:
            total = 0
            while num > 0:
                d = num % 10
                num //= 10
                total += d * d
            return total
        
        slow, fast = n, getNext(n)
        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
        return fast == 1


# 🔹 Testing locally
if __name__ == "__main__":
    sol = Solution()
    n = 19
    print(sol.isHappy(n))   # Output: True

    n = 2
    print(sol.isHappy(n))   # Output: False

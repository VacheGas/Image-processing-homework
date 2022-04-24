z = bin(8)
s = str(z)
print(s.count('1'), s)

n = 2
arr = []
for i in range(0, n + 1):
    arr.append(str(bin(i)).count('1'))
print(arr)


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num_int = int(num1)
        num2_int = int(num2)
        return str(num2_int + num_int)

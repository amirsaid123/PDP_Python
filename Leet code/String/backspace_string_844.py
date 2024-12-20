class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = []
        b = []

        for letter in s:
            if letter != '#':
                a.append(letter)
            else:
                if len(a) > 0:
                    a.pop()

        for letter in t:
            if letter != '#':
                b.append(letter)
            else:
                if len(b) > 0:
                    b.pop()

        return a == b









s = "a#b#"
t = "cd##"

a = []
b = []

for letter in s:
    if letter != '#':
        a.append(letter)
    else:
        if len(a) > 0:
            a.remove(a[-1])

for letter in t:
    if letter != '#':
        b.append(letter)
    else:
        if len(b) > 0:
            b.remove(b[-1])


print(a)
print(b)
print(a == b)



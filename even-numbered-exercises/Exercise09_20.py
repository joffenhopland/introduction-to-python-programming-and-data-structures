from Rational import *

def removeBlank(s):
    result = ""
    for ch in s:
        if ch != ' ':
            result += ch
    return result

def parseRationalNumber(s):
    s = removeBlank(s)
    if "/" in s:
        s1 = s[0 : s.find('/')]
        s2 = s[s.find('/') + 1 : ]
        # print("s1 ", s1, " s2 ", s2)
        return Rational(int(s1), int(s2))
    else:
        return Rational(int(s), 1);

def main():
    r1 = parseRationalNumber(input("Enter the first rational number: "))
    r2 = parseRationalNumber(input("Enter the second rational number: "))

    print(r1, "+", r2, "=", r1 + r2)

main()

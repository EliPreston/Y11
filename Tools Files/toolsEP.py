#  Function isEven takes an integer (a >=0) and returns True if even, and False if odd
'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def isEven(a):

    # if a % 2 == 0:
    #     return True
    # return False
    # A faster way below

    return(a % 2 == 0)


# Testing isEven
print(isEven(78))
print(isEven(99))
print(isEven(36))

for i in range(1, 200, 1):
    print(str(i)+" --> "+str(isEven(i)))


# Funciton missing_char takes a string (str) and a number (n)
# and returns a new string where the character at index n has been removed
'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def missing_char(str, n):
    return str[0:n] + str[n+1:]


# Testing missing_char
print(missing_char('hello', 2))
print(missing_char('goodbye', 6))
print(missing_char('abcdefghijklmnopqrstuvwxyz', 17))


# Binary conversion function; converts a binary input to base 10 output
'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def base2to10(str):

    n = 0
    total = 0

    for i in range(len(str) - 1, -1, -1):
        total = total + int(str[i]) * 2**n
        n = n + 1

    return total


# Testing base2To10
print(base2to10("101"))
print(base2to10("111111"))
print(base2to10("10111111"))


'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def sumDigitsA(a):

    total = 0
    a = int(a)

    while (a > 0):
        total = total + a % 10
        a = a//10
    return total


# Testing sumDigits
print(sumDigitsA(-123))
print(sumDigitsA(92343))
print(sumDigitsA(123456789))


# Sum of digits function 2, converting to str option
'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def sumDigitsB(a):

    a = str(a)  # this is casting, changes the type of a from an int to an str
    total = 0

    for i in range(0, len(a), 1):
        x = a[i]
        total = total + int(x)
    return total


print(sumDigitsB(11111111))
print(sumDigitsB(92343))
print(sumDigitsB(123456789))


# ScaleElementsA scales an array's numbers up
'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def scaleElementsA(a, b):

    for i in range(0, len(b), 1):
        b[i] = a*b[i]

    # for i in b:
    #     x = a*i
    #     # print(x)
    # return(x)


print(scaleElementsA(2, [2, 4, 6, 8]))
print(scaleElementsA(5, [1, 4, 6, 8, 3, 5]))


# ScaleElementsB scales an array's numbers up in another array
'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def scaleElementsB(a, b):

    c = []
    for i in b:
        x = a*i
        c.append(x)
    return c

    # l = []
    # for i in range(0, len(b), 1):
    #     l.append(b[i]*a)
    # return l


print(scaleElementsB(3, [1, 2, 3]))


# Adding strings together
'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def addStringsSmallLarge(a, b):

    if len(b) > len(a):
        print(b + a)
    else:
        print(a + b)


print(addStringsSmallLarge("argument", "argument1"))


'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def isPrime(n):

    r = round(n/2)
    N = int(r + 1)
    count = 0

    for i in range(2, N, 1):

        if n % i == 0:
            count += 1

    if count > 0:
        return False
    else:
        return True


for i in range(1, 100):
    number = str(isPrime(i))
    print(str(i) + " is " + number)

'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def allEven(n):

    N = int(n)
    EVEN = True

    while (N > 0) and (EVEN == True):
        if (N % 10) % 2 == 1:
            EVEN = False
        N = N // 10

    print(EVEN)


allEven(26626464)


'''
Description;
Parameters;
Return;
Pre-conditions;
Post-conditions;

'''


def fibonacciGen(n):

    sequence = [1, 2]

    # while last value in list is less than a
    while sequence[-1] < n:

        nxt = sequence[-1] + sequence[-2]
        sequence.append(nxt)

    del sequence[-1]
    return sequence


print(fibonacciGen(10000))

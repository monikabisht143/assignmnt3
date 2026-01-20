def fact(num):
        factorial = 1
        while num > 1:
            factorial *= num
            num -= 1
        return factorial
n=int(input("enter the number:"))
print(F" factorial of {n} is {fact(n)}")

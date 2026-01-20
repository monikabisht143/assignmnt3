def fact_rec(num):
    if num == 1:
        return 1
    else:
        factorial = num * fact_rec(num)
        return factorial
print(fact_rec(4))

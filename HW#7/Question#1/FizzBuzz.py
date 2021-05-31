def Fizz_Buzz():
    fizzbuzz = []
    for i in range(101):
        if i == 0:
            continue
        elif i % 3 == 0 and i % 5 == 0:
            fizzbuzz.append(i)
            continue
        elif i % 3 == 0:
            fizzbuzz.append("fizz")
            continue
        fizzbuzz.append(i)
    return fizzbuzz

print(Fizz_Buzz())

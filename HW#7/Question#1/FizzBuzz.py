def Fizz_Buzz():
    fizzbuzz = []
    for i in range(101):
        if i == 0:
            continue
        elif i % 3 == 0 and i % 5 == 0:
            fizzbuzz.append("fizzbuzz")
            continue
        elif i % 3 == 0:
            fizzbuzz.append("fizz")
            continue
        elif i % 5 == 0:
            fizzbuzz.append("buzz")
            continue
        fizzbuzz.append(i)
    return fizzbuzz

print(Fizz_Buzz())

def fibonacci():
    a = 0
    b = 1

    while a <= 50:
        print(a)
        a, b = b, a + b

fibonacci()
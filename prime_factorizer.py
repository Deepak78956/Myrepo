def prime_factors(num):
    if num == 1:
        print("1")
    elif num == 2:
        print("1", "2")
    elif num == 3:
        print("1", "2", "3")
    else:
        print(1)
        print(2)
        print(3)
        for n in range(5, num+1, 2):
            div = 2
            while div <= n:
                if n == div:
                    print(n)
                    break
                elif n % div == 0:
                    break
                else:
                    div += 1

prime_factors(3)

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"Your number {n} is a prime")
    else:
        print(f"Your number {n} is NOT a prime")


n = int(input("Check your number: "))
prime_checker(number=n)
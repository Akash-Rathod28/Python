a = int(input("Enter a number greater than 1: "))

if a <= 1:
    print("Please enter a number greater than 1.")
else:
    is_prime = True
    
    # Check for factors from 2 up to the number itself
    for i in range(2, a):
        if a % i == 0:
            is_prime = False
            break  # We found a factor, so it's definitely not prime

    if is_prime:
        print(f"{a} is a Prime Number")
    else:
        print(f"{a} is NOT a Prime Number")

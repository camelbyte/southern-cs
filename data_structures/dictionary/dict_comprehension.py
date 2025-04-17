import random 
import numpy as np 


names = ["Alice", "Bob", "Charlie", "David", "Eve"]

rd = {f"key_{i}": random.randint(1, 100) for i in range(5)}
print(rd)


random_values = [random.random() for _ in range(10)]
print("\n", random_values)

names_ages_dict = {k: v for k, v in zip(names, random_values)}
print(names_ages_dict)


prices = {"avocados": 6.5, "eggs": 13.8, "milk": 8.5}


# Apply 75% discount to every product in the dictionary

discounted = {item: price *0.75 for item, price in prices.items()}

print(discounted)



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0:
            return False
    return True




def prime_list(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]



print(prime_list(50))  
print(is_prime(11))  
print(is_prime(12)) 



def first_primes(n):
    primes = []
    num = 2  # Start from the first prime number
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
        print(primes)
    return primes



first_primes(64)

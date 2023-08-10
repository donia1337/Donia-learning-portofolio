# Create a prime number generator that yields all prime numbers in a loop. (consider having an is_prime function already defined).


def get_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num 
        num += 1
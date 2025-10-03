def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, n):
        if n % i == 0:
            return False  # Found a factor, so n is not prime
    return True  # No factors found, n is prime

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#Efficient approach root n logic
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    # Initialize a boolean list where index represents the number
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False  # 0 and 1 are not prime

    for p in range(2, int(limit ** 0.5) + 1):
        if prime[p]:
            # Mark multiples of p as non-prime
            for i in range(p * p, limit + 1, p):
                prime[i] = False

    # Collect all prime numbers
    primes = [num for num, is_prime in enumerate(prime) if is_prime]
    return primes

# Example usage
n = int(input("Find primes up to: "))
print(f"Primes up to {n}: {sieve_of_eratosthenes(n)}")
# ▶️ Time Complexity of Sieve of Eratosthenes:

# Time Complexity: O(n log log n)

# Space Complexity: O(n) (to store the boolean array)
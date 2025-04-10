def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nth_prime(n):
    if n < 1:
        raise ValueError("n must be a positive integer.")
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate

# Example usage:
# print(find_nth_prime(10))  # Output: 29




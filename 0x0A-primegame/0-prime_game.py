#!/usr/bin/python3
"""
The Prime Game
"""


def sieve_of_eratosthenes(max_num):
    """Returns a list of booleans representing whether numbers are prime up to
    max_num
    """
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(max_num**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, max_num + 1, p):
                is_prime[multiple] = False
    return is_prime


def count_primes_up_to_n(is_prime, n):
    """Count primes up to n and return the number of primes
    """
    count = 0
    remaining = list(range(1, n + 1))

    for i in range(2, n + 1):
        if is_prime[i]:
            count += 1
            # Remove multiples of the prime i
            remaining = [x for x in remaining if x % i != 0]
    return count


def isWinner(x, nums):
    """Return the name of the player that won the most rounds
    """
    max_n = max(nums)
    # Precompute prime information for all numbers up to max_n
    is_prime = sieve_of_eratosthenes(max_n)

    players = {'Maria': 0, 'Ben': 0}

    for num in nums:
        prime_count = count_primes_up_to_n(is_prime, num)
        if prime_count % 2 == 1:
            players['Maria'] += 1
        else:
            players['Ben'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None

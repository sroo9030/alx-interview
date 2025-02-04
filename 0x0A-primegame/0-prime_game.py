#!/usr/bin/python3


def isWinner(x, nums):
    """Determines the winner of the game
    """
    if not nums or x < 1:
        return None
    
    def sieve(n):
        """Returns a list where primes[i] is True if i is a prime number
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes
    
    max_n = max(nums)  # Find the maximum n in nums
    # Store the count of primes up to index i
    prime_counts = [0] * (max_n + 1)  
    primes = sieve(max_n)
    
    # Precompute prime counts
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1  # Maria wins if the count of primes is odd
        else:
            ben_wins += 1  # Ben wins if the count of primes is even
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

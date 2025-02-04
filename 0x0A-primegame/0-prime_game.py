#!/usr/bin/python3
"""
This module determines the winner of a game played between Maria and Ben

"""


def isWinner(x, nums):
    """
    Determines the overall winner after x rounds of the game.

    Parameters:
    x (int): Number of rounds.
    nums (list of int): List of values for n in each round.

    Returns:
    str: Name of the player who won the most rounds ("Maria" or "Ben").
         Returns None if there is a tie.
    """
    if not nums or x < 1:
        return None

    def sieve(n):
        """
        Generates a boolean list where primes[i]
        is True if i is a prime number.

        Parameters:
        n (int): The maximum number to check for primes.

        Returns:
        list: A boolean list indicating prime status for numbers
        from 0 to n.
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
            # Maria wins if the count of primes is odd
            maria_wins += 1
        else:
            # Ben wins if the count of primes is even
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None

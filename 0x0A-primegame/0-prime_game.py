#!/usr/bin/python3

"""contains a solution to the problem where two players, Maria and Ben,
take turns choosing a prime number from a set of consecutive integers
starting from 1 to `n`
"""


def isWinner(x, nums):
    """A function that finds solution to the problem where two players,
    Maria and Ben, take turns choosing a prime number from a set of
    consecutive integers starting from 1 to `n`
    """
    def sieve_of_eratosthenes(n):
        """Helper function to find primes up to n using Sieve of Eratosthenes
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return [i for i in range(2, n + 1) if primes[i]]

    def simulate_game(n):
        """Function to simulate one round of the game
        """
        primes = sieve_of_eratosthenes(n)
        # True means the number is still in the game
        numbers = [True] * (n + 1)
        turn = 0  # 0 means Maria's turn, 1 means Ben's turn

        while primes:
            for prime in primes:
                if numbers[prime]:
                    # The current player removes prime and its multiples
                    for multiple in range(prime, n + 1, prime):
                        numbers[multiple] = False
                    primes = sieve_of_eratosthenes(n)
                    break
            else:
                return "Ben" if turn == 0 else "Maria"

            turn = 1 - turn

        return "Ben" if turn == 0 else "Maria"

    maria_wins = 0
    ben_wins = 0

    # Simulate each round and count wins
    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

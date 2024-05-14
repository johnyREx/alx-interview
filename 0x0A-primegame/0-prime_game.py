#!/usr/bin/python3

def isWinner(x, nums):
    """Determines the winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of n for each round.

    Returns:
        str: name of the player that won the most rounds or None.
    """

    def isPrime(num):
        """Check if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def getPrimes(n):
        """Generate a list of prime numbers up to n.

        Args:
            n (int): The upper limit.

        Returns:
            list: List of prime numbers.
        """
        primes = []
        for i in range(2, n + 1):
            if isPrime(i):
                primes.append(i)
        return primes

    def playGame(n):
        """Simulate the game for a given n.

        Args:
            n (int): The upper limit.

        Returns:
            str: Name of the winner ('Maria', 'Ben', or None).
        """
        primes = getPrimes(n)
        maria_primes = 0
        ben_primes = 0

        for i in range(len(primes)):
            if i % 2 == 0:
                maria_primes += 1
            else:
                ben_primes += 1

        if maria_primes > ben_primes:
            return "Maria"
        elif ben_primes > maria_primes:
            return "Ben"
        else:
            return None

    winners = [playGame(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

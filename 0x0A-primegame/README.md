# README for `0x0A-primegame` in the `alx-interview` Repository

## Project Overview

The `0x0A-primegame` directory contains a solution to the problem where two players, Maria and Ben, take turns choosing a prime number from a set of consecutive integers starting from 1 to `n`. Each player removes the chosen prime number and all its multiples from the set. The game ends when no more prime numbers are left for a player to pick, and the player who cannot make a move loses. The task is to determine the winner for each round of the game and, ultimately, identify the player who wins the most rounds.

## Problem Description

In each round, Maria and Ben take turns selecting a prime number from a set starting from 1 to `n`. After a prime is chosen, it and all its multiples are removed from the set. Maria always goes first, and both players play optimally. The player who cannot make a move loses the round.

The function `isWinner(x, nums)` is implemented to simulate `x` rounds of the game where each round corresponds to a different value of `n` (from the array `nums`). The goal is to determine who won the most rounds. If both players win an equal number of rounds, the function returns `None`.

### Input

- `x`: An integer representing the number of rounds of the game.
- `nums`: An array of integers, where each integer represents the value of `n` for a round.

### Output

The function returns the name of the player who won the most rounds, or `None` if there is a tie in the number of rounds won by Maria and Ben.

## Requirements

- No additional libraries are required to run the solution.
- The solution must be implemented without importing external packages (e.g., `math`, `numpy`).
- The input size `n` will not exceed 10,000, and `x` will also not exceed 10,000, ensuring that the approach needs to be efficient for large inputs.

## Algorithm Overview

The solution follows these steps:

1. **Prime Calculation**: For each round, we use the Sieve of Eratosthenes algorithm to calculate all the prime numbers up to `n`. This allows us to know the valid moves for each player.
  
2. **Game Simulation**: For each round, we simulate the game by removing prime numbers and their multiples from the set of numbers. Players alternate turns, and if a player cannot make a move, they lose the round.

3. **Winner Determination**: After simulating all rounds, we count how many rounds Maria and Ben each won and return the player who won the most rounds.

## Author

- Martin Olutade
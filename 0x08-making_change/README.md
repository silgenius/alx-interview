# 0x08. Making Change

This project focuses on solving the "making change" problem, where you are given a pile of coins of different values and need to determine the fewest number of coins required to make a given amount.

## Table of Contents

- [Task Description](#task-description)
- [Prototype](#prototype)
- [Requirements](#requirements)
- [Usage](#usage)
- [Test Cases](#test-cases)
- [Contributors](#contributors)

---

## Task Description

You are given a pile of coins of different values. Your goal is to determine the fewest number of coins required to meet a given total. If it is not possible to meet the total using the available coin denominations, the program should return `-1`.

The problem will be solved by implementing the function `makeChange(coins, total)`.

---

## Prototype

```python
def makeChange(coins, total)
```

### Return Value
-  If `total` is 0 or less, return `0`.
- If the `total` cannot be met by any combination of the coins available, return `-1`.
- Otherwise, return the fewest number of coins needed to make the total.

## Usage

```python
makeChange = __import__('0-making_change').makeChange

# Test cases
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

## Author
- [Martin Olutade](https://github.com/silgenius)
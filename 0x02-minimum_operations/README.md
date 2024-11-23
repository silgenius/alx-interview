# 0x02. Minimum Operations

This project focuses on solving the problem of determining the minimum number of operations required to reach a given number of `n` starting from `1` using two types of operations: 

1. **Copy All**: Copies the current number to the clipboard.
2. **Paste**: Pastes the number from the clipboard onto the current number.

The task is to calculate the minimum number of operations needed to reach exactly `n` using the two operations.

## File: `0-minoperations.py`

This Python script contains a solution to the problem of finding the minimum number of operations required to reach a target number `n` from `1` using the least number of operations. The solution involves checking for divisors of `n` and performing the required copy and paste actions accordingly.

### Function: `minOperations(n)`

This function calculates the minimum number of operations to reach the target number `n` from `1`. The function works as follows:

- If `n <= 1`, the function returns `0` because no operations are needed.
- Otherwise, the function computes the minimum number of operations by checking the factors of `n`.
- It continues to reduce the number `n` by dividing it by its factors until `n` becomes `1`.

#### Parameters:
- `n` (int): The target number to reach from `1`.

#### Returns:
- int: The minimum number of operations required to reach `n`.

### Example

```python
minOperations(9)
```

For n = 9, the function would return 6, as it requires 6 operations to reach 9 starting from 1.

### Time Complexity
The time complexity of the algorithm is approximately `O(sqrt(n))`, as we check factors of n up to the square root of n.

## Requirements
- Python 3.x

## How to run
- Clone this repository:

```bash
git clone https://github.com/yourusername/0x02-minimum_operations.git
```

- Navigate to the project directory:

```bash
cd 0x02-minimum_operations
```

- Run the script:

```bash
python3 0-minoperations.py
```
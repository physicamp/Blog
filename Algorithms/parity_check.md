# Parity Calculation in Python

## Overview
This document explains a Python function that calculates the **parity** of an integer.

## What is Parity?
- The **parity** of a binary number determines whether the count of `1`s in its binary representation is **even (0)** or **odd (1)**.
- Used in error detection and low-level computing operations.

## Python Implementation
```python
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1  # Right shift x to process the next bit
    return result
```

## Explanation
1. **Initialize `result = 0`**.
2. **Loop while `x` is non-zero**:
   - Extract the least significant bit using `x & 1`.
   - XOR (`^=`) it with `result`.
   - Right shift `x` (`x >>= 1`) to process the next bit.
3. **Return `result`**, which is:
   - `1` if the number of `1`s in `x` is odd.
   - `0` if the number of `1`s in `x` is even.

## Example Usage
```python
print(parity(7))  # 7 in binary is 111 (3 ones) -> returns 1
print(parity(8))  # 8 in binary is 1000 (1 one) -> returns 1
print(parity(10)) # 10 in binary is 1010 (2 ones) -> returns 0
```

## Edge Cases
- `parity(0)`: Returns `0` (binary `0` has zero `1`s).
- `parity(1)`: Returns `1` (binary `1` has one `1`).
- Large numbers: Works efficiently but can be optimized further.

## Notes
- The function runs in **O(n)** time, where `n` is the number of bits in `x`.
- Faster methods exist, such as **bitwise tricks** and **lookup tables**.

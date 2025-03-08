# Bit Swapping in Python

## Overview
This document explains how to swap two bits in a 64-bit integer efficiently using bitwise operations.

## Key Concepts
1. **Bits and Indexing:**
   - A 64-bit integer consists of 64 bits.
   - The rightmost bit (LSB - Least Significant Bit) is at index 0.
   - The leftmost bit (MSB - Most Significant Bit) is at index 63.

2. **Bit Manipulation Tricks:**
   - `x & (x - 1)`: Clears the lowest set bit (1).
   - `x & ~(x - 1)`: Extracts the lowest set bit.

3. **Swapping Bits Efficiently:**
   - Instead of using extra variables to store bits, we use **bitwise XOR** (`^`).
   - First, we check if the two bits are different.
   - If they are different, flipping both results in a swap.

## Python Code
```python
def swap_bits(x, i, j):
    # Extract the i-th and j-th bits and check if they are different
    if (x >> i) & 1 != (x >> j) & 1:
        # Create a bit mask to flip the bits at indices i and j
        bit_mask = (1 << i) | (1 << j)
        # Use XOR (^) to flip the selected bits
        x ^= bit_mask
    return x
```

## How It Works
- **Extracting Bits:**  
  `(x >> i) & 1` gets the bit at index `i`, and `(x >> j) & 1` gets the bit at index `j`.
- **Checking Difference:**  
  If the two bits are the same, no swap is needed.
- **Bit Masking & XOR:**  
  - `1 << i` and `1 << j` create a mask to select the bits.
  - `x ^= bit_mask` flips the bits, swapping them.

## Example
```python
x = 73  # Binary: 01001001
i, j = 1, 6
result = swap_bits(x, i, j)
print(bin(result))  # Output: 0b1011 (Decimal: 11)
```

This swaps bit `1` and bit `6`, transforming `73` (`0b1001001`) into `11` (`0b1011`).


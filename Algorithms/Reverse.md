# **Reversing Bits of a 64-bit Unsigned Integer**

## **Problem Statement**
Given a 64-bit unsigned integer, return another 64-bit unsigned integer where the bits are in reverse order.

### **Example**
Input:  `1110000000000001`  
Output: `1000000000000111`

## **Brute-force Approach**
- Swap each bit with its corresponding opposite bit.
- Iterate through the 32 least significant bits and swap them with the 32 most significant bits.

## **Optimized Approach (Using Lookup Table)**
1. **Break the 64-bit number** into four 16-bit segments:  
   - \( y_3, y_2, y_1, y_0 \) (where \( y_3 \) holds the most significant bits).
2. **Precompute bit-reversal of 16-bit numbers** using a lookup table.
3. **Reconstruct the reversed number** by retrieving reversed segments from the table:
   - Reversed \( y_0 \) forms the most significant bits of the result.
   - Reversed \( y_1 \) comes next.
   - Reversed \( y_2 \) follows.
   - Reversed \( y_3 \) forms the least significant bits.

## **Example with 8-bit Numbers**
- Let’s assume we have a lookup table for 2-bit numbers:
  ```
  rev = [(00), (10), (01), (11)]
  ```
- Given the input `10010011`:
  - Reverse each 2-bit segment: `rev(11), rev(00), rev(01), rev(10)`
  - Result: `11001001`

## **Why Use a Lookup Table?**
- **Efficiency:** Avoids repetitive bit manipulations.
- **Speed:** Precomputed values allow quick access.
- **Scalability:** Works well when reversing bits multiple times.

---

## **Explanation for a Junior Programmer**
Think of reversing bits like flipping a mirror image of a number. If you write down a binary number and then write it in reverse, that’s the output you want.

### **Basic Idea (Brute Force)**
Imagine we have `64` switches (bits), and we want to swap the first with the last, the second with the second last, and so on. We do this by using bitwise operations, but this can be slow.

### **Optimized Way: Lookup Table**
Instead of manually flipping every bit:
1. We **divide** the number into smaller parts (like cutting a long sentence into words).
2. We **precompute** the reverse of those smaller parts.
3. We **use the precomputed values** to quickly assemble the final reversed number.

### **Example in Simpler Terms**
Think of reversing a word like `"hello"`:
- Brute-force: Swap `h` with `o`, `e` with `l` (manual work).
- Optimized: Use a dictionary where we store `"he"` → `"eh"`, `"lo"` → `"ol"` and quickly rebuild `"olleh"`.

Using a lookup table is like having a dictionary that tells you the reverse of small parts, making the process faster.


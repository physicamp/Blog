# Differences Between List and Array in Python

## 1. Overview
In Python, both **lists** and **arrays** can be used to store collections of items. However, they differ in terms of data types, performance, and use cases.

## 2. Key Differences

| Feature          | List (`list`)        | Array (`array.array`) |
|-----------------|---------------------|-----------------------|
| Data Type       | Can store mixed types | Stores elements of a single type |
| Memory Usage    | Higher (stores references to objects) | Lower (stores raw values) |
| Performance     | Slower for numerical operations | Faster for numerical operations |
| Flexibility     | More flexible (supports heterogeneous data) | Less flexible (homogeneous data only) |
| Import Required | No | Yes (`from array import array`) |
| Suitable For    | General-purpose collections | Numerical computations with fixed types |

## 3. Example Usage

### **List Example**
```python
my_list = [1, "hello", 3.14]  # Mixed types allowed
print(my_list[1])  # Output: hello

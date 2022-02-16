# Binry Spaghetti Sort and Binary Spaghetti Index
Repository of the publication:

# Description
Sorting items is a fundamental problem in computer science and algorithms design. Sorting algorithms can be divided in two categories, comparison based and non-comparison based, depending on the way they perform the sorting. Non-comparison based algorithms work on the nature of numbers, for instance, the fact that they are represented as decimal numbers. No algorithm so far, to the best of my knowledge, exploits the binary representation of numbers and, at the same time, bitwise operations to sort items. In this work, I present a stable non-comparison based algorithm (inspired by Spaghetti Sort) which sorts lists of $\mathbb{N}^+$ numbers using binary numbers to create an index which can also stored on distributed systems. Furthermore, because of its nature, I show how this algorithm can be assembled into an electrical circuit to sort numbers in parallel.

# Example
<img src="/images/example.png" alt="drawing" width="600"/>

# How to use it
```
from binaryspaghettisort import *
BinarySpaghettiSort([3,42,4234,23])
```

# Binry Spaghetti Sort and Binary Spaghetti Index
Repository of the publication:

Author: Alberto Calderone

Contact: sinnefa@gmail.com

# Description
Sorting items is a fundamental problem in computer science and algorithms design. Sorting algorithms can be divided in two categories, comparison based and non-comparison based, depending on the way they perform the sorting. Non-comparison based algorithms work on the nature of numbers, for instance, the fact that they are represented as decimal numbers. No algorithm so far, to the best of my knowledge, exploits the binary representation of numbers and, at the same time, bitwise operations to sort items. In this work, I present a stable non-comparison based algorithm (inspired by Spaghetti Sort) which sorts lists of N+ numbers using binary numbers to create an index which can also be stored on distributed systems. Furthermore, because of its nature, I show how this algorithm can be assembled into an electrical circuit to sort numbers in parallel.

# Example
<img src="/images/example.png" alt="drawing" width="600"/>

# How to use it
```
from binaryspaghettisort import *
BinarySpaghettiSort([3,42,4234,23])
```

# Algorithm

```
def BinarySpaghettiSort(values, reverse=False):
  length = len(values)
  sorted = [0]*length
  maximum = max(values)
  minimum = min(values)
  binary_spaghetti_heads_index=[0]*(maximum-minimum+1)
  #binary_spaghetti_heads_index=SparseList() # De-Comment to use sparse data structure
  
  for i,n in enumerate(values):
    #if binary_spaghetti_heads_index[(n-minimum)] is None: # De-Comment to use sparse data structure
    #  binary_spaghetti_heads_index[(n-minimum)] = 0 # De-Comment to use sparse data structure
    binary_spaghetti_heads_index[(n-minimum)] += 1<<(length-1-i)
    
  index = 0
  start = 0
  stop = len(binary_spaghetti_heads_index)
  pace = 1
  if reverse:
    start = len(binary_spaghetti_heads_index)-1
    stop = -1
    pace = -1
  for i in range(start,stop,pace):
    xor = binary_spaghetti_heads_index[i]
    #if xor is None: # De-Comment to use sparse data structure
    #  continue # De-Comment to use sparse data structure
    while xor > 0:
      k = int(math.log2(xor))
      sorted[index] = values[length-1-k]
      xor = xor ^ (1 << k)
      index += 1
  return sorted
```

## (Bonus) Electrical Circuit in Logisim
<img src="/images/Main_Circuit_2.png" alt="drawing" width="600"/>
<img src="/images/Loop_Circuit_1.png" alt="drawing" width="600"/>

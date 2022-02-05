# Spaghetti Sort Using Bitwise Operations
A freaky implementation of the Spaghetti Sort using bits, binary numbers and as many bitwise operations as possible

Spaghetti sort: https://en.wikipedia.org/wiki/Spaghetti_sort

My implementation using binary operations. 

Because of its nature it sorts N+ numbers {1, 2, 3, ...}

# Key points:
1. Mimic the spaghetti sort main steps
- Spaghetti creation
- Spaghetti alignments according to length
- Hand moving down to collect spaghetti by length

2. Don't use imports
3. Use as many bitwise operations as possible
Note: Instead our hand we will be using a mask of bits

# Wordy explanation:
Take each number in the list and create rods of 1's of the same lengths as the numbers. With a mask of bits slide from the top down using XOR's to get rid of selected spaghetti.

# 05 February 2022
# Author: sinnefa@gmail.com

def bitwiseRoundedLog2(x):
  # Calculates rounded log2 to get the leftmost bit
  k = -1
  while x > 0:
    x = x >> 1
    k += 1
  return k

def bitwiseBooleanToInteger(bitlist):
  # Turns a list of bit into an integer
  v = 0
  for bit in bitlist:
    v = (v << 1) | bit
  return v

def freakyBinarySpaghettiSort(values, verbose = False, verbonetime=False):

  # Spaghetti sort implementation using binary operations. Because of its
  # nature it sorts N+ numbers {1, 2, 3, ...}
  #
  # Key points:
  # 1) Mimic the spaghetti sort main steps
  #   1 - Spaghetti creation
  #   2 - Spaghetti alignments according to length
  #   3 - Hand moving down to collect spaghetti by length
  # 2) Don't use imports
  # 3) Use as many bitwise operations as possible
  # Note: Instead our hand we will be using a mask of bits

  length, maximum, minimum, mask = len(values), max(values), min(values), 0
  range_limit = maximum-minimum+1 # we virtually create spaghetti
                                  # with a length relative to the list
                                  # to save some bits as this algo 
                                  # can wreak havoc on your machine :P
  sorted, spaghetti = [0]*length, [0]*length
  
  # Using shifts we create spaghetti rods consisting of 1's
  # but remember we saved memory with the max/min trick ^_^
  spaghetti = [(1<<(n-minimum+1))-1<<(maximum-n) for n in values]

  index = 0
  for x in range(0, range_limit):
    xor = bitwiseBooleanToInteger([(s >> x) & 1 for s in spaghetti])
    xor = xor ^ mask  # processing only bits left moving the mask from
                      # left to right
    mask = xor | mask # Updating the mask for when we move leftwards
    while xor > 0: # Filtering bits set to one to get the position of the
                   # sorted value in values
      k = bitwiseRoundedLog2(xor)
      sorted[index] = values[-k-1]
      bin_pos = 1 << k # As we took a spaghetto we can mask the bit
      xor = xor ^ bin_pos # Processing only unmasked spaghetti
      index += 1
  return sorted

print(freakyBinarySpaghettiSort([534, 36, 36, 45, 634, 346, 34]))

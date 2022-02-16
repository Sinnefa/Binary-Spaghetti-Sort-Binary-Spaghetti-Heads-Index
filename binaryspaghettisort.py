import random
import math
import time

class SparseList(list):
  def __setitem__(self, index, value):
    missing = index - len(self) + 1
    if missing > 0:
      self.extend([None] * missing)
    list.__setitem__(self, index, value)
  def __getitem__(self, index):
    try: return list.__getitem__(self, index)
    except IndexError: return None

def BinarySpaghettiSort(values):
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
  for xor in binary_spaghetti_heads_index:
    #if xor is None: # De-Comment to use sparse data structure
    #  continue # De-Comment to use sparse data structure
    while xor > 0:
      k = int(math.log2(xor))
      sorted[index] = values[length-1-k]
      xor = xor ^ (1 << k)
      index += 1
  return sorted

if __name__ == "__main__":
	values = [random.randint(1, 5000) for _ in range(5000)]
	start_time = time.time()
	vett = BinarySpaghettiSort(values)
	print("Binary Spaghetti Sort 5000 random N+ numbers took: ",time.time() - start_time, "seconds")
	start_time = time.time()
	sorted(values)
	print("Python Sort 5000 random N+ numbers took: ",time.time() - start_time, "seconds")
	print("Is Binary Spaghetti Sort equal to Python sort?: ", sorted(values)==vett)

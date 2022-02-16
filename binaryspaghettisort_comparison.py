import math
import random
import time
import pandas as pd
import tracemalloc
import gc
import sys
import os
import matplotlib.pyplot as plt
from binaryspaghettisort import * 
import searchsort as ss

########## Utility Functions

def average(lst):
  return sum(lst) / len(lst)

def sd(xs):
  mean = sum(xs) / len(xs)
  var  = sum(pow(x-mean,2) for x in xs) / len(xs)
  std  = math.sqrt(var)
  return std

######### COMPARISON RANDOM

results = pd.DataFrame(columns=[
                                'Length',
                                "PS",
                                "CS",
                                "BS",
                                "RS",
                                "SS",
                                "Mean_Time_PS",
                                "Mean_Time_CS",
                                "Mean_Time_BS",
                                "Mean_Time_RS",
                                "Mean_Time_SS",
                                "SD_Time_PS",
                                "SD_Time_CS",
                                "SD_Time_BS",
                                "SD_Time_RS",
                                "SD_Time_SS",
                                "Mean_Memory_PS",
                                "Mean_Memory_CS",
                                "Mean_Memory_BS",
                                "Mean_Memory_RS",
                                "Mean_Memory_SS",
                                "SD_Memory_PS",
                                "SD_Memory_CS",
                                "SD_Memory_BS",
                                "SD_Memory_RS",
                                "SD_Memory_SS"])

names = ["PS","CS","BS","RS","SS"]

for length in range(5,500,5):
        print(length)
        try:
          run = {}
          tbsa, tisa, thsa, tmsa, tssa = [], [], [], [], []
          mbsa, misa, mhsa, mmsa, mssa = [], [], [], [], []
          for i in range(10):
              values = [random.randint(1, length) for _ in range(length)]
              tracemalloc.start()
              mbs = tracemalloc.get_traced_memory()[1]
              start_time = time.time()
              ss.PigeonholeSort(values.copy())
              tbs = time.time() - start_time
              mbs = tracemalloc.get_traced_memory()[1] - mbs
              tracemalloc.stop()
              gc.collect()

              tracemalloc.start()
              mis = tracemalloc.get_traced_memory()[1]
              start_time = time.time()
              ss.CountingSort(values.copy())
              tis = time.time() - start_time
              mis = tracemalloc.get_traced_memory()[1] - mis
              tracemalloc.stop()
              gc.collect()

              tracemalloc.start()
              mhs = tracemalloc.get_traced_memory()[1]
              start_time = time.time()
              ss.BucketSort(values.copy())
              ths = time.time() - start_time
              mhs = tracemalloc.get_traced_memory()[1] - mhs
              tracemalloc.stop()
              gc.collect()

              tracemalloc.start()
              mms = tracemalloc.get_traced_memory()[1]
              start_time = time.time()
              ss.RadixSort(values.copy(), 2)
              tms = time.time() - start_time
              mms = tracemalloc.get_traced_memory()[1] - mms
              tracemalloc.stop()
              gc.collect()

              tracemalloc.start()
              mss = tracemalloc.get_traced_memory()[1]
              start_time = time.time()
              BinarySpaghettiSort(values.copy())
              tss = time.time() - start_time
              mss = tracemalloc.get_traced_memory()[1] - mss
              tracemalloc.stop()
              gc.collect()
              if BinarySpaghettiSort(values.copy())!=list(ss.PigeonholeSort(values.copy())):
                print("error")
                print(vett)
                print(list(ss.PigeonholeSort(values)))
                break

              tbsa.append(tbs)
              tisa.append(tis)
              thsa.append(ths)
              tmsa.append(tms)
              tssa.append(tss)
              mbsa.append(mbs / 1024)
              misa.append(mis / 1024)
              mhsa.append(mhs / 1024)
              mmsa.append(mms / 1024)
              mssa.append(mss / 1024)

          run["PS"] = average(tbsa)
          run["CS"] = average(tisa)
          run["BS"] = average(thsa)
          run["RS"] = average(tmsa)
          run["SS"] = average(tssa)

          ranking = list(dict(sorted(run.items(), key=lambda item: item[1])).keys())
          row = {}
          for name in names:
            row[name] = ranking.index(name)+1
          row["Length"] = length
          row["Mean_Time_PS"] = average(tbsa)
          row["Mean_Time_CS"] = average(tisa)
          row["Mean_Time_BS"] = average(thsa)
          row["Mean_Time_RS"] = average(tmsa)
          row["Mean_Time_SS"] = average(tssa)
          row["SD_Time_PS"] = sd(tbsa)
          row["SD_Time_CS"] = sd(tisa)
          row["SD_Time_BS"] = sd(thsa)
          row["SD_Time_RS"] = sd(tmsa)
          row["SD_Time_SS"] = sd(tssa)
          row["Mean_Memory_PS"] = average(mbsa)
          row["Mean_Memory_CS"] = average(misa)
          row["Mean_Memory_BS"] = average(mhsa)
          row["Mean_Memory_RS"] = average(mmsa)
          row["Mean_Memory_SS"] = average(mssa)
          row["SD_Memory_PS"] = sd(mbsa)
          row["SD_Memory_CS"] = sd(misa)
          row["SD_Memory_BS"] = sd(mhsa)
          row["SD_Memory_RS"] = sd(mmsa)
          row["SD_Memory_SS"] = sd(mssa)
          results = results.append(row,ignore_index=True)
        except Exception as e:
          exc_type, exc_obj, exc_tb = sys.exc_info()
          fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
          print(exc_type, fname, exc_tb.tb_lineno)
          print(e)

results
results.to_csv("results.csv")

my_dpi = 150
fig, ax = plt.subplots(nrows=2,ncols=1,figsize=(2048/my_dpi, 1024/my_dpi), dpi=my_dpi)
plt.style.use('seaborn-paper')
p = results.plot(ax=ax[0], x='Length',y='Mean_Time_PS',color="red",label="Pigeonhole Sort", logy=True)
#p.fill_between(results.Length, results.Mean_Time_PS-results.SD_Time_PS, results.Mean_Time_PS+results.SD_Time_PS, alpha=0.25, color="red")
p = results.plot(ax=ax[0], x='Length',y='Mean_Time_CS',color="blue",label="Count Sort", logy=True)
#p.fill_between(results.Length, results.Mean_Time_CS-results.SD_Time_CS, results.Mean_Time_CS+results.SD_Time_CS, alpha=0.25, color="blue")
p = results.plot(ax=ax[0], x='Length',y='Mean_Time_BS',color="orange",label="Bucket Sort", logy=True)
#p.fill_between(results.Length, results.Mean_Time_BS-results.SD_Time_BS, results.Mean_Time_BS+results.SD_Time_BS, alpha=0.25, color="orange")
p = results.plot(ax=ax[0], x='Length',y='Mean_Time_RS',color="darkmagenta",label="Radix Sort", logy=True)
#p.fill_between(results.Length, results.Mean_Time_RS-results.SD_Time_RS, results.Mean_Time_RS+results.SD_Time_RS, alpha=0.25, color="darkmagenta")
p = results.plot(ax=ax[0], x='Length',y='Mean_Time_SS',color="green",label="Binary Spaghetti Sort", ylabel="Time in seconds", logy=True)
#p.fill_between(results.Length, results.Mean_Time_SS-results.SD_Time_SS, results.Mean_Time_SS+results.SD_Time_SS, alpha=0.25, color="green")

p = results.plot(ax=ax[1], x='Length',y='Mean_Memory_PS',color="red",label="Pigeonhole Sort", logy=True)
#p.fill_between(results.Length, results.Mean_Memory_PS-results.SD_Memory_PS, results.Mean_Memory_PS+results.SD_Memory_PS, alpha=0.25, color="red")
p = results.plot(ax=ax[1], x='Length',y='Mean_Memory_CS',color="blue",label="Count Sort", logy=True)
#p.fill_between(results.Length, results.Mean_Memory_CS-results.SD_Memory_CS, results.Mean_Memory_CS+results.SD_Memory_CS, alpha=0.25, color="blue")
p = results.plot(ax=ax[1], x='Length',y='Mean_Memory_BS',color="orange",label="Bucket Sort", logy=True)
#p.fill_between(results.Length, results.Mean_Memory_BS-results.SD_Memory_BS, results.Mean_Memory_BS+results.SD_Memory_BS, alpha=0.25, color="orange")
p = results.plot(ax=ax[1], x='Length',y='Mean_Memory_RS',color="darkmagenta",label="Radix Sort", logy=True)
#p.fill_between(results.Length, results.Mean_Memory_RS-results.SD_Memory_RS, results.Mean_Memory_RS+results.SD_Memory_RS, alpha=0.25, color="darkmagenta")
p = results.plot(ax=ax[1], x='Length',y='Mean_Memory_SS',color="green",label="Binary Spaghetti Sort", ylabel="Memory in KiB", logy=True)
#p.fill_between(results.Length, results.Mean_Memory_SS-results.SD_Memory_SS, results.Mean_Memory_SS+results.SD_Memory_SS, alpha=0.25, color="green")

fig.suptitle('Binary Spaghetti Sort - Random Values [1, length)')
plt.savefig('my_fig.png', dpi=my_dpi)
plt.show()

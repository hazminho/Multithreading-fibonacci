import concurrent.futures
import time
import math
import threading

def matematika(x):
 n = int(math.sqrt(x))
 return n*n == x
def find_fibonacci(n):
 
 return matematika(5*n*n + 4) or matematika(5*n*n - 4)


def do_something():
  for i in range(100):
    if (find_fibonacci(i) == True):
      print(i,"adalah sebuah angka fibonacci")
      time.sleep(1)
    else:
      print(i,"BUKAN sebuah angka fibonacci ")
      


start = time.perf_counter()

threads = []
for i in range(5):
  t = threading.Thread(target=do_something)
  t.start()

  threads.append(t)


for thread in threads:
  thread.join()

finish = time.perf_counter()

executed_time = round(finish - start, 2)
print(f"Finished in {executed_time} second(s)")
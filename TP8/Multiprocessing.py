import multiprocessing
import datetime

def run(self):
    n = 1E7
    while n > 0:
        n -= 1
        print(str(self.ident) + ":" + str(n) + "\n")

start = datetime.datetime.now()
p = multiprocessing.Pool(processes = multiprocessing.cpu_count())
result = p.map(run, range(multiprocessing.cpu_count() * 2 ))

p.close()
p.join()
print(result)

stop = datetime.datetime.now()

print("Duration: ", stop-start)

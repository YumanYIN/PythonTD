import multiprocessing
import datetime

def run(self):
    n = 1E7
    while n > 0:
        n -= 1

if __name__ == "__main__":
    start = datetime.datetime.now()
    p = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    result = p.map(run, range(multiprocessing.cpu_count() * 3))

    p.close()
    p.join()

    stop = datetime.datetime.now()

    print("Duration: ", stop-start)

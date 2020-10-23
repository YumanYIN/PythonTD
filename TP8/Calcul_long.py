import datetime
from threading import Thread

# Calcul long sans Thread
def calcul():
    n = 1E7
    while n > 0:
        n -= 1

# Calcul long avec Thread
class Calcul_long(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        n = 1E7
        while n > 0:
            n -= 1

# Lancer 5 thread
def fiveThreads():
    start = datetime.datetime.now()

    th_1 = Calcul_long()
    th_2 = Calcul_long()
    th_3 = Calcul_long()
    th_4 = Calcul_long()
    th_5 = Calcul_long()

    th_1.start()
    th_2.start()
    th_3.start()
    th_4.start()
    th_5.start()

    th_1.join()
    th_2.join()
    th_3.join()
    th_4.join()
    th_5.join()

    stop = datetime.datetime.now()

    print("Duration de lancer 5 thread par 5 cores: ", stop - start)
    return stop - start


# Lancer la fonction Calcul 5 fois
# return: le temps total
def oneFunctionFiveTimes():
    time2Total = datetime.datetime.now() - datetime.datetime.now()
    for i in range(0, 5):
        start = datetime.datetime.now()
        calcul()
        stop = datetime.datetime.now()
        time2 = stop - start
        time2Total += time2
    #print("Duration de lancer 1 thread 5 fois: ", stop - start)
    return time2Total


if __name__ == '__main__':
    time1 = fiveThreads()
    time2Total = oneFunctionFiveTimes()
    print("Difference: ", time1 - time2Total)





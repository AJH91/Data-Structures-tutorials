import time
import threading


def square_numbers(array):
     for x in array:
         time.sleep(0.2)
         print("Here is your number squared " + str(x*x))

def cubed_numbers(array):
    for x in array:
        time.sleep(0.2)
        print("Here is your number cubed " + str(x*x*x))


#a = [2,4,6,8,10]

#thread1 = threading.Thread(target=square_numbers, args=(a,))
#thread2 = threading.Thread(target=cubed_numbers, args=(a,))

#thread1.start()
#thread2.start()
#thread1.join()
#thread2.join()

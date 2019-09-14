from threading import Thread
import time

boolean = False
x = 1

def Double():
    global boolean
    global x
    while True:
        time.sleep(0.5)
        if boolean:
            break
        x = 2*x
        


class Test(Thread):
    def __init__(self):


    def run(self):

loop = Test()
loop.start()
Double()
print(x)
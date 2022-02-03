# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önce olan işlemler")
#         func(name)
#         print("Fonksiyondan sonra olan işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("Hello ", name)
    
# sayHello("Ali")

import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):

        start = time.time()
        time.sleep(1)

        func(*args, **kwargs)

        finish = time.time()
        print("Fonksiyon "+ func.__name__+": "+ str(finish-start) + " Saniye Sürdü.")
    return inner
@calculate_time
def usAlma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))
@calculate_time
def toplama(a,b):
    print(a+b)

usAlma(2,3)
faktoriyel(4)
toplama(10,20)



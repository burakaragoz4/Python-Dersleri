# def greeting(name):
#     print("Hello", name)
# sayHello = greeting
# # print(sayHello)
# # print(greeting)
# del sayHello
# print(sayHello)
# # print(greeting)

# def outer(num1):
#     print("Outer")

#     def inner_increment(num1):
#         print("Inner")
#         return num1 + 1

#     num2 = inner_increment(num1)  # return den dönen değerdir num1 ise 
#     print(num1, num2)

# outer(10)

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("Number must be an integer")

    if not number >= 0:
        raise ValueError("Number must be zero or positive integer ")
        
    def inner_factorial(number):
        sonuc = 1
        for i in range(1,number+1):
            sonuc = sonuc * i
        return sonuc

    return inner_factorial(number)
print(factorial(5))
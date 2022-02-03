def usAlma(number):

    def inner(power):
        return number ** power 
    
    return inner

two = usAlma(2)
three = usAlma(3)
print(two(3))
print(three(4))
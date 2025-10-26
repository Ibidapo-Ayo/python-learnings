# def say_hello():
#     print("hello")
    
# say_hello()

#parameter
def say_hello(name, emoji="👋"):
    print(f"Hey {name} {emoji}")
    
   

# # positional arguments
# say_hello("Ayomide")

# # keyword arguments
# say_hello( name="Ayomide")

# return statement
# def sum(num1, num2):
#     return num1 + num2

# print(sum(4, 5))

#docstring
# def test(a):
#     '''
#     Info: this function tests and prints param a
#     '''
#     print(a)

# test("!!!!")

# # *args, **kwargs
# def super_func(*args, **kwargs):
    
#     return sum(args)


# print(super_func(1,2,3,4,5,6,7,8,9,10, name="John", age=20))

#exercise: find the highest even number in the list

# def highest_even(li):
#     highest_even_num = 0
#     for item in li:
#         if item % 2 == 0:
#             highest_even_num = max(highest_even_num, item)
#     return highest_even_num

# print(highest_even([10,2,3,4,8,11,12,13,14,15,16,17,18,19,20]))

# def remove_duplicates(li):
#     return list(set(li))

# print(remove_duplicates([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]))

#walrus operator
# a = "helloooooooooooo"
# if((n := len(a)) > 10):
#     print(f"too long {n} elements")

# scope

def outer():
    x = "local x"
    def inner():
        nonlocal x
        x = "nonlocal x"
        print(x)
    inner()
    print(x)
outer()

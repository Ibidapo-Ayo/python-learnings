# palindrome_word = "racecars"

# reverse_word = ""
# for char in palindrome_word:
#     reverse_word = char + reverse_word

# if palindrome_word == reverse_word:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

# my_dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }

# for k, v in my_dict.items():
#     print(k, v)

# exercise counter
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# counter = 0
# for item in my_list:
#     counter += item

# print(f"The sum of the list is {counter}")


# for i in range(0,10, 2):
#     print(i)

#enumerate

for i, char in enumerate(list(range(100))):
    if(char == 50): 
        print(f"index of 50 is: {i}")
    print(i, char)
        
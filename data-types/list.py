amazon_cart = [
    "notebook",
    "sunglasses",
    "toys",
    "grapges"
]

amazon_cart[0] = "laptop"
new_cart = amazon_cart[:]
new_cart[0] = "gum"
print(new_cart)
print(amazon_cart)

# Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(len(matrix))

# List methods
#  Adding mthds - append, extend, insert
basket = ["a","b","c","d","e"]
# basket.append(6) # This modify the list in place
# print(basket)

# Removing mthd
# new_list = basket.pop(2)
# print(new_list)
# basket.remove(2)
# basket.clear()
# print(basket)

print(basket.index("a"))
print("r" in basket)
print(sorted(basket))
basket.reverse()
print(basket)

# List unpacking
a,b, *other, d = [1,2,3,4,5]
print(other)
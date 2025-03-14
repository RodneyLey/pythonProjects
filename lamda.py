#example of lambda function
add = lambda x, y: x + y
print(add(3, 5))

#example of map function
myNumbers = [1, 2, 3, 4, 5]
def square(num):
    return num ** 2

squares = list(map(square, myNumbers))
print(squares) 

#example of map function with lambda
myNumbers = [1, 2, 3, 4, 5]
squares = list(map(lambda num: num ** 2, myNumbers))
print(squares)  
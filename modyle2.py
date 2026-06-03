# x = 10
# y = 3

# print(x // y)  # Floor Division
# print(x % y)  # Modulus

# s = "python"
# print(s[1:4])  # Slicing
# print(s[-1:-5:-3])  # Reversing the string 

# a = [1, 2, 3]
# b = a 
# print(a is b)  # Identity operator
# print(a != b)  # Equality operator

# c = [1, 2, 3]
# d = [1, 2, 3]
# print(c is d)  # Identity operator
# print(c == d)  # Equality operator
# print(c is not d)  # Identity operator
# print(c != d)  # Inequality operator

# fruits = "apple"
# print("c" in fruits)  # Indexing
# print("g" not in fruits)  # Indexing

# x = 5
# y = 5

# if x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")
# else:
#     print("x is less than y")

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# counter = 0
# for letter in alphabet:
#     if letter in ['a', 'e', 'i', 'o', 'u']:
#         counter += 1

# print(f"Number of vowels: {counter}")

# def greet(name):
#     print(f"Hello, {name}!")

# name = greet(input("Enter your name: "))

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("even number")
# else:
#     print("odd number")


# num = [1,18,3,8]
# large_num = 0
# for n in num:
#     if n > large_num:
#         large_num = n

# print(large_num)

# table = int(input("Enter num: "))

# for i in range(1,11):
#     print(table * i)

sum = 0

for i in range(1,11):
    sum += i

print(sum)

word = "python"
# print(word[::-1])

rev = ""

for i in range(len(word)-1, -1,-1):
    rev += word[i]
print(rev)

lst = [1,2,3,4,5]
lst[4] = 18
print(lst)
print(len(lst))

lst[len(lst) -1] = 20
print(lst)

s = {1,2,34,5,46,5,46,4,45,1,4,}
print(s)


list = [1,2,3,5,6,4,5,5,5,6,4,8,9,7,9]
print(len(list))
list[len(list)-8] = 15
print(list)

print(5 in list)

names = ["shyam","rahul","baburao","raju","manu","sohu"]
print("raju" in names)
print(names.index("raju"))
names[3] = "babu bhai"
print(names)

num_list = [1,2,3,4,5,6,7,8,9,10]
square = []

for i in num_list:
    sq = i * i
    square.append(sq)

print(square)
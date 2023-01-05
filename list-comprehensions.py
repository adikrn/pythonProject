# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable] - one way to use list comprehension
#                      list = [expression for item in iterable if conditional] - second way to use list comprehension
#                      list = [expression (if/else) for item in iterable] - third  way to use list comprehension

"""
squares = []
for i in range(1, 11):
    squares.append(i*i)
print(squares)

squares = [i*i for i in range(1,11)]
print(squares)
"""
students = [100,90,80,70,60,50,40,30,20,10]
#
# passed_students = list(filter(lambda x:x>=60, students))
# print(passed_students)

#different ways
# passed_students = [i for i in students if i >= 60]
# passed_students = [str(i) + ": PASS" if i >= 60 else str(i) + ": FAILED" for i in students]
# print(passed_students)

passed_students = [print(str(i) + ": PASS\n") if i >= 60 else print(str(i) + ": FAILED\n") for i in students]

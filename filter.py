#filter() = filter function cerates a collection of elements from an iterable for which a function returns true
#
# filter(function, iterable)

friends = [("rachel", 19),
           ("monica", 18),
           ("phoebe", 17),
           ("joey", 16),
           ("chandler", 21),
           ("ross", 20)]

# test_age = lambda list: True if list[1] >=18 else False # This is also correct
test_age = lambda list:list[1]>=18

above_age = list(filter(test_age, friends))

for i in above_age:
    print(i)
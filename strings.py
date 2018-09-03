#!/bin/usr/env python3

items = ['one', 'two','three','four']
x = ['five','six',]
y = ['zero']
print(items)
for i in items:
    print((i))
items.extend(x)
print(items)
items.append('seven')
print(items)
items.insert(0,'zero')
print(items)
items.insert(len(items),'eight') # for some reason, I cant insert to the end using (-1)
print(items)
pop = items.pop(-1)
print(pop)
print(items)
items.remove('zero')
print(items)
items.reverse()
print(items)
items.sort()
print('Sorted items =',items)

#!/bin/usr/env python3

# in progress -

import os

f = os.chdir('/Users/bnicholls/Movies/python')
print(os.getcwd())

for i in os.listdir():
    f_name, f_ext = os.path.splitext(i)
    #print(f_name)
    f_1, f_2, f_3, f_4, f_5, = f_name.split('-')

    print(f'-{f_1}-{f_2}-{f_3}-{f_4}-{f_ext}')


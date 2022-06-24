# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:01:47 2022

@author: Ariel
"""
my_list = [1,2,3,4,5,6]

class stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
        print(f'success, pushed value {value}')
    
    def pop(self):
        if self.stack != []:
            value = self.stack.pop()
            print(value)
            return value
        else:
            print('empty stack')
            return None
    
my_stack1 = stack()
my_stack2 = stack()

for value in my_list:
    my_stack1.push(value)

while my_stack1.stack != []:
    value = my_stack1.pop()
    my_stack2.push(value)


while my_stack2.stack != []:
    my_stack2.pop()

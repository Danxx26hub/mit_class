#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 23:52:08 2018

        @author: danielgalvan
"""


found = False
low = 0
high = 101
print('please think of a number between 1 and 100!')   
    
while not found:
    ans = (high + low) / 2
    ans = int(ans)
    print('is your secret number {} ? :'.format(str(ans)))
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
            
    if guess == 'h':
        high = ans
    elif guess == 'l':
        low  = ans
    elif guess == 'c':
        print('Awesome! I guessed correct your number is {}'.format(str(ans)))
        break
    else:
        print("I don't understand your input, please try again")

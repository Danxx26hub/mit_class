#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 23:27:38 2018

@author: danielgalvan
"""

import random

print('guess a number between 1 & 100:')

ranNum = random.randint(1, 100)
found = False

while not found:
    guess = int(input('please guess my secret number (between 1 & 100):'))
    if guess == ranNum:
        print('you win! the number was {}'.format(ranNum))
        found = True
    elif guess > ranNum:
        print('guess lower\n')
    else:
        print('guess higher\n')


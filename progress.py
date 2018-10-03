#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 19:45:38 2018

@author: danielgalvan
"""
import sys
import time


def main():
    display_spinner()


def display_spinner():
    print('please wait ......', )
    syms = ['\\', '|', '/', '-']
    bs = '\b'

    for _ in range(8):
        for sym in syms:
            sys.stdout.write('\b%s' % sym)
            sys.stdout.flush()
            time.sleep(.5)


if __name__ == "__main__":
    main()

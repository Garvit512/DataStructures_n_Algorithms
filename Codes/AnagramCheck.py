#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 01:17:21 2019

@author: garvit
"""


def anagram(S1, S2):
    a1 = (S1.replace(' ', '')).lower()
    a2 = (S2.replace(' ', '')).lower()
    counter = 0

    if len(a1) != len(a2):
        print("Not an anagram")
    else:
        L = len(a1)
        for i in a1:
            for j in a2:
                if i == j:
                    a2 = a2.replace(j, '')
                    a1 = a1.replace(i, '')
                    counter += 1
    if (len(a1) == 0 and len(a2) == 0) and counter == L:
        print("Yes it is anagram")


S1 = "public relations"
S2 = "crap built on lies"
obj = anagram(S1, S2)






#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A = tuple(map(int, input("Введите несколько одинаковых элементов и остальные\n").split()))
    c = 0
    for item in A:
        if A[item] == A[item + 1]:
            c += 0
    print("Кол. один. элем.:", c)
    print(A[c:])

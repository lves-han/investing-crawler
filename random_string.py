#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 16:19
# @Author  : eason.han
# @Email   : hanclong@hotmail.com
# @File    : random_string.py
# @Software: PyCharm


"""function random_string(a) {
    var g = 'abcdefghijklmnopqrstuvwxyz0123456789_';
    b = g.length;
    var c,
        d = [];
    for (c = 0; c < a; c++) {
        d.push(g.substr(Math.floor(Math.random() * b), 1))
    };
    return d.join('')
}"""

import math
import random
def random_str():
    g = 'abcdefghijklmnopqrstuvwxyz0123456789_'
    b = len(g)
    d = []
    for i in range(8):
        d.append(g[math.floor(random.random()*b)])
    return "".join(d)

if __name__ == '__main__':
    print(random_str())
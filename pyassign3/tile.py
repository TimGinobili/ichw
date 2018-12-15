#!/usr/bin/env python3

"""tile.py: Print all the solutions to fill a wall(m * n) using tiles(a * b)
and visualize one of them.
__author__ = "Xiao Niu"
__pkuid__  = "1800011701"
__email__  = "1800011701@pku.edu.cn"
"""

#调用copy和turtle模块
import copy
import turtle

#铺砖函数
def tile(wall, m, n, a, b, direc):
    """
    :param wall:the list that records the state of the wall,
    in which 1 represents alredy filled and 0 represents not.
    :param m: the length of the wall.
    :param n: the width of the wall.
    :param a: the length of the tile.
    :param b: the width of the tile.
    :param direc: the direction of the tile.
    :return: one solution to fill the wall
    """
    oneans = []
    newwall = list(wall)
    if direc == 0:
        for i in range(b):
            for x in range(newwall.index(0) + i * m, newwall.index(0) + i * m + a):
                oneans.append(x)
                wall[x] = 1
    if direc == 1:
        for i in range(a):
            for x in range(newwall.index(0) + i * m, newwall.index(0) + i * m + b):
                oneans.append(x)
                wall[x] = 1
    return tuple(oneans)

#检测函数
def already(wall, m, n, a, b, direc):
    """
    :param wall:the list that records the state of the wall,
    in which 1 represents alredy filled and 0 represents not.
    :param m: the length of the wall.
    :param n: the width of the wall.
    :param a: the length of the tile.
    :param b: the width of the tile.
    :param direc: the direction of the tile.
    :return: True or False which represents the wall can be filled or not.
    """
    if 0 not in wall:
        return True
    elif direc == 0 and (wall.index(0) % m + a) <= m:
            for i in range(b):
                for x in range(wall.index(0) + i * m, wall.index(0) + i * m + a):
                    try:
                        if wall[x] == 1:
                            return True
                    except IndexError:
                        return True
            return False
    elif direc == 1 and (wall.index(0) % m + b) <= m:
            for i in range(a):
                for x in range(wall.index(0) + i * m, wall.index(0) + i * m + b):
                    try:
                        if wall[x] == 1:
                            return True
                    except IndexError:
                        return True
            return False
    else:
        return True

#执行函数
def fill(wall, m, n, a, b):
    """
    :param wall:the list that records the state of the wall,
    in which 1 represents alredy filled and 0 represents not.
    :param m: the length of the wall.
    :param n: the width of the wall.
    :param a: the length of the tile.
    :param b: the width of the tile.
    :return: all the solutions to fill the wall.
    """
    if wall == [1] * len(wall):
        return[[]]
    ans = []
    for direc in 0, 1:
        if not already(wall, m, n, a, b, direc):
            newwall = copy.deepcopy(wall)
            oneans = tile(newwall, m, n, a, b, direc)
            parts = fill(newwall, m, n, a, b)
            for part in parts:
                part.append(oneans)
            ans.extend(parts)
    return ans

#可视化函数
def visualization(m, n, onesol):
    """
    Visualize a chosen solution by turtle
    :param m: the length of the wall.
    :param n: the width of the wall.
    :param onesol: the solution which the user choose to fill the wall.
    """
    w = turtle.Turtle()
    w.speed(0)
    w.pensize(5)
    t = turtle.Turtle()
    t.color("blue")
    t.speed(0)
    t.pensize(3)
    p = turtle.Turtle()
    p.speed(0)
    p.pensize(1)

    x = (40000 * m / n) ** 0.5
    y = (40000 * n / m) ** 0.5
    w.hideturtle()
    w.penup()
    w.goto(x, 0)
    w.pendown()
    w.goto(x, y)
    w.goto(- x, y)
    w.goto(- x, - y)
    w.goto(x, - y)
    w.goto(x, 0)

    for a in range(n):
        for b in range(m):
            p.penup()
            p.hideturtle()
            p.goto(b * x / m * 2 - x + x / m, a * y / n * 2 - y + y / n)
            p.pendown()
            p.write(b + m * a, align="center", font=("Times New Roman", int((5000/(m*n))**0.5)))
    turtle.done

    for i in onesol:
        x1 = (i[0] % m) * 2 * x / m - x
        y1 = (i[0] // m) * 2 * y / n - y
        x2 = (i[-1] % m + 1) * 2 * x / m - x
        y2 = (i[-1] // m + 1) * 2 * y / n - y
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y1)
        t.goto(x2, y2)
        t.goto(x1, y2)
        t.goto(x1, y1)

#main函数
def main():
    """the main module
    """
    m = int(input('请输入墙的长度：'))
    n = int(input('请输入墙的宽度：'))
    a = int(input('请输入瓷砖的长度：'))
    b = int(input('请输入瓷砖的宽度：'))
    wall = [0] * m * n
    ans = fill(wall, m, n, a, b)
    if len(ans) == 0:
        print('不存在可将墙铺满的方法')
    else:
        print('共有', len(ans), '种铺法，显示如下：')
        for i in ans:
            print(i)
        numonesol = turtle.numinput('展示铺法','请输入您想要展示的铺法序号：(1 - ' + str(len(ans)) + ')',
                                minval = 1, maxval = len(ans))
        onesol = ans[int(numonesol) - 1]
        visualization(m, n, onesol)

if __name__ == '__main__':
    main()
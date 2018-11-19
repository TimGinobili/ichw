#!/usr/bin/env python3

"""solar.py: planets

__author__ = "niuxiao"
__pkuid__  = "1800011701"
__email__  = "1800011701@pku.edu.cn"
"""

import turtle
import math

#背景颜色
turtle.bgcolor('black')

#画一个太阳
t = turtle.Turtle()
t.color('red')
t.shape('circle')
t.turtlesize(1)

#行星数据
pls = []
colors = ['grey', 'yellow', 'blue', 'darkred', 'brown', 'green']
size = [0.6, 0.8, 1.0, 0.6, 1.5, 1.25]
la = [50, 90, 130, 180, 235, 300]
lb = [40, 70, 110, 150, 190, 260]
dr = [10, 1, 2, 20, 20, 30]
sp = [1, 2, 3, 6, 8, 12]

#画出行星
for i in range(6):
    t = turtle.Turtle()
    t.color(colors[i])
    t.speed(0)
    t.turtlesize(size[i])
    t.shape('circle')
    t.penup()
    t.goto(la[i]+dr[i],0)
    t.pendown
    pls.append(t)
    
#运行函数
def run(i):
    """行星运行函数
    """
    x=la[i%6] * math.cos(math.radians(i/sp[i%6]))+dr[i%6]
    y=lb[i%6] * math.sin(math.radians(i/sp[i%6]))
    pls[i%6].goto(x,y)
    pls[i%6].pendown()
    if i/sp[i%6] >= 360:
        pls[i%6].penup()

def main():
    """行星开始运行
    """
    while True:
	    for i in range(0,360*2*3*6*8*12):
		    run(i)

if __name__ == '__main__':
    main()
    

#/use/bin/env python3
#coding: UTF-8

import matplotlib.pyplot as plt
from matplotlib import cm
import pylab
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from math import *

'''В этом модуле рисуется график функции и найденная точка минимума'''

#Функция Розенброка
def rosenbrock(x,y):
    return (1-x)**2+100*(y-x**2)**2

#Функция для симплекс-метода - она одна
def function_for_simples(x1,x2):
    return 2*x1**2+2*x1*x2+2*x2**2-4*x1-6*x2

#Функция сферы
def sphere_function(x,y):
    return x*x+y*y

#Функция Растригина
def rastrigin_function(x,y):
    return 20+(x*x - 10*np.cos(2*pi*x) + y*y - 10*np.cos(2*pi*y))

#Функция Швефеля
def chwefel_function(x,y):
    return (-x * np.sin (np.sqrt (np.abs (x))))+(-y * np.sin (np.sqrt (np.abs (y))))

#Функция Химмельблау
def himmelblow_function(x,y):
    return (x**2+y-11)**2+(x+y**2 - 7)**2

#Функция Голдштейна
def goldstein_function(x1,x2):
    return (1.0 + ( (x1 + x2 + 1.0) ** 2 ) * \
                                            (19.0 - 14.0 * x1 + 3.0 * x1 * x1 - 14.0 * x2  + 6.0 * x1 * x2 + 3.0 * x2 *x2) ) * \
                                            (30.0 + ( (2.0 * x1 - 3.0 * x2) ** 2 ) * \
                                            (18.0 - 32.0 * x1 + 12.0 * x1 * x1 + 48.0 * x2 - 36.0 * x1 * x2 + 27.0 * x2 * x2) )    

'''
Параметры:
1. Номер функции
   0 - Розенброка
   1 - Квадратичная
   2 - сферы
   3 - Растригина
   4 - Швефеля
   5 - Химмельблау
   6 - Голдштейна
2. Точка минимума
3-6 минимальные и максимальные значения координат
7. Путь к картинке
'''
def draw_function(num_function,point, minx, maxx, miny, maxy, path):
    fig=plt.figure()
    ax=fig.gca(projection='3d')
    #plt.hold(True)
    X=np.arange(minx,maxx,(maxx-minx)/300)
    Y=np.arange(miny,maxy,(maxx-minx)/300)
    X,Y=np.meshgrid(X,Y)
    #print(X)
    #print(Y)
    if num_function==0:
        Z=rosenbrock(X,Y)
    elif num_function==1:
        Z=function_for_simples(X,Y)
    elif num_function==2:
        Z=sphere_function(X,Y)
    elif num_function==3:
        Z=rastrigin_function(X,Y)
    elif num_function==4:
        Z=chwefel_function(X,Y)
    elif num_function==5:
        Z= himmelblow_function(X,Y)
    elif num_function==6:
        Z=goldstein_function(X,Y)
        
    xs=[point[0][0]]
    ys=[point[0][1]]
    zs=[point[1]]
    surf=ax.plot_surface(X,Y,Z, cmap=cm.coolwarm, linewidth=0, antialiased=False, alpha=0.3)
    plt.xlabel("x")
    plt.ylabel("y")
    ax.scatter(xs,ys,zs,c='r', marker='o', s=[10])
    plt.savefig(path+"\\graphic_1.png")
    ax.view_init(89,269)
    plt.savefig(path+"\\graphic_2.png")
    #plt.show()
    return [path+"\\graphic_1.png", path+"\\graphic_2.png"]

#draw_function(4,[[0,0],1], -4, 4, -4, 4,"C:\\Users\\--\\Desktop\\Optimization")
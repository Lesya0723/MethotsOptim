#!/usr/bin/python
# -*- coding: UTF-8 -*-
from runoptimize_rastrigin import rastrigin_swarm_run
from runoptimize_schwefel import schewefel_swarm_run
from runoptimize_x2 import x2_swarm_run

'''
Параметры:
1. Количество итераций
2. Размер роя
3. Оптимизируемая функция:
    0 - функция Растригина
    1 - функция Швефеля
    2 - функция сферы
Количкство измерений всегда 2
'''

def main_swarm_function(iterCount,swarmsize,function):
    dimension=2
    if function==0:
        return rastrigin_swarm_run(dimension,iterCount,swarmsize)
    if function==1:
        return schewefel_swarm_run(dimension,iterCount,swarmsize)
    if function==2:
        return x2_swarm_run(dimension,iterCount,swarmsize)

#/use/bin/env python3
#coding: UTF-8
from bacteria_algorithm import bacteria_algorithm
from Genetic_algorithm import genetic_algorithm
from imm_algorithm import immun_algorithm
from beetest import bee_algorithm
from swarm_algorithm import main_swarm_function
from Simplex import start_count
from quickest_descent import quickest_descent
from hybrid_algorithm import hybrid_algorithm

from opt_graphics import draw_function

'''
Главная функция.
Параметры:
1. Алгоритм оптимизации (он же номер лабы)
   1 - Наискорейший спуск
   2 - Симплекс-метод
   3 - Генетичнский алгоритм
   4 - Роевый алгоритм
   5 - Пчелиный алгоритм
   6 - Алгоритм иммунной сети
   7 - Алгоритм бактериальной оптимизации
   8 - Гибридный алгоритм
2. Путь к папке с картинками (для отрисовки функции)
3. Параметры алгоритма оптимизации (для каждого свой набор)
4. Ограничения на обрасть отрисовки в формате:
    [[min_x, max_x],[min_y, max_y]]
    
Внимание! Все функции от двух параметров
'''

def main_function_optimize(algorithm, path, p, bounds):
	if algorithm==1:
		point=quickest_descent(p[0],p[1],p[2], p[3], p[4])
		num_function=5
	elif algorithm == 2:
		point=start_count()
		num_function=1
	elif algorithm== 3:
		point=genetic_algorithm(p[0],p[1],p[2], p[3], p[4], p[5],p[6],p[7],p[8],p[9],p[10])
		num_function=0
	elif algorithm==4:
		point=main_swarm_function(p[0],p[1],p[2])
		
		if p[2]==0:
			num_function=3
		elif p[2]==1:
			num_function=4
			bounds[0][0]=point[0][0]-2
			bounds[0][1]=point[0][0]+2
			bounds[1][0]=point[0][1]-2
			bounds[1][1]=point[0][1]+2            
		elif p[2]==2:
			num_function=2
	elif algorithm==5:
		point=bee_algorithm(p[0],p[1],p[2], p[3], p[4], p[5],p[6],p[7],p[8])
		if p[0]==0:
			num_function=2
		elif p[0]==2:
			num_function=6
		elif p[0]==3:
			num_function=0
	elif algorithm==6:
		point=immun_algorithm(p[0],p[1],p[2], p[3], p[4], p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12])
		num_function=0
	elif algorithm==7:
		point=bacteria_algorithm(p[0],p[1],p[2], p[3], p[4], p[5],p[6],p[7], p[8])
		num_function=2
	elif algorithm==8:
		point=hybrid_algorithm(p[0],p[1],p[2], p[3], p[4], p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13])
		num_function=5

	graphic=draw_function(num_function, point, bounds[0][0], bounds[0][1], bounds[1][0], bounds[1][1], path)
	draw_function(num_function, point, bounds[0][0], bounds[0][1], bounds[1][0], bounds[1][1], path)
	
	return [point[0][0], point[0][1], point[1]], [graphic[0], graphic[1]]
  
#main_function_optimize(1,"C:\\Users\\--\\Desktop\\Optimization", [-3,5,100, 0.01, 0.01], [[-4,4],[-4,4]])
#main_function_optimize(2, "C:\\Users\\--\\Desktop\\Optimization", [], [[-4,4],[-4,4]])
#main_function_optimize(3, "C:\\Users\\--\\Desktop\\Optimization", [100, -2,2,-2,2,0,0,0,0.05,0.1,5], [[-2,2],[-2,2]])
#main_function_optimize(4, "C:\\Users\\--\\Desktop\\Optimization", [100,50,2], [[-4,4],[-4,4]])
#main_function_optimize(5, "C:\\Users\\--\\Desktop\\Optimization", [3,300,10,30,15,5,1, 500, 10], [[-4,4],[-4,4]])
#main_function_optimize(6, "C:\\Users\\--\\Desktop\\Optimization", [-2, 2, -2,2,50,50,10,5, 7,0.2,100,0.2,0.2],[[-2,2],[-2,2]])
#main_function_optimize(7, "C:\\Users\\--\\Desktop\\Optimization", [-3, 3, -3, 3, 10, 250, 0.1, 5, 0.1], [[-1,1],[-1,1]])
#main_function_optimize(8,"C:\\Users\\--\\Desktop\\Optimization",[100, -5,5,-5,5,0,0,0,0.05,0.1,5,   100, 0.01, 0.01],[[-5,5],[-5,5]])
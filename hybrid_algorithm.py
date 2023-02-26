#/use/bin/env python3
#coding: UTF-8

from quickest_descent import quickest_descent
import random



#оптимизируемая функция
def function(x,y):
    return (x**2+y-11)**2+(x+y**2 - 7)**2

#Генерация начальной популяции
def generate_population(num_persons,min_x,max_x,min_y,max_y):
    population=[]
    for i in range(num_persons):
        population.append([random.uniform(min_x,max_x), random.uniform(min_y,max_y)])
    return population
                          
#селекция усечением
def truncation_selection(num_persons, population):
    new_population=[]
    for i in population:
        new_population.append([function(i[0],i[1]), i[0], i[1]])
    new_population.sort()
    result=[]
    for i in range(num_persons):
        percent=random.uniform(0,1)
        person=random.randint(0,int(len(new_population)*percent))
        result.append([new_population[person][1],new_population[person][2]])
    return result

#элитарная селекция
def elite_selection(num_persons,population):
    new_population=[]
    for i in population:
        new_population.append([function(i[0], i[1]), i[0], i[1]])
    new_population.sort()
    result=[]
    elite=int(num_persons*0.1)
    for i in range(elite):
        result.append([new_population[elite][1],new_population[elite][2]])
    n_pop=truncation_selection(num_persons-elite, population[elite:])
    result+=n_pop
    return result

#панмиксия
def panmixy(population):
    parents_pairs=[]
    num_persons=len(population)
    for i in range(num_persons):
        second_parent=random.randint(0,num_persons-1)
        parents_pairs.append([population[i],population[second_parent]])
    return parents_pairs

def get_distance(parent_1,parent_2):
    return (parent_1[0]-parent_2[0])**2+(parent_1[1]-parent_2[1])

#инбридинг
#метод=0 для генотипа, 1 - для фенотипа
def inbriding(population,method):
    #это по фенотипу - значению функции
    if method==1:
        parents_pairs=[]
        function_values=[]
        for i in range (len(population)):
            function_values.append(function(population[i][0],population[i][1]))
        for i in range(len(population)):
            mn=abs(function_values[i] - function_values[1 if i==0 else 0])
            second_parent = 1 if i==0 else 0
            for j in range(len(population)):
                if j!=i and abs(function_values[i]-function_values[j])<mn:
                    second_parent=j
                    mn=abs(function_values[i]-function_values[j])
            parents_pairs.append([population[i],population[second_pair]])
        return parents_pairs
    #теперь по генотипу - значениям переменных
    parents_pairs=[]
    for i in range(len(population)):
        mn=get_distance(population[i],population[1 if i==0 else 0])
        second_parent = 1 if i==0 else 0
        for j in range(len(population)):
            if j!=i and get_distance(population[i],population[j])<mn:
                mn=get_distance(population[i],population[j])
                second_parent=j
        parents_pairs.append([population[i],population[second_parent]])
    return parents_pairs
        
#аутбридинг
#аналогично метод=0 для генотипа, 1 - для фенотипа
def outbriding(population,method):
    #это по фенотипу - значению функции
    if method==1:
        parents_pairs=[]
        function_values=[]
        for i in range (len(population)):
            function_values.append(function(population[i][0],population[i][1]))
        for i in range(len(population)):
            mx=abs(function_values[i] - function_values[0])
            second_parent = 0
            for j in range(len(population)):
                if j!=i and abs(function_values[i]-function_values[j])>mx:
                    second_parent=j
                    mx=abs(function_values[i]-function_values[j])
            parents_pairs.append([population[i],population[second_parent]])
        return parents_pairs
    #теперь по генотипу - значениям переменных
    parents_pairs=[]
    for i in range(len(population)):
        mx=get_distance(population[i],population[0])
        second_parent = 0
        for j in range(len(population)):
            if j!=i and get_distance(population[i],population[j])>mx:
                mn=get_distance(population[i],population[j])
                second_parent=j
        parents_pairs.append([population[i],population[second_parent]])
    return parents_pairs
     
#промежуточная рекомбинация                   
def intermediate_recombination(parent_pairs):
    new_population=[]
    for i in range(len(parent_pairs)):
        alpha_1=random.uniform(-0.25,1.25)
        alpha_2=random.uniform(-0.25,1.25)
        parent_1=parent_pairs[i][0]
        parent_2=parent_pairs[i][1]
        new_population.append([parent_1[0]+alpha_1*(parent_2[0]-parent_1[0]), parent_1[1]+alpha_1*(parent_2[1]-parent_1[1])])
    return new_population


#мутация
def mutation(population,chance,step):
    for i in range(len(population)):
        for j in range(2):
            val=random.uniform(0,1)
            #мутация
            if val<chance:
                population[i][j]+= step if val<chance/2 else -step
    return population
         

def genetic_algorithm(num_persons,min_x,max_x,min_y,max_y,parent_choice,method,selection,mutation_chance,mutation_step, num_generations):
    population=generate_population(num_persons,min_x,max_x,min_y,max_y)
    for gen in range (num_generations):
        #Выбор родителей
        if parent_choice==0:
            parents=panmixy(population)
        elif parent_choice==1:
            parents=inbriding(population,method)
        elif parent_choice==2:
            parents=outbriding(population,method)
        #Скрещивание и мутация
        children=intermediate_recombination(parents)
        children=mutation(children,mutation_chance,mutation_step)
        
        #Выбор особей следующего поколения
        population+=children
        if selection==0:
            population=truncation_selection(num_persons, population)
        elif selection==1:
            population=elite_selection(num_persons,population)
    
    #print(p,"%.3f" % mn)
    #print(population)
    return population

#genetic_algorithm(100, -5,5,-5,5,0,0,0,0.05,0.1,5)
#print("")
#genetic_algorithm(100, -5,5,-5,5,1,0,0,0.05,0.1,25)
#print("")
#genetic_algorithm(100, -5,5,-5,5,2,1,0,0.05,0.1,100)
#print("")

'''Гибридный алгоритм = генетический + наискорейшего спуска
Параметры: 
1. Число особей
2-5. Минимальные и максимальные значения переменных
6. Способ выбора родителей
    0 - Панмиксия
    1 - Инбридинг
    2 - Аутбридинг
7. Метод выбора родителей (только для инбридинга и аутбридинга)
    0 - по генотипу
    1 - по фенотипу
8. Селекция особей
    0 - Отсечением
    1 - Элитарная
9. Вероятность мутации
10. Шаг мутации
11. Число поколений генетического алгоритма
12. Число итераций наискорейшего спуска
13. Погрешность для градиента
14. Погрешность для функции'''
def hybrid_algorithm(num_persons,min_x,max_x,min_y,max_y,parent_choice,method,selection,mutation_chance,mutation_step, num_generations, iterations, ep1, ep2):
    #Запускаем генетический
    population=genetic_algorithm(num_persons,min_x,max_x,min_y,max_y,parent_choice,method,selection,mutation_chance,mutation_step, num_generations)
    #Для каждой особи выполняем наискорейший спуск
    min_population=[]
    for item in population:
        #print(item)
        min_population.append(quickest_descent(item[0],item[1],iterations, ep1, ep2))
        #print(min_population[-1])
    min_population.sort(key=lambda a: a[1])
    #print(min_population[0])
    return min_population[0]
    
    
#hybrid_algorithm(100, -5,5,-5,5,0,0,0,0.05,0.1,5,   100, 0.01, 0.01)
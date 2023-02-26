#/use/bin/env python3
#coding: UTF-8

#получаем ключ
def get_key(lst,val):
    for i in range(len(lst)):
        if lst[i]==val:
            return i
    return -1
 
#находим разрешающую строку и столбец
def simple_find_row_col(matrix):
    #сначала столбец
    mx=0
    col=-1
    for i in range(0,len(matrix[-1])-1):
        if matrix[-1][i]>mx:
            mx=matrix[-1][i]
            col=i
    if col==-1:
        return [-1,-1]
    #теперь строка
    mn=matrix[0][-1]/matrix[0][col]
    row=0
    for i in range(1,len(matrix)-1):
        if matrix[i][-1]/matrix[i][col]<mn and matrix[i][-1]/matrix[i][col]>0:
            mn=matrix[i][-1]/matrix[i][col]
            row=i
    return [row,col]

#меняем матрицу
def simple_change_matrix(rows,cols,matrix,row,col):
    #обрабатываем элемент на пересечении
    matrix[row][col]**=-1
    #обрабатываем остальные элементы матрицы, кроме нужной строки и столбца
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if i!=row and j!=col:
                matrix[i][j]=matrix[i][j]-(matrix[row][j]*matrix[i][col])*matrix[row][col]
    #обрабатываем строчку
    for i in range(0,len(matrix[row])):
        if i!=col:
            matrix[row][i]*=matrix[row][col]
    #теперь столбец
    for i in range(0,len(matrix)):
        if i!=row:
            matrix[i][col]*=-matrix[row][col]
    #переобозначаем базис
    rows[row],cols[col]=cols[col],rows[row]
    
def simple_simplex(matrix,rows,cols,variables):
    while True:
        #находим разрешающую строку и столбец
        rw,cl=simple_find_row_col(matrix)
        #если не нашли - алгоритм завершается
        if (rw==-1):
            res=[]
            for var in variables:
                key=get_key(rows,var)
                #если переменная есть в базисных, то выводим её
                if key!=-1:
                    #print(var," = ",matrix[key][-1])
                    res.append(matrix[key][-1])
            #print("F = ",funct(res[0],res[1]))
            res.append(funct(res[0],res[1]))
            return res
        #иначе меняем матрицу
        simple_change_matrix(rows,cols,matrix,rw,cl)
        #print_matrix(matrix,rows,cols)
        
                
def print_matrix(matrix,rows,cols):
    print("\t",end="")
    for cl in cols:
        print(cl,end="\t")
    print("")
    for i in range(0,len(matrix)-1):
        print(rows[i],end="\t")
        for j in range(len(matrix[0])):
            print("%.2f" % matrix[i][j],end="\t")
        print("")
    print("\t",end="")
    for j in range(len(matrix[0])):
        print("%.2f" % matrix[-1][j],end="\t")    
    print("")

def funct(x1,x2):
    return 2*x1**2+2*x1*x2+2*x2**2-4*x1-6*x2

'''
Запускать эту функцию
Вернёт список из значений двух переменных и значения функции в этой точке
'''
def start_count():
    rows=["z1","z2","w"]
    cols=["x1","x2","lmbd","v1","v2"]
    variables=["x1","x2"]
    matr=[[4,2,1,-1,0,4],[2,4,2,0,-1,6],[1,2,0,0,0,2],[6,6,3,-1,-1,10]]
    res=simple_simplex(matr,rows,cols,variables)
    #print(res)
    return [[res[0],res[1]],res[2]]

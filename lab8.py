#!c:\Users\я\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
from main_function_optimize import main_function_optimize

form = cgi.FieldStorage()
num_persons = form.getfirst("num_persons", "")
minx = form.getfirst("minx", "")
maxx = form.getfirst("maxx", "")
miny = form.getfirst("miny", "")
maxy = form.getfirst("maxy", "")
choise_parents = form.getfirst("choise_parents", "")
type_choise = form.getfirst("type_choise", "")
selection = form.getfirst("selection", "")
poss_mutation = form.getfirst("poss_mutation", "")
mutation_step = form.getfirst("mutation_step", "")
num_generations = form.getfirst("num_generations", "")
num_iterations = form.getfirst("num_iterations", "")
gradient_error = form.getfirst("gradient_error", "")
function_error = form.getfirst("function_error", "")

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html>
    <head>
        <!-- <meta charset="utf-8"> -->
        <title>Гибридный</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
		<center>
			<header>
				<ol>
					<li><a href="/">Лабораторные работы</a></li>
				</ol>
				<h1>Гибридный</h1>
			</header>
			<section>
				<form action="/lab8.py" method="POST" name="lab8-form">
					<h2>Параметры генетического</h2>
					<label>Число особей</label>
					<input required="" type="number" placeholder="Число особей" value="%s" name="num_persons">
					<hr>
					<label>Минимальные и максимальные значения переменных</label>
					<input required="" type="text" placeholder="Минимальное значение х" value="%s" name="minx">
					<input required="" type="text" placeholder="Максимальное значение х" value="%s" name="maxx">
					<input required="" type="text" placeholder="Минимальное значение у" value="%s" name="miny">
					<input required="" type="text" placeholder="Максимальное значение у" value="%s" name="maxy">
					<hr>
					<label>Способ выбора родителей</label>
					<select name="choise_parents">
						<option disabled>Способ выбора родителей</option>""" % (num_persons, minx, maxx, miny, maxy))
						
if (choise_parents == "0"):
	print("""<option value="0" selected>Панмиксия</option>""")
else:
	print("""<option value="0">Панмиксия</option>""")
	
if (choise_parents == "1"):
	print("""<option value="1" selected>Инбридинг</option>""")
else:
	print("""<option value="1">Инбридинг</option>""")
	
if (choise_parents == "2"):
	print("""<option value="2" selected>Аутбридинг</option>""")
else:
	print("""<option value="2">Аутбридинг</option>""")
	
print("""</select>
					<hr>
					<label>Метод выбора родителей</label>
					<select name="type_choise">
						<option disabled>Метод выбора родителей</option>""")
						
if (type_choise == "0"):
	print("""<option value="0" selected>По генотипу</option>""")
else:
	print("""<option value="0">По генотипу</option>""")
	
if (type_choise == "1"):
	print("""<option value="1" selected>По фенотипу</option>""")
else:
	print("""<option value="1">По фенотипу</option>""")

print("""</select>
					<hr>
					<label>Селекция особей</label>
					<select name="selection">
						<option disabled>Селекция особей</option>""")
						
if (selection == "0"):
	print("""<option value="0" selected>Отсечением</option>""")
else:
	print("""<option value="0">Отсечением</option>""")
	
if (selection == "1"):
	print("""<option value="1" selected>Элитарная</option>""")
else:
	print("""<option value="1">Элитарная</option>""")

print("""</select>
					<hr>
					<label>Вероятность мутации</label>
					<input required="" type="text" placeholder="Вероятность мутации" value="%s" name="poss_mutation">
					<hr>
					<label>Шаг мутации</label>
					<input required="" type="text" placeholder="Шаг мутации" value="%s" name="mutation_step">
					<hr>
					<label>Число поколений генетического алгоритма</label>
					<input required="" type="number" placeholder="Число поколений генетического алгоритма" value="%s" name="num_generations">
					<hr>
					<h2>Параметры наискорейшего спуска</h2>
					<label>Число итераций наискорейшего спуска</label>
					<input required="" type="number" placeholder="Максимальное количество итераций" value="%s" name="num_iterations">
					<hr>
					<label>Погрешность для градиента</label>
					<input required="" type="text" placeholder="Погрешность для градиента" value="%s" name="gradient_error">
					<hr>
					<label>Погрешность для функции</label>
					<input required="" type="text" placeholder="Погрешность для функции" value="%s" name="function_error">
					<hr><input type="submit" value="НАЧАТЬ">
				</form>""" % (poss_mutation, mutation_step, num_generations, num_iterations, gradient_error, function_error))
					
if os.getenv("REQUEST_METHOD") == "POST":
	if num_persons != "" and minx != "" and maxx != "" and miny != "" and maxy != "" and choise_parents != "" and type_choise != "" and selection != "" and poss_mutation != "" and mutation_step != "" and num_generations != "" and num_iterations != "" and gradient_error != "" and function_error != "":
		num_persons = int(num_persons)
		minx = float(minx)
		maxx = float(maxx)
		miny = float(miny)
		maxy = float(maxy)
		choise_parents = int(choise_parents)
		type_choise = int(type_choise)
		selection = int(selection)
		poss_mutation = float(poss_mutation)
		mutation_step = float(mutation_step)
		num_generations = int(num_generations)
		num_iterations = int(num_iterations)
		gradient_error = float(gradient_error)
		function_error = float(function_error)
		p = [num_persons, minx, maxx, miny, maxy, choise_parents, type_choise, selection, poss_mutation, mutation_step, num_generations, num_iterations, gradient_error, function_error]
		point, graphic = main_function_optimize(8, "Optimization", p, [[-5, 5], [-5, 5]])
		print("""<hr>
		<label>Найденная точка</label>
		<p>x = %f</p>
		<p>y = %f</p>
		<p>f(x, y) = %f</p>""" % (point[0], point[1], point[2]))
		print("""<hr>
		<label>Вид сбоку</label>
		<img src="%s">""" % graphic[0])
		print("""<hr>
		<label>Вид сверху</label>
		<img src="%s">""" % graphic[1])

print("""</section></center></body></html>""")
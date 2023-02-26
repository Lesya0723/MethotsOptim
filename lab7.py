#!c:\Users\я\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
from main_function_optimize import main_function_optimize

form = cgi.FieldStorage()
minx = form.getfirst("minx", "")
maxx = form.getfirst("maxx", "")
miny = form.getfirst("miny", "")
maxy = form.getfirst("maxy", "")
num_bacteries = form.getfirst("num_bacteries", "")
num_iterations = form.getfirst("num_iterations", "")
speed = form.getfirst("speed", "")
liquid_persons = form.getfirst("liquid_persons", "")
liquid_poss = form.getfirst("liquid_poss", "")

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html>
    <head>
        <!-- <meta charset="utf-8"> -->
        <title>Алгоритм бактериальной оптимизации</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
		<center>
			<header>
				<ol>
					<li><a href="/">Лабораторные работы</a></li>
				</ol>
				<h1>Алгоритм бактериальной оптимизации</h1>
			</header>
			<section>
				<form action="/lab7.py" method="POST" name="lab7-form">
					<label>Минимальные и максимальное значения координат</label>
					<input required="" type="text" placeholder="Минимальное значение х" value="%s" name="minx">
					<input required="" type="text" placeholder="Максимальное значение х" value="%s" name="maxx">
					<input required="" type="text" placeholder="Минимальное значение у" value="%s" name="miny">
					<input required="" type="text" placeholder="Максимальное значение у" value="%s" name="maxy">
					<hr>
					<label>Размер популяции</label>
					<input required="" type="number" placeholder="Размер популяции" value="%s" name="num_bacteries">
					<hr>
					<label>Количество итераций изменения популяции (суммарное число шагов)</label>
					<input required="" type="number" placeholder="Количество итераций изменения популяции (суммарное число шагов)" value="%s" name="num_iterations">
					<hr>
					<label>Размер шага (скорость)</label>
					<input required="" type="text" placeholder="Размер шага (скорость)" value="%s" name="speed">
					<hr>
					<label>Количество особей, уничтожаемых в ходе ликвидации</label>
					<input required="" type="number" placeholder="Количество особей, уничтожаемых в ходе ликвидации" value="%s" name="liquid_persons">
					<hr>
					<label>Вероятность ликвидации</label>
					<input required="" type="text" placeholder="Вероятность ликвидации" value="%s" name="liquid_poss">
					<hr><input type="submit" value="НАЧАТЬ">
				</form>""" % (minx, maxx, miny, maxy, num_bacteries, num_iterations, speed, liquid_persons, liquid_poss))
					
if os.getenv("REQUEST_METHOD") == "POST":
	if minx != "" and maxx != "" and miny != "" and maxy != "" and num_bacteries != "" and num_iterations != "" and speed != "" and liquid_persons != "" and liquid_poss != "":
		minx = float(minx)
		maxx = float(maxx)
		miny = float(miny)
		maxy = float(maxy)
		num_bacteries = int(num_bacteries)
		num_iterations = int(num_iterations)
		speed = float(speed)
		liquid_persons = int(liquid_persons)
		liquid_poss = float(liquid_poss)
		p = [minx, maxx, miny, maxy, num_bacteries, num_iterations, speed, liquid_persons, liquid_poss]
		point, graphic = main_function_optimize(7, "Optimization", p, [[-1, 1], [-1, 1]])
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
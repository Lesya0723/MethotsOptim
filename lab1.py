#!c:\Users\я\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
from main_function_optimize import main_function_optimize

form = cgi.FieldStorage()
coord_x = form.getfirst("coord_x", "")
coord_y = form.getfirst("coord_y", "")
max_iterations = form.getfirst("max_iterations", "")
gradient_error = form.getfirst("gradient_error", "")
function_error = form.getfirst("function_error", "")

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html>
    <head>
        <!-- <meta charset="utf-8"> -->
        <title>Наискорейший спуск</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
		<center>
			<header>
				<ol>
					<li><a href="/">Лабораторные работы</a></li>
				</ol>
				<h1>Наискорейший спуск</h1>
			</header>
			<section>
				<form action="/lab1.py" method="POST" name="lab1-form">
					<label>Координаты начальной точки</label>
					<input required="" type="text" placeholder="Координата х" value="%s" name="coord_x">
					<input required="" type="text" placeholder="Координата у" value="%s" name="coord_y">
					<hr>
					<label>Максимальное количество итераций</label>
					<input required="" type="number" placeholder="Максимальное количество итераций" value="%s" name="max_iterations">
					<hr>
					<label>Погрешность для градиента</label>
					<input required="" type="text" placeholder="Погрешность для градиента" value="%s" name="gradient_error">
					<hr>
					<label>Погрешность для функции</label>
					<input required="" type="text" placeholder="Погрешность для функции" value="%s" name="function_error">
					<hr><input type="submit" value="НАЧАТЬ">
				</form>""" % (coord_x, coord_y, max_iterations, gradient_error, function_error))
					
if os.getenv("REQUEST_METHOD") == "POST":
	if coord_x != "" and coord_y != "" and max_iterations != "" and gradient_error != "" and function_error != "":
		coord_x = float(coord_x)
		coord_y = float(coord_y)
		max_iterations = int(max_iterations)
		gradient_error = float(gradient_error)
		function_error = float(function_error)
		p = [coord_x, coord_y, max_iterations, gradient_error, function_error]
		point, graphic = main_function_optimize(1, "Optimization", p, [[-4, 4], [-4, 4]])
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
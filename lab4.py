#!c:\Users\я\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
from main_function_optimize import main_function_optimize

form = cgi.FieldStorage()
num_iterations = form.getfirst("num_iterations", "")
swarm_size = form.getfirst("swarm_size", "")
opt_function = form.getfirst("opt_function", "")

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html>
    <head>
        <!-- <meta charset="utf-8"> -->
        <title>Роевый алгоритм</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
		<center>
			<header>
				<ol>
					<li><a href="/">Лабораторные работы</a></li>
				</ol>
				<h1>Роевый алгоритм</h1>
			</header>
			<section>
				<form action="/lab4.py" method="POST" name="lab4-form">
					<label>Количество итераций</label>
					<input required="" type="number" placeholder="Количество итераций" value="%s" name="num_iterations">
					<hr>
					<label>Размер роя</label>
					<input required="" type="number" placeholder="Размер роя" value="%s" name="swarm_size">
					<hr>
					<label>Оптимизируемая функция</label>
					<select name="opt_function">
						<option disabled>Оптимизируемая функция</option>""" % (num_iterations, swarm_size))
						
if (opt_function == "0"):
	print("""<option value="0" selected>Функция Растригина</option>""")
else:
	print("""<option value="0">Функция Растригина</option>""")
	
if (opt_function == "1"):
	print("""<option value="1" selected>Функция Швефеля</option>""")
else:
	print("""<option value="1">Функция Швефеля</option>""")
	
if (opt_function == "2"):
	print("""<option value="2" selected>Функция сферы</option>""")
else:
	print("""<option value="2">Функция сферы</option>""")
	
print("""</select>
					<hr><input type="submit" value="НАЧАТЬ">
				</form>""")
					
if os.getenv("REQUEST_METHOD") == "POST":
	if num_iterations != "" and swarm_size != "" and opt_function != "":
		num_iterations = int(num_iterations)
		swarm_size = int(swarm_size)
		opt_function = int(opt_function)
		p = [num_iterations, swarm_size, opt_function]
		point, graphic = main_function_optimize(4, "Optimization", p, [[-4, 4], [-4, 4]])
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
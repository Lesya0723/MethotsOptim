#!c:\Users\я\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
from main_function_optimize import main_function_optimize

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html>
    <head>
        <!-- <meta charset="utf-8"> -->
        <title>Симплекс-метод</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
		<center>
			<header>
				<ol>
					<li><a href="/">Лабораторные работы</a></li>
				</ol>
				<h1>Симплекс-метод</h1>
			</header>
			<section>
				<form action="/lab2.py" method="POST" name="lab2-form">
					<p>f(x) = 2x<sub>1</sub><sup>2</sup> + 2x<sub>1</sub>x<sub>2</sub> + 2x<sub>2</sub><sup>2</sup> - 4x<sub>1</sub> - 6x<sub>2</sub></p>
					<hr>
					<input type="submit" value="НАЧАТЬ">
				</form>""")
					
if os.getenv("REQUEST_METHOD") == "POST":
	point, graphic = main_function_optimize(2, "Optimization", [], [[-4, 4], [-4, 4]])
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
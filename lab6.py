#!c:\Users\я\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
from main_function_optimize import main_function_optimize

form = cgi.FieldStorage()
minx = form.getfirst("minx", "")
maxx = form.getfirst("maxx", "")
miny = form.getfirst("miny", "")
maxy = form.getfirst("maxy", "")
sb = form.getfirst("sb", "")
sg = form.getfirst("sg", "")
nb = form.getfirst("nb", "")
nd = form.getfirst("nd", "")
num_clons = form.getfirst("num_clons", "")
mutate_coeff = form.getfirst("mutate_coeff", "")
num_iterations = form.getfirst("num_iterations", "")
death_coeff = form.getfirst("death_coeff", "")
clone_compress = form.getfirst("clone_compress", "")

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html>
    <head>
        <!-- <meta charset="utf-8"> -->
        <title>Алгоритм имунной сети</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
		<center>
			<header>
				<ol>
					<li><a href="/">Лабораторные работы</a></li>
				</ol>
				<h1>Алгоритм имунной сети</h1>
			</header>
			<section>
				<form action="/lab6.py" method="POST" name="lab6-form">
					<label>Минимальные и максимальное значения координат</label>
					<input required="" type="text" placeholder="Минимальное значение х" value="%s" name="minx">
					<input required="" type="text" placeholder="Максимальное значение х" value="%s" name="maxx">
					<input required="" type="text" placeholder="Минимальное значение у" value="%s" name="miny">
					<input required="" type="text" placeholder="Максимальное значение у" value="%s" name="maxy">
					<hr>
					<label>Размер начальной популяции антител</label>
					<input required="" type="number" placeholder="Размер начальной популяции антител" value="%s" name="sb">
					<hr>
					<label>Размер начальной популяции антигенов</label>
					<input required="" type="number" placeholder="Размер начальной популяции антигенов" value="%s" name="sg">
					<hr>
					<label>Число антител для мутации</label>
					<input required="" type="number" placeholder="Число антител для мутации" value="%s" name="nb">
					<hr>
					<label>Число оставляемых клонов</label>
					<input required="" type="number" placeholder="Число оставляемых клонов" value="%s" name="nd">
					<hr>
					<label>Число клонов клонируемого антитела</label>
					<input required="" type="number" placeholder="Число клонов клонируемого антитела" value="%s" name="num_clons">
					<hr>
					<label>Коэффициент мутации</label>
					<input required="" type="text" placeholder="Коэффициент мутации" value="%s" name="mutate_coeff">
					<hr>
					<label>Количество итераций</label>
					<input required="" type="number" placeholder="Количество итераций" value="%s" name="num_iterations">
					<hr>
					<label>Пороговый коэффициент гибели</label>
					<input required="" type="text" placeholder="Пороговый коэффициент гибели" value="%s" name="death_coeff">
					<hr>
					<label>Коэффициент клонального сжатия</label>
					<input required="" type="text" placeholder="Коэффициент клонального сжатия" value="%s" name="clone_compress">
					<hr><input type="submit" value="НАЧАТЬ">
				</form>""" % (minx, maxx, miny, maxy, sb, sg, nb, nd, num_clons, mutate_coeff, num_iterations, death_coeff, clone_compress))
					
if os.getenv("REQUEST_METHOD") == "POST":
	if minx != "" and maxx != "" and miny != "" and maxy != "" and sb != "" and sg != "" and nb != "" and nd != "" and num_clons != "" and mutate_coeff != "" and num_iterations != "" and death_coeff != "" and clone_compress != "":
		minx = float(minx)
		maxx = float(maxx)
		miny = float(miny)
		maxy = float(maxy)
		sb = int(sb)
		sg = int(sg)
		nb = int(nb)
		nd = int(nd)
		num_clons = int(num_clons)
		mutate_coeff = float(num_clons)
		num_iterations = int(num_iterations)
		death_coeff = float(death_coeff)
		clone_compress = float(clone_compress)
		p = [minx, maxx, miny, maxy, sb, sg, nb, nd, num_clons, mutate_coeff, num_iterations, death_coeff, clone_compress]
		point, graphic = main_function_optimize(6, "Optimization", p, [[-2, 2], [-2, 2]])
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
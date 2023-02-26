#!c:\Users\я\AppData\Local\Programs\Python\Python37-32\python.exe
import os
import cgi
from main_function_optimize import main_function_optimize

form = cgi.FieldStorage()
opt_func = form.getfirst("opt_func", "")
num_scouts = form.getfirst("num_scouts", "")
best_bees = form.getfirst("best_bees", "")
good_bees = form.getfirst("good_bees", "")
good_regions = form.getfirst("good_regions", "")
best_regions = form.getfirst("best_regions", "")
num_runs = form.getfirst("num_runs", "")
max_iterations = form.getfirst("max_iterations", "")
static_iter = form.getfirst("static_iter", "")

print("Content-Type: text/html\n")
print("""<!DOCTYPE html>
<html>
    <head>
        <!-- <meta charset="utf-8"> -->
        <title>Пчелиный алгоритм</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
		<center>
			<header>
				<ol>
					<li><a href="/">Лабораторные работы</a></li>
				</ol>
				<h1>Пчелиный алгоритм</h1>
			</header>
			<section>
				<form action="/lab5.py" method="POST" name="lab5-form">
					<label>Оптимизируемая функция</label>
					<select name="opt_func">
						<option disabled>Оптимизируемая функция</option>""")
						
if (opt_func == "0"):
	print("""<option value="0" selected>Сферическая</option>""")
else:
	print("""<option value="0">Сферичрская</option>""")
	
if (opt_func == "2"):
	print("""<option value="2" selected>Голдштейна</option>""")
else:
	print("""<option value="2">Голдштейна</option>""")
	
if (opt_func == "3"):
	print("""<option value="3" selected>Розенброка</option>""")
else:
	print("""<option value="3">Розенброка</option>""")
	
print("""</select>
					<hr>
					<label>Количество пчёл-разведчиков</label>
					<input required="" type="number" placeholder="Количество пчёл-разведчиков" value="%s" name="num_scouts">
					<hr>
					<label>Количество пчел, отправляемые на лучшие участки</label>
					<input required="" type="number" placeholder="Количество пчел, отправляемых на лучшие участки" value="%s" name="best_bees">
					<hr>
					<label>Количество пчел, отправляемых на выбранные, но не лучшие участки</label>
					<input required="" type="number" placeholder="Количество пчел, отправляемых на выбранные, но не лучшие участки" value="%s" name="good_bees">
					<hr>
					<label>Количество выбранных, но не лучших, участков</label>
					<input required="" type="number" placeholder="Количество выбранных, но не лучших участков" value="%s" name="good_regions">
					<hr>
					<label>Количество лучших участков</label>
					<input required="" type="number" placeholder="Количество лучших участков" value="%s" name="best_regions">
					<hr>
					<label>Количество запусков алгоритма</label>
					<input required="" type="number" placeholder="Количество запусков алгоритма" value="%s" name="num_runs">
					<hr>
					<label>Максимальное количество итераций</label>
					<input required="" type="number" placeholder="Максимальное количество итераций" value="%s" name="max_iterations">
					<hr>
					<label>Через такое количество итераций без нахождения лучшего решения уменьшим область поиска</label>
					<input required="" type="number" placeholder="Через такое количество итераций без нахождения лучшего решения уменьшим область поиска" value="%s" name="static_iter">
					<hr><input type="submit" value="НАЧАТЬ">
				</form>""" % (num_scouts, best_bees, good_bees, good_regions, best_regions, num_runs, max_iterations, static_iter))
					
if os.getenv("REQUEST_METHOD") == "POST":
	if opt_func != "" and num_scouts != "" and best_bees != "" and good_bees != "" and good_regions != "" and best_regions != "" and num_runs != "" and max_iterations != "" and static_iter != "":
		opt_func = int(opt_func)
		num_scouts = int(num_scouts)
		best_bees = int(best_bees)
		good_bees = int(good_bees)
		good_regions = int(good_regions)
		best_regions = int(best_regions)
		num_runs = int(num_runs)
		max_iterations = int(max_iterations)
		static_iter = int(static_iter)
		p = [opt_func, num_scouts, best_bees, good_bees, good_regions, best_regions, num_runs, max_iterations, static_iter]
		point, graphic = main_function_optimize(5, "Optimization", p, [[-4, 4], [-4, 4]])
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
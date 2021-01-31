
N = 40
G = 100

res = []

res.append("unset label")
res.append("set label 'Hypervolume' at graph 0.5, 0.95 center")
res.append("unset key")

number = 1

line_1 = "plot './tmp_zdt3p{}g{}/hypervol1.out' using 1:2 w l,\\".format(N, G)
res.append(line_1)

for number in range(2, 20):
    new_line = "'./tmp_zdt3p{}g{}/hypervol{}.out' using 1:2 w l,\\".format(N, G, number)
    res.append(new_line)

last_line = "'./tmp_zdt3p{}g{}/hypervol20.out' using 1:2 w l".format(N, G)
res.append(last_line)

for element in res:
    print(element)

with open('plot_zdt3p{}g{}'.format(N, G), 'w') as f:
    for item in res:
        f.write(item + '\n')


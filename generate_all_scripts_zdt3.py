import generate_stall_script


# Params
N = 200
G = 50
n_eval = N*G

# Generate stall_script
generate_stall_script.generate_stall(N, G)

# Do not modify
hvref_number = 1
seed_number = 1
res = []

# Add DE commands
# First lines (seed 1)
line_1 = 'cp ./zdt3_de_results/{}/P{}G{}/zdt3_all_popmp{}g{}_seed{}.out zdt3_all_popmp{}g{}.out'.format(n_eval, N, G, N, G, seed_number, N, G)
res.append(line_1)

line_2 = './metrics < zdt3p{}g{}stall.in'.format(N, G)
res.append(line_2)

line_3 = 'cp hvref.out ./tmp_zdt3p{}g{}/hvref{}.out'.format(N, G, hvref_number)
res.append(line_3)

line_4 = 'cp ./tmp_zdt3p{}g{}/hvref{}.out ./tmp_zdt3p{}g{}/hvrefp{}g{}.out'.format(N, G, hvref_number, N, G, N, G)
res.append(line_4)

while seed_number < 10:
    seed_number = seed_number + 1
    hvref_number = hvref_number + 1

    line_1 = 'cp ./zdt3_de_results/{}/P{}G{}/zdt3_all_popmp{}g{}_seed{}.out zdt3_all_popmp{}g{}.out'.format(n_eval, N, G, N, G, seed_number, N, G)
    res.append(line_1)

    line_2 = './metrics < zdt3p{}g{}stall.in'.format(N, G)
    res.append(line_2)

    line_3 = 'cp hvref.out ./tmp_zdt3p{}g{}/hvref{}.out'.format(N, G, hvref_number)
    res.append(line_3)

    line_4 = 'cat ./tmp_zdt3p{}g{}/hvref{}.out >> ./tmp_zdt3p{}g{}/hvrefp{}g{}.out'.format(N, G, hvref_number, N, G, N, G)
    res.append(line_4)



# TODO: Comprobar hvref_number
# TODO: seed 099

# Add NSGAII commands
seed_number = 0
while seed_number < 10:
    seed_number = seed_number + 1
    hvref_number = hvref_number + 1

    if seed_number == 10:
        seed_number = 99

    line_1 = 'cp ./zdt3_nsgaii_results/{}/P{}G{}/zdt3_all_popmp{}g{}_seed0{}.out zdt3_all_popmp{}g{}.out'.format(n_eval, N, G, N, G, seed_number, N, G)
    res.append(line_1)

    line_2 = './metrics < zdt3p{}g{}stall.in'.format(N, G)
    res.append(line_2)

    line_3 = 'cp hvref.out ./tmp_zdt3p{}g{}/hvref{}.out'.format(N, G, hvref_number)
    res.append(line_3)

    line_4 = 'cat ./tmp_zdt3p{}g{}/hvref{}.out >> ./tmp_zdt3p{}g{}/hvrefp{}g{}.out'.format(N, G, hvref_number, N, G, N, G)
    res.append(line_4)


for element in res:
    print(element)

with open('zdt3p{}g{}allscript'.format(N, G), 'w') as f:
    for item in res:
        f.write(item + '\n')




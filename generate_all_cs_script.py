import generate_stall_script

# Params
N = 100
G = 40
n_eval = N*G

# Generate .in file
generate_stall_script.generate_stall_allcs_basic(N, G)

seed_number = 0
res = []

while seed_number < 10:
    seed_number = seed_number + 1

    line_1 = 'cp ./zdt3_de_results/{}/P{}G{}/zdt3_all_popmp{}g{}_seed{}.out zdt3_all_popmp{}g{}_de.out'.format(n_eval, N, G, N, G, seed_number, N, G)
    res.append(line_1)

    if seed_number == 10:
        seed_number = 99

    line_2 = 'cp ./zdt3_nsgaii_results/{}/P{}G{}/zdt3_all_popmp{}g{}_seed0{}.out zdt3_all_popmp{}g{}_nsgaii.out'.format(n_eval, N, G, N, G, seed_number, N, G)
    res.append(line_2)

    line_3 = './metrics < zdt3p{}g{}stallCS.in'.format(N, G)
    res.append(line_3)

    line_4 = 'cp cs.out ./tmp_zdt3p{}g{}/cs1_{}.out'.format(N, G, seed_number)
    res.append(line_4)

    line_5 = 'cp cs2.out ./tmp_zdt3p{}g{}/cs2_{}.out'.format(N, G, seed_number)
    res.append(line_5)


for element in res:
    print(element)

with open('zdt3p{}g{}allCSscript'.format(N, G), 'w') as f:
    for item in res:
        f.write(item + '\n')
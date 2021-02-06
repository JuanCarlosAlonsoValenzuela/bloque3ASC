import generate_stall_script


# Params
N = 100
G = 40
d = 16
n_eval = N*G

# Generate .in file
generate_stall_script.generate_stall_allcs_basic(N, G, d)

seed_number = 0
res = []

while seed_number < 10:
    seed_number = seed_number + 1

    line_1 = 'cp ./cf6_{}d_de_results/{}/P{}G{}/cf6_{}d_all_popmp{}g{}_seed{}.out cf6_{}d_all_popmp{}g{}_de.out'\
        .format(d, n_eval, N, G, d, N, G, seed_number, d, N, G)
    res.append(line_1)

    if seed_number == 10:
        seed_number = 99

    line_2 = 'cp ./cf6_{}d_results/{}/P{}G{}/cf6_{}d_all_popmp{}g{}_seed0{}.out cf6_{}d_all_popmp{}g{}_nsgaii.out'\
        .format(d, n_eval, N, G, d, N, G, seed_number, d, N, G)
    res.append(line_2)

    line_3 = './metrics < cf6_{}dp{}g{}stallCS.in'.format(d, N, G)
    res.append(line_3)

    line_4 = 'cp cs.out ./tmp_cf6_{}dp{}g{}/cs1_{}.out'.format(d, N, G, seed_number)
    res.append(line_4)

    line_5 = 'cp cs2.out ./tmp_cf6_{}dp{}g{}/cs2_{}.out'.format(d, N, G, seed_number)
    res.append(line_5)


for element in res:
    print(element)

with open('cf6_{}d_p{}g{}allCSscript'.format(d, N, G), 'w') as f:
    for item in res:
        f.write(item + '\n')
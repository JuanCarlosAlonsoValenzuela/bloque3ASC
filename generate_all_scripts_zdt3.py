import generate_stall_script


# Params
N = 100
G = 40
d = 16
n_eval = N*G

# Generate stall_script
generate_stall_script.generate_stall(N, G, d)

# Do not modify
hvref_number = 1
seed_number = 1
res = []

# Add DE commands
# First lines (seed 1)
line_1 = 'cp ./cf6_{}d_de_results/{}/P{}G{}/cf6_{}d_all_popmp{}g{}_seed{}.out cf6_{}d_all_popmp{}g{}.out'\
    .format(d, n_eval, N, G, d, N, G, seed_number, d, N, G)
res.append(line_1)

line_2 = './metrics < cf6_{}d_p{}g{}stall.in'.format(d, N, G)
res.append(line_2)

line_3 = 'cp hvref.out ./tmp_cf6_{}dp{}g{}/hvref{}.out'.format(d, N, G, hvref_number)
res.append(line_3)

line_4 = 'cp ./tmp_cf6_{}dp{}g{}/hvref{}.out ./tmp_cf6_{}dp{}g{}/hvrefp{}g{}.out'\
    .format(d, N, G, hvref_number, d, N, G, N, G)
res.append(line_4)

while seed_number < 10:
    seed_number = seed_number + 1
    hvref_number = hvref_number + 1

    line_1 = 'cp ./cf6_{}d_de_results/{}/P{}G{}/cf6_{}d_all_popmp{}g{}_seed{}.out cf6_{}d_all_popmp{}g{}.out'\
        .format(d, n_eval, N, G, d, N, G, seed_number, d, N, G)
    res.append(line_1)

    line_2 = './metrics < cf6_{}d_p{}g{}stall.in'.format(d, N, G)
    res.append(line_2)

    line_3 = 'cp hvref.out ./tmp_cf6_{}dp{}g{}/hvref{}.out'.format(d, N, G, hvref_number)
    res.append(line_3)

    line_4 = 'cat ./tmp_cf6_{}dp{}g{}/hvref{}.out >> ./tmp_cf6_{}dp{}g{}/hvrefp{}g{}.out'\
        .format(d, N, G, hvref_number, d, N, G, N, G)
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

    line_1 = 'cp ./cf6_{}d_results/{}/P{}G{}/cf6_{}d_all_popmp{}g{}_seed0{}.out cf6_{}d_all_popmp{}g{}.out'\
        .format(d, n_eval, N, G, d, N, G, seed_number, d, N, G)
    res.append(line_1)

    line_2 = './metrics < cf6_{}d_p{}g{}stall.in'.format(d, N, G)
    res.append(line_2)

    line_3 = 'cp hvref.out ./tmp_cf6_{}dp{}g{}/hvref{}.out'.format(d, N, G, hvref_number)
    res.append(line_3)

    line_4 = 'cat ./tmp_cf6_{}dp{}g{}/hvref{}.out >> ./tmp_cf6_{}dp{}g{}/hvrefp{}g{}.out'\
        .format(d, N, G, hvref_number, d, N, G, N, G)
    res.append(line_4)


for element in res:
    print(element)

with open('cf6_{}d_p{}g{}allscript'.format(d, N, G), 'w') as f:
    for item in res:
        f.write(item + '\n')




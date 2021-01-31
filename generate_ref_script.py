import generate_stall_script


# Params
N = 40
G = 100
n_eval = N*G

# Generate basic stall script
generate_stall_script.generate_stall_basic(N, G)

# Do not modify
seed_number = 0
spacing_number = 0
hypervol_number = 0
res = []

# Add DE commands
while seed_number < 10:
    seed_number = seed_number + 1
    spacing_number = spacing_number + 1
    hypervol_number = hypervol_number + 1

    line_1 = 'cp ./zdt3_de_results/{}/P{}G{}/zdt3_all_popmp{}g{}_seed{}.out zdt3_all_popmp{}g{}.out'.format(n_eval, N, G, N, G, seed_number, N, G)
    res.append(line_1)

    line_2 = 'cp zdt3p{}g{}stallbasic.in zdt3p{}g{}stallref.in'.format(N, G, N, G)
    res.append(line_2)

    # TODO: Modify HVREF NAME
    line_3 = 'cat ./tmp_zdt3p{}g{}/hvref.out >> zdt3p{}g{}stallref.in'.format(N, G, N, G)
    res.append(line_3)

    line_4 = './metrics < zdt3p{}g{}stallref.in'.format(N, G)
    res.append(line_4)

    line_5 = 'cp hypervol.out ./tmp_zdt3p{}g{}/hypervol{}.out'.format(N, G, hypervol_number)
    res.append(line_5)

    line_6 = 'cp spacing.out ./tmp_zdt3p{}g{}/spacing{}.out'.format(N, G, spacing_number)
    res.append(line_6)


# NSGA II
seed_number = 0
while seed_number<10:
    seed_number = seed_number + 1
    spacing_number = spacing_number + 1
    hypervol_number = hypervol_number + 1

    if seed_number == 10:
        seed_number = 99

    # TODO: 0 before seed
    line_1 = 'cp ./zdt3_nsgaii_results/{}/P{}G{}/zdt3_all_popmp{}g{}_seed0{}.out zdt3_all_popmp{}g{}.out'.format(n_eval, N, G, N, G, seed_number, N, G)
    res.append(line_1)

    line_2 = 'cp zdt3p{}g{}stallbasic.in zdt3p{}g{}stallref.in'.format(N, G, N, G)
    res.append(line_2)

    line_3 = 'cat ./tmp_zdt3p{}g{}/hvref.out >> zdt3p{}g{}stallref.in'.format(N, G, N, G)
    res.append(line_3)

    line_4 = './metrics < zdt3p{}g{}stallref.in'.format(N, G)
    res.append(line_4)

    line_5 = 'cp hypervol.out ./tmp_zdt3p{}g{}/hypervol{}.out'.format(N, G, hypervol_number)
    res.append(line_5)

    line_6 = 'cp spacing.out ./tmp_zdt3p{}g{}/spacing{}.out'.format(N, G, spacing_number)
    res.append(line_6)


for element in res:
    print(element)

with open('zdt3p{}g{}allrefscript'.format(N, G), 'w') as f:
    for item in res:
        f.write(item + '\n')
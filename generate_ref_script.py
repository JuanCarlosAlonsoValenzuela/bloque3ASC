import generate_stall_script


# Params
N = 200
G = 50
d = 16
n_eval = N*G

# Generate basic stall script
generate_stall_script.generate_stall_basic(N, G, d)

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

    line_1 = 'cp ./cf6_{}d_de_results/{}/P{}G{}/cf6_{}d_all_popmp{}g{}_seed{}.out cf6_{}d_all_popmp{}g{}.out'\
        .format(d, n_eval, N, G, d, N, G, seed_number, d, N, G)
    res.append(line_1)

    line_2 = 'cp cf6_{}d_p{}g{}stallbasic.in cf6_{}d_p{}g{}stallref.in'\
        .format(d, N, G, d, N, G)
    res.append(line_2)

    line_3 = 'cat ./tmp_cf6_{}dp{}g{}/hvref.out >> cf6_{}d_p{}g{}stallref.in'\
        .format(d, N, G, d, N, G)
    res.append(line_3)

    line_4 = './metrics < cf6_{}d_p{}g{}stallref.in'.format(d, N, G)
    res.append(line_4)

    line_5 = 'cp hypervol.out ./tmp_cf6_{}dp{}g{}/hypervol{}.out'.format(d, N, G, hypervol_number)
    res.append(line_5)

    line_6 = 'cp spacing.out ./tmp_cf6_{}dp{}g{}/spacing{}.out'.format(d, N, G, spacing_number)
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
    line_1 = 'cp ./cf6_{}d_results/{}/P{}G{}/cf6_{}d_all_popmp{}g{}_seed0{}.out cf6_{}d_all_popmp{}g{}.out'\
        .format(d, n_eval, N, G, d, N, G, seed_number, d, N, G)
    res.append(line_1)

    line_2 = 'cp cf6_{}d_p{}g{}stallbasic.in cf6_{}d_p{}g{}stallref.in'.format(d, N, G,d, N, G)
    res.append(line_2)

    line_3 = 'cat ./tmp_cf6_{}dp{}g{}/hvref.out >> cf6_{}d_p{}g{}stallref.in'.format(d, N, G, d, N, G)
    res.append(line_3)

    line_4 = './metrics < cf6_{}d_p{}g{}stallref.in'.format(d, N, G)
    res.append(line_4)

    line_5 = 'cp hypervol.out ./tmp_cf6_{}dp{}g{}/hypervol{}.out'.format(d, N, G, hypervol_number)
    res.append(line_5)

    line_6 = 'cp spacing.out ./tmp_cf6_{}dp{}g{}/spacing{}.out'.format(d, N, G, spacing_number)
    res.append(line_6)


for element in res:
    print(element)

with open('cf6_{}dp{}g{}allrefscript'.format(d, N, G), 'w') as f:
    for item in res:
        f.write(item + '\n')
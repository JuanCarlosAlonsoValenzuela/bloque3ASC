def generate_stall(N, G, d):
    res = []
    res.append('1')
    res.append('1')
    res.append('2')

    file_name = 'cf6_{}d_all_popmp{}g{}.out'.format(d, N, G)
    res.append(file_name)

    res.append(str(N))
    res.append(str(G))
    res.append('1')

    for element in res:
        print(element)

    with open('cf6_{}d_p{}g{}stall.in'.format(d, N, G), 'w') as f:
        for item in res:
            f.write(item + '\n')


def generate_stall_basic(N, G, d):
    res = []
    res.append('1')
    res.append('1')
    res.append('2')

    file_name = 'cf6_{}d_all_popmp{}g{}.out'.format(d, N, G)
    res.append(file_name)

    res.append(str(N))
    res.append(str(G))
    res.append('0')

    for element in res:
        print(element)

    with open('cf6_{}d_p{}g{}stallbasic.in'.format(d, N, G), 'w') as f:
        for item in res:
            f.write(item + '\n')


def generate_stall_allcs_basic(N, G, d):
    res = []
    res.append('2')
    res.append('1')
    res.append('2')

    file_name = 'cf6_{}d_all_popmp{}g{}_de.out'.format(d, N, G)
    res.append(file_name)

    res.append(str(N))
    res.append(str(G))

    file_name = 'cf6_{}d_all_popmp{}g{}_nsgaii.out'.format(d, N, G)
    res.append(file_name)

    res.append(str(N))
    res.append(str(G))

    res.append('1')

    for element in res:
        print(element)

    with open('cf6_{}dp{}g{}stallCS.in'.format(d, N, G), 'w') as f:
        for item in res:
            f.write(item + '\n')
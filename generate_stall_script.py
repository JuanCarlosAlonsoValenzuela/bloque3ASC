def generate_stall(N, G):
    res = []
    res.append('1')
    res.append('1')
    res.append('2')

    file_name = 'zdt3_all_popmp{}g{}.out'.format(N, G)
    res.append(file_name)

    res.append(str(N))
    res.append(str(G))
    res.append('1')

    for element in res:
        print(element)

    with open('zdt3p{}g{}stall.in'.format(N, G), 'w') as f:
        for item in res:
            f.write(item + '\n')


def generate_stall_basic(N, G):
    res = []
    res.append('1')
    res.append('1')
    res.append('2')

    file_name = 'zdt3_all_popmp{}g{}.out'.format(N, G)
    res.append(file_name)

    res.append(str(N))
    res.append(str(G))
    res.append('0')

    for element in res:
        print(element)

    with open('zdt3p{}g{}stallbasic.in'.format(N, G), 'w') as f:
        for item in res:
            f.write(item + '\n')


def generate_stall_allcs_basic(N, G):
    res = []
    res.append('2')
    res.append('1')
    res.append('2')

    file_name = 'zdt3_all_popmp{}g{}_de.out'.format(N, G)
    res.append(file_name)

    res.append(str(N))
    res.append(str(G))

    file_name = 'zdt3_all_popmp{}g{}_nsgaii.out'.format(N, G)
    res.append(file_name)

    res.append(str(N))
    res.append(str(G))

    res.append('1')

    for element in res:
        print(element)

    with open('zdt3p{}g{}stallCS.in'.format(N, G), 'w') as f:
        for item in res:
            f.write(item + '\n')
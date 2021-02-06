import pandas as pd


def min_or_zero(x, y):
    z = min(x, y)
    if z <= 0.0:
        return z
    else:
        return 0.0


N = 200
G = 50
d = 16

n_eval = N*G
for seed_number in range(1, 11):
    path = 'cf6_{}d_de_results/{}/P{}G{}/cf6_{}d_all_popmp{}g{}_seed{}.out'\
        .format(d, n_eval, N, G, d, N, G, seed_number)

    df = pd.read_csv(path, header=None, sep='\t')

    df[4] = df.apply(lambda row: min_or_zero(row[2], row[3]), axis=1)

    df = df.drop([2, 3], axis=1)

    print(df.head())

    df.to_csv(path, sep='\t', header=False, index=False)

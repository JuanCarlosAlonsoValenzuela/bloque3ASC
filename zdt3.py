import math


# generate x
def zdt3(x, n):
    out = [0.0, 0.0]
    out[0] = x[0]

    tmp = 0.0
    for i in range(1, n):
        tmp = tmp + x[i]

    # print(tmp)

    g = 1.0 + ((9.0*tmp)/(n-1.0))
    h = 1.0 - math.sqrt(out[0]/g) - (out[0]/g) * math.sin(10*math.pi*out[0])
    f_2 = g*h

    out[1] = f_2

    return out
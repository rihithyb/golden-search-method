import math

def f(x):
    return - (x - 2)**2 + 4

def neg_f(x):
    return -f(x)

def golden_section_search(f, a, b, tol=1e-5):
    gr = (math.sqrt(5) + 1) / 2
    c = b - (b - a) / gr
    d = a + (b - a) / gr

    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c

        c = b - (b - a) / gr
        d = a + (b - a) / gr

    x_opt = (a + b) / 2
    return x_opt, -f(x_opt)

xmax, fmax = golden_section_search(neg_f, 0, 5)
print(f"Maximum at x = {xmax:.5f}, f(x) = {fmax:.5f}")

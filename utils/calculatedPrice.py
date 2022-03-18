import math

def setPriceSucTotal(l):
    val = l.getPIC()
    suc = l.getSUC()
    if 0 < val <= 200:
        l.setSUCtotal(suc + 2 * suc)
    elif 200 < val <= 800:
        total = 8 * suc
        l.setSUCtotal(total - 0.1 * total)
    elif 800 < val <= 1600:
        total = 16 * suc
        l.setSUCtotal(total - 0.15 * total)
    else:
        k = round(math.log2(val / 1600))
        total = 32 * suc
        sucTotal = math.pow(2, k) * (total - 0.25 * total)
        l.setSUCtotal(sucTotal)


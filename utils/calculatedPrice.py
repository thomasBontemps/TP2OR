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
<<<<<<< HEAD
        k = round(math.log2(val / 1600))
=======
        k = math.log2(val / 1600)
>>>>>>> 8d3bf9e2e7803c1c869eac91683c959b4ee4cea0
        total = 32 * suc
        sucTotal = math.pow(2, k) * (total - 0.25 * total)
        l.setSUCtotal(sucTotal)


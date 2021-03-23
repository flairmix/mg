
pi = 3.14159265359


def GCalh_to_kW(power_Gcal_h):
    return power_Gcal_h * 1163


def kW_to_GCalh(power_kW):
    return power_kW / 1163


def pipeG(Q, t1=130, t2=70):
    """
    return consuption for pipe in t/h
    Q - Gcal/h - power,
    t1 - high temperature, 
    t2 - low temperature
    """
    G = int(1000* Q / (t1 - t2))
    return G


def pipeDn(G, v = 1):
    """
    return dn for pipe
    G - t/h - consuption,
    v = 1 m/s - velocity of water  
    """
    DN = (20, 25, 32, 40, 50, 65, 80, 100, 125, 150, 200, 250, 300)
    dn = int(1000 * (G / 2826 / v) ** 0.5)
    i = 0
    while dn > DN[i]:
        i += 1 
    return DN[i]


def pipev(G, dn):
    """
    return velosity for dn pipe
    G - t/h 
    dn - mm
    """
    v = 10**6 *(G / (dn**2) / 2826)
    return v


def kv(Gmax, dpMin):
    kv = Gmax / (dpMin ** 0.5)
    return kv


def dp(Gmax, kvs):
    """
    return dp for Gmax consumption with kvs
    G - t/h 
    """
    return (Gmax / kvs)
    

if __name__ == '__main__':
    
    G = pipeG(3.217, 90, 70)
    print("G - m3/h - ", G)

    Dn = pipeDn(2.15)
    print("Dn - ", Dn)

    V = pipev(G, 200)
    print("V m/s - ", V)
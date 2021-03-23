
from enum import Enum


pi = 3.14159265359


# def Power_convert(power, unit_in, unit_out):
#     """ 
#     unit_in  - Gcal_h | kW
#     unit_out - Gcal_h | kW
#     """

#     if unit_in == "Gcal_h" and unit_out == "kW":
#         return power * 1163
#     elif unit_in == "kW" and unit_out == "Gcal_h":
#         return power / 1163
#     else:
#         raise ValueError("Wrong units for converting")
   
   
            


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
    return (1000 * Q / (t1 - t2))


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
    
    # ait 21
    G1 = pipeG((1296 / 1163), 90, 70)
    Dn1 = pipeDn(G1, 1.3)
    print("G_1184 - m3/h - ", G1, " , Dn1 - ", Dn1)

    G2 = pipeG((849 / 1163), 90, 70)
    Dn2 = pipeDn(G2, 1)
    print("G_849 - m3/h - ", G2, " , Dn2 - ", Dn2)

    G12 = pipeG(2.175, 90, 70)
    Dn12 = pipeDn(G12, 1.3)
    v12 = pipev(G12, Dn12)
    print("G12 - m3/h - ", G12, " , Dn12 - ", Dn12)
    print("v - m/s - ", v12)


    # Dn = pipeDn(2.15)
    # print("Dn - ", Dn)

    # V = pipev(155, 200)
    # print("V m/s - ", V)

    # print(Power_convert(1.000, "Gcal_h", "kW"))
    # print(Power_convert(1000, "kW", "Gcal_h"))
    # print(Power_convert(1.000, "kW", "kW"))




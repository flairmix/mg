import source_data

#л на кВт
# coef_v = 7
# V_system = source_data.POWER_sum_23
 * 1.163 * coef_v 
V_system = 0.942 + 0.97 + 0.97 + 0.109 + 0.778

#подпитка 
G_refill_h = 0.0025 * V_system
G_refill_day = G_refill_h * 24

#заполение
fill_hours = 4
G_fill_h = V_system / fill_hours

#пожаротушение 
#хоз - быт нужды 

#раковина m/h 
G_rak = 0.08
hours_rak = 1 
#унитаз 
G_uni = 0.083
hours_uni = 1 

G_hoz_byt = G_rak * hours_rak + G_uni * hours_uni

if __name__ == "__main__":
    
    print("V_system, m3/h - ", round(V_system, 3))
    print("G_fill_h , m3/h - ", round(G_fill_h, 3))
    print("G_refill_day , m3/day - ", round(G_refill_day, 3))
    print("G_refill_h , m3/h - ", round(G_refill_h, 3))
    print("G_hoz_byt , m3/day - ", round(G_hoz_byt, 3))
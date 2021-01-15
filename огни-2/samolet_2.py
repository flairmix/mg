
import calc
import equipment


#Gcal / h
heat_power = 5.77
vent_power = 0.244
hot_water_power = 1.152
temp_t3 = 65
temp_w1_winter = 5
temp_w1_summer = 15

POWER = heat_power + vent_power + hot_water_power

#расчетный режим
#котловой контур
temp_T1_inside = 130
temp_T2_inside = 80
#сетевой контур
temp_T1_outside = 130
temp_T2_outside = 70

#летний режим
#котловой контур
temp_T1_summer_in = 70
temp_T2_summer_in = 60
#сетевой контур
temp_T1_summer_out = 70
temp_T2_summer_out = 40


print("heat_power, Gcal / h - ", heat_power)
print("vent_power, Gcal / h - ", vent_power)
print("hot_water_power, Gcal / h - ", hot_water_power)
print("POWER, Gcal / h - ", round(POWER, 3))
print("temp_T1_inside - ", temp_T1_inside, ", temp_T2_inside - ", temp_T2_inside)
print("temp_T1_outside - ", temp_T1_outside, ", temp_T2_outside - ", temp_T2_outside)

print("---------------------------------------------")
# G_main_inside = round(1000 * POWER / (temp_T1_inside - temp_T2_inside), 3)
# print("расход расчетный котловой контур, т/ч - ", G_main_inside)
# dn_t1_inside = calc.pipeDn(G_main_inside, 1.3)
# print("диаметр Т1 / Т2 котловой контур- ", dn_t1_inside)
# print("скорость Т1 / Т2, м/с - ", round(calc.pipev(G_main_inside, dn_t1_inside), 3))
print("---------------------------------------------")

G_main_outside = round(1000 * POWER / (temp_T1_outside - temp_T2_outside), 3)
print("расход расчетный сетевой контур, т/ч - ", G_main_outside)
dn_t1_outside = calc.pipeDn(G_main_outside, 1.2)
print("диаметр Т1 / Т2 сетевой контур- ", dn_t1_outside)
print("скорость Т1 / Т2, м/с - ", round(calc.pipev(G_main_outside, dn_t1_outside), 3))
print("---------------------------------------------")

#Gcal / h
Q_boiler_0 = 3.009
Q_boiler_1 = 3.009
Q_boiler_2 = 1.72

expansion_tank = equipment.Expansion_tank("expansion tank", POWER, temp_T1_outside, temp_T2_outside, 4, 6)
print("расширительный бак")
print("объем системы при 3 л на кВт, м3 - ", round((POWER * 1163 * 3) * 0.001, 3))
print("3 л на кВт, расширительный бак объемом л - ", expansion_tank.tank_volume_manually(POWER * 1163 * 3))
print("---------------------------------------------")

print("подпитка")
refill_hours = 4
print("для заполения системы объемом м3 - ", round((POWER * 4), 3), " за ", refill_hours, " часов")
G_refill = round((POWER * 4), 3) / refill_hours
print("расход подпитки м3/ч - ", G_refill)

# G_refill = 10
# print("по замечанию / заданию Заказчика м3/ч - ", G_refill)

dn_refill = calc.pipeDn(G_refill, 1)
print("диаметр подпитки - ", dn_refill)
print("скорость в тр-де подпитки м/c- ", round(calc.pipev(G_refill, dn_refill), 3))
print("---------------------------------------------")

print("насосы сетевые")
G_pump = round(G_main_outside / 2, 3)
print("расход 1 сетевого насоса расчетный, т/ч - ", G_pump)

dn_pump = calc.pipeDn(G_pump, 1)
print("диаметр- ", dn_pump)
print("скорость, м/с - ", round(calc.pipev(G_pump, dn_pump), 3))
print("---------------------------------------------")

print("трубопроводы на котлах")
G_boiler_0 = round(1000 * Q_boiler_0 / (temp_T1_outside - temp_T2_outside), 3)
dn_boiler_0 = calc.pipeDn(G_boiler_0, 1.3)
print("для котла мощностью ", Q_boiler_0," расход т/ч - ", G_boiler_0 ,", dn - ", dn_boiler_0)
print("скорость в тр-де dn_boiler_0, м/с - ", round(calc.pipev(G_boiler_0, dn_boiler_0), 3))

G_boiler_2 = round(1000 * Q_boiler_2 / (temp_T1_outside - temp_T2_outside), 3)
dn_boiler_2 = calc.pipeDn(G_boiler_2, 1.3)
print("для котла мощностью ", Q_boiler_2," расход т/ч - ", G_boiler_2 ,", dn - ", dn_boiler_2)
print("скорость в тр-де dn_boiler_2, м/с - ", round(calc.pipev(G_boiler_2, dn_boiler_2), 3))
print("---------------------------------------------")

#рециркуляция общая 
print("рециркуляция")
print("рассматривается для режима 70-40, на входе в котел t >= 60")
Q_hot_water_summer = hot_water_power * ((temp_t3 - temp_w1_summer) / (temp_t3 - temp_w1_winter))
G_boiler_summer = 1000 * Q_hot_water_summer / (temp_T1_summer_in - temp_T2_summer_in)
G_main_summer = 1000 * Q_hot_water_summer / (temp_T1_summer_out - temp_T2_summer_out)
print("нагрузка летняя на ГВС Gcal/h - ", Q_hot_water_summer)
print("расход летний котловой воды, т/ч - ", G_boiler_summer)
print("расход летний сетевой воды, т/ч - ", G_main_summer)
temp_min_boiler = 60
G_circle_sum = abs(round(G_boiler_summer * (temp_T2_summer_out - temp_min_boiler) / (temp_T1_summer_in - temp_T2_summer_out), 3))
print("расход на циркуляцию общий, т/ч - ", G_circle_sum)

#разбивка на несколько котлов 

G_boiler_1_summer = 32.0
G_boiler_2_summer = 64.0

G_circle_1 = G_circle_sum * (G_boiler_1_summer / G_boiler_summer)
G_circle_2 = G_circle_sum - G_circle_1

print("расход через котел G_boiler_1_summer, т/ч - ", G_boiler_1_summer)
print("расход через котел G_boiler_2_summer, т/ч - ", G_boiler_2_summer)

#рециркуляция  
print("Циркуляция сети через 1 котел, т/ч - ", G_circle_1)
print("Циркуляция сети через 2 котел, т/ч - ", G_circle_2)

v_boiler_0_summer = round(calc.pipev(21.4, 125), 3)
v_boiler_1_summer = round(calc.pipev(10.6, 100), 3)
print("v_boiler_0_summer = ", v_boiler_0_summer)
print("v_boiler_1_summer = ", v_boiler_1_summer)



# v_summer = round(calc.pipev(32, 150), 3)
# print("------------ = ", v_summer)



dn_circle_1 = calc.pipeDn(G_circle_1, 1.2)
dn_circle_2 = calc.pipeDn(G_circle_2, 1.2)
print("диаметр рециркуляции dn_circle_1 ", dn_circle_1)
print("диаметр рециркуляции dn_circle_2 ", dn_circle_2)

v_circ_1 = round(calc.pipev(G_circle_1, dn_circle_1), 3)
v_circ_2 = round(calc.pipev(G_circle_2, dn_circle_2), 3)

print("v_circ_1 = ", v_circ_1)
print("v_circ_2 = ", v_circ_2)








# dn_circle = calc.pipeDn(G_circle_sum)
# print("диаметр- ", dn_circle)
# print("скорость в тр-де рециркуляции, м/с - ", round(calc.pipev(G_circle_sum, dn_circle), 3))
# print("---------------------------------------------")

# #рециркуляция на котел 3.5 МВт 
# G_circle_0_1 = round(0.3 * (1000 * Q_boiler_0 / (temp_T1_outside - temp_T2_outside)), 3)
# print("расход на циркуляцию для котла 3,5 МВт, т/ч - ", G_circle_0_1)
# dn_circle_0 = calc.pipeDn(G_circle_0_1)
# print("диаметр- ", dn_circle_0)
# print("скорость в тр-де рециркуляции, м/с - ", round(calc.pipev(G_circle_0_1, dn_circle_0), 3))

# print("---------------------------------------------")
# print("перемычка")
# #перемычка 
# G_bypass = G_main_2_summer
# dn_bypass = calc.pipeDn(G_bypass, 1.2)
# print("расход т/ч- ", G_bypass)
# print("диаметр- ", dn_bypass)
# print("скорость в перемычке, м/с - ", round(calc.pipev(G_bypass, dn_bypass), 3))



# n = input("press anything for exit")

def cold_water_input():

    # Ввод холодной воды для паровой и ИТП 
    # расход воды на паровую котельную 
    G_steam = 20.88
    #расход воды на ИТП 
    G_hp = 35.96

    dn = calc.pipeDn((G_hp + G_steam), 1.5)
    print("диаметр расчетный - ", dn)
    print("скорость в трубе Ду", dn, ", м/с - ", round(calc.pipev((G_hp + G_steam), dn), 3))
    print("скорость в трубе Ду80, м/с - ", round(calc.pipev(G_hp + G_steam, 80), 3))

    print("---------------------------------------------")
    dn = calc.pipeDn((20.88), 1.5)
    print("диаметр расчетный - ", dn)
    print("скорость в трубе ", dn, ", м/с - ", round(calc.pipev((G_steam), dn), 3))
    dn = calc.pipeDn((35.96), 1.5)
    print("диаметр расчетный - ", dn)
    print("скорость в трубе ", dn, ", м/с - ", round(calc.pipev((G_hp), dn), 3))
import source_data
import calc
import gas_in




print("heat_power, Gcal / h - ", source_data.heat_power)
print("vent_power, Gcal / h - ", source_data.vent_power)
print("hot_water_power_mid, Gcal / h - ", source_data.hot_water_power_mid)
print("hot_water_power_max, Gcal / h - ", source_data.hot_water_power_max)
print("POWER, Gcal / h - ", round(source_data.POWER_one, 3))
if (source_data.temp_T1_inside):
    print("temp_T1_inside - ", source_data.temp_T1_inside, ", temp_T2_inside - ", source_data.temp_T2_inside)
print("temp_T1_outside - ", source_data.temp_T1_outside, ", temp_T2_outside - ", source_data.temp_T2_outside)
print("---------------------------------------------")


G_main_outside = round(1000 * source_data.POWER_one / (source_data.temp_T1_outside - source_data.temp_T2_outside), 3)
print("расход расчетный сетевой контур, т/ч - ", G_main_outside)
dn_t1_outside = calc.pipeDn(G_main_outside, 1.2)
print("диаметр Т1 / Т2 сетевой контур- ", dn_t1_outside)
print("скорость Т1 / Т2, м/с - ", round(calc.pipev(G_main_outside, dn_t1_outside), 3))
print("---------------------------------------------")


S_boiler_room = source_data.wall_0 * source_data.wall_1 
V_boiler_room = round(source_data.wall_0 * source_data.wall_1 * source_data.height, 3)

print("Габариты помещения")
print("длина_0, м - ", source_data.wall_0, "; длина_1, м - ", source_data.wall_1, "; высота, м - ", source_data.height)
print("объем здания, м3 - ", V_boiler_room)

if source_data.BOILER_ROOM_TYPE.name == "SP_253":
    S_glass = gas_in.GAS_DROP_CONSTRUCT_COEF.SP_253.value * V_boiler_room
elif source_data.BOILER_ROOM_TYPE.name == "SP_373":
    S_glass = gas_in.GAS_DROP_CONSTRUCT_COEF.SP_373.value * V_boiler_room
else:
    S_glass = gas_in.GAS_DROP_CONSTRUCT_COEF.SP_89.value * V_boiler_room

print("площадь легксосбрасываемых конструкций, м2 - ", S_glass)
print("---------------------------------------------")



print("трубопроводы на котлах")
i=0
for boiler in source_data.Q_boilers:

    print("boiler - ", i)
    G_boiler = round(1000 * boiler / (source_data.temp_T1_outside - source_data.temp_T2_outside), 3)
    dn_boiler = calc.pipeDn(G_boiler, 1.3)
    print("для котла мощностью ", boiler," расход т/ч - ", G_boiler ,", dn - ", dn_boiler)
    print("скорость в тр-де dn_boiler_0, м/с - ", round(calc.pipev(G_boiler, dn_boiler), 3))
    i += 1 



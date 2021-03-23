import source_data
import calc
import gas_in
import vent



print("heat_power, Gcal / h - ", source_data.heat_power)
print("vent_power, Gcal / h - ", source_data.vent_power)
# print("hot_water_power_mid, Gcal / h - ", source_data.hot_water_power_mid)
print("hot_water_power_max, Gcal / h - ", source_data.hot_water_power_max)
print("POWER, Gcal / h - ", round(source_data.POWER_sum, 3))
if (source_data.temp_T1_inside):
    print("temp_T1_inside - ", source_data.temp_T1_inside, ", temp_T2_inside - ", source_data.temp_T2_inside)
print("temp_T1_outside - ", source_data.temp_T1_outside, ", temp_T2_outside - ", source_data.temp_T2_outside)
print("---------------------------------------------")


G_main_outside = round(1000 * source_data.POWER_sum / (source_data.temp_T1_outside - source_data.temp_T2_outside), 3)
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

#Gas ---------------------------------------

gas_1_1 = gas_in.Gas_subsystem(0.05)

print(gas_1_1.gas_pressure_class)
gas_1_1_cons = gas_1_1.gas_consumption_norm(source_data.Q_boilers, source_data.efficiency_boiler)

print("расход газа нм3/ч нормальный ", gas_1_1_cons)
gas_1_1_cons_work = gas_1_1.gas_consumption_work(gas_1_1_cons)
print("расход газа м3/ч рабочий", gas_1_1_cons_work)
print("dn  ", gas_1_1.gas_dn_pipe(gas_1_1_cons))
print("скорость ", gas_1_1.gas_velocity(gas_1_1_cons, gas_1_1.gas_dn_pipe(gas_1_1_cons)))

length = 8.
print("Dn_collector ", round(gas_1_1.gas_collector_dn(gas_1_1_cons_work, length), 5), "при длине в м. - ", length)

dn_gas_0_cons = gas_1_1.gas_consumption_norm_one(source_data.Q_boilers[0], source_data.efficiency_boiler)
dn_gas_0 = gas_1_1.gas_dn_pipe(dn_gas_0_cons)
dn_gas_0_vel = gas_1_1.gas_velocity(dn_gas_0_cons, dn_gas_0)

dn_gas_1_cons = gas_1_1.gas_consumption_norm_one(source_data.Q_boilers[1], source_data.efficiency_boiler)
dn_gas_1 = gas_1_1.gas_dn_pipe(dn_gas_1_cons)
dn_gas_1_vel = gas_1_1.gas_velocity(dn_gas_1_cons, dn_gas_1)

dn_gas_2_cons = gas_1_1.gas_consumption_norm_one(source_data.Q_boilers[2], source_data.efficiency_boiler)
dn_gas_2 = gas_1_1.gas_dn_pipe(dn_gas_2_cons)
dn_gas_2_vel = gas_1_1.gas_velocity(dn_gas_2_cons, dn_gas_2)


print("диаметр опуска газа для %f Гкал/ч - %i мм - скорость - %f" %(source_data.Q_boilers[0], dn_gas_0, dn_gas_0_vel))
print("диаметр опуска газа для %f Гкал/ч - %i мм - скорость - %f" %(source_data.Q_boilers[1], dn_gas_1, dn_gas_1_vel))
print("диаметр опуска газа для %f Гкал/ч - %i мм - скорость - %f" %(source_data.Q_boilers[2], dn_gas_2, dn_gas_2_vel))

#Vent --------------------------------------

vent_sys = vent.Vent()
print("Вентиляция-------------------------- ")
print("Площадь АИТ м2 ", vent_sys.S_boiler_room)
print("Общеобмен расход м3/ч ", vent_sys.general_exchange_vent())
print("На горение расход м3/ч ", vent_sys.G_air_for_fire())

vent_grill = vent.Vent_grill()
print("Решетка приточная м2 -  ", vent_grill.S_grill_sum(), " , при кол-ве - ", vent_grill.grill_number, " шт")

#Исходные данные ЖК Огни-2 
# Общая тепловая мощность Gcal/h
Qsum_twice = 7.004 

#Gcal / h
heat_power = 3.848
vent_power = 1.079
hot_water_power_mid = 1.302
hot_water_power_max = 1.907
POWER_sum = heat_power + vent_power + hot_water_power_max
POWER_one = POWER_sum / 2


Q_heat_loss = 8.0                #TODO
# temp_t3 = 65
# temp_w1_winter = 15
# temp_w1_summer = 14

#давление в теплосети в бар 
t1_pressure = 1.9
t2_pressure = 2

#расчетный режим
#котловой контур
temp_T1_inside = 0
temp_T2_inside =0
#сетевой контур
temp_T1_outside = 90
temp_T2_outside = 70

#летний режим
#котловой контур
temp_T1_summer_in = 0
temp_T2_summer_in = 0
#сетевой контур
temp_T1_summer_out = 90
temp_T2_summer_out = 70

#Мощность котлов - Gcal / h
# Q_boilers = [1.273, 1.114, 1.114]

Q_boilers = [1.079, 1.079, 0.943]

# Запрашиваемое топливо: природный газ по ГОСТ Р 5542-87 (8000 ккал/м3)

# Объем помещения 
wall_0 = 7.4                       #TODO
wall_1 = 10.9                       #TODO
height = 3.0                        #TODO

#temperature inside 
t_in = 5
#temperature outside 
t_out = -25

#теплоемкость воздуха с = ккал/(кг*С) 
thermal_capacity = 0.24
#плотность воздуха 1,293 кг/м3 
density = 1.293

n_grills = 1 #count of grills 
n_defl = 1 #count of deflectors

#расход газа часовой м3/ч
efficiency_boiler = 0.92
heating_value = 8000 

def gas_consution(list:Q_boilers, efficiency_boiler=0.92, heating_value=8000):

    #расчет расхода природного газа  
    G_gas = [i for i in range (0, len(Q_boilers))]
    for boiler in Q_boilers:
        G_gas.append(round(10 **6 * boiler / heating_value / efficiency_boiler, 3)) 
        # print("расход газа котел,", boiler,"  м3/ч - ", G_gas[-1])

    G_gas_sum = sum(i for i in G_gas)
    # print("расход газа сумма, м3/ч - ", G_gas_sum)

    return(G_gas_sum)

print(gas_consution(Q_boilers))
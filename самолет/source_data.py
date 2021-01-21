
#Исходные данные ГК Самолет 

#Gcal / h
heat_power = 5.77
vent_power = 0.244
hot_water_power = 1.152
POWER = heat_power + vent_power + hot_water_power

temp_t3 = 65
temp_w1_winter = 5
temp_w1_summer = 15

#давление в теплосети в бар 
t1_pressure = 6.0
t2_pressure = 4.0

#расчетный режим
#котловой контур
temp_T1_inside = 130
temp_T2_inside = 85
#сетевой контур
temp_T1_outside = 130
temp_T2_outside = 70

#летний режим
#котловой контур
temp_T1_summer_in = 100
temp_T2_summer_in = 60
#сетевой контур
temp_T1_summer_out = 70
temp_T2_summer_out = 40

#Мощность котлов - Gcal / h
Q_boilers = [3.009, 3.009, 1.72]

# Запрашиваемое топливо: природный газ по ГОСТ Р 5542-87 (8000 ккал/м3)

# Объем помещения 
wall_0 = 8.8
wall_1 = 11.0
height = 3.5

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


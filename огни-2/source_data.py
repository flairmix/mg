
from enum import Enum, auto

#Исходные данные ЖК Огни-2 

#тип котельной по нормативной документации 
class BOILER_ROOM_TYPE(Enum):
    Sp_89 = 'Sp_89'
    Sp_373 = 'Sp_373'
    Sp_253 = 'Sp_253'

BOILER_ROOM_TYPE = BOILER_ROOM_TYPE.Sp_253

#Gcal / h
heat_power = 3.908
vent_power = 0.886
hot_water_power_mid = 1.12
hot_water_power_max = 1.64

# Общая тепловая мощность Gcal/h
POWER_sum = heat_power + vent_power + hot_water_power_max

#Мощность одного 
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
Q_boilers = [1.273, 1.114, 1.114]

# Запрашиваемое топливо: природный газ по ГОСТ Р 5542-87 (8000 ккал/м3)

# Объем помещения 
wall_0 = 6.25                       #TODO
wall_1 = 9.75                      #TODO
height = 3.5                        #TODO

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





from enum import Enum, auto

#Исходные данные ЖК Огни-2 

C_AIR = 0.24   #ккал/(кг * K) - весовая теплоемкость воздуха ;
P_AIR = 1.293  #кг/м3 - плотность воздуха при нормальных условиях;


project_name = "Многофункциональная комплексная жилая застройка по адресу:\
г. Москва, ЗАО, район Раменки, между ул. Лобачевского и платформой «Матвеевское», квартал корпус 1,2"

#тип котельной по нормативной документации 
class BOILER_ROOM_TYPE(Enum):
    SP_89 = 'SP_89'
    SP_373 = 'SP_373'
    SP_253 = 'SP_253'

BOILER_ROOM_TYPE = BOILER_ROOM_TYPE.SP_253

#Gcal / h
heat_power = 0.935
vent_power = 0.913
# hot_water_power_mid = 1.12
hot_water_power_max = 0.979

power_boiler_room = 0.01 * (3.10)

# Общая тепловая мощность Gcal/h
POWER_sum = heat_power + vent_power + hot_water_power_max + power_boiler_room

#Мощность одного 
# POWER_one = POWER_sum / 2

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
# Q_boilers = [1.273431, 1.114359, 1.114359]
Q_boilers = [1.079, 1.079, 0.943]

# Запрашиваемое топливо: природный газ по ГОСТ Р 5542-87 (8000 ккал/м3)

# Объем помещения 
wall_0 = 11.27                       #TODO
wall_1 = 6.82                      #TODO
height = 3.9                        #TODO

#temperature inside 
t_in = 5
t_in_wc = 18
#temperature outside 
t_out = -25

#теплоемкость воздуха с = ккал/(кг*С) 
thermal_capacity = 0.24
#плотность воздуха 1,293 кг/м3 
density = 1.293

n_grills = 1 #count of grills 
n_defl = 1 #count of deflectors

#расход газа часовой м3/ч
efficiency_boiler = 0.926
heating_value = 8000 

gas_temperature = 298.15


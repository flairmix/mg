import equipment

power_21 = 2.96 #Gkal/h
power_22 = 3.5 #Gkal/h
power_23 = 3.5 #Gkal/h


exp_tank_21 = equipment.Expansion_tank('tank21', power_21, 90, 70, 6, 9)
exp_tank_22 = equipment.Expansion_tank('tank22', power_22, 90, 70, 6, 9)
exp_tank_23 = equipment.Expansion_tank('tank23', power_23, 90, 70, 6, 9)


print(exp_tank_21.tank_volume_manually(109+97+97+37+394))
print(exp_tank_21.tank_volume_manually(109+97+97+37+394))
print(exp_tank_23.tank_volume_manually(97+97+70+37+394))



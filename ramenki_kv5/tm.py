import equipment

power_1 = 2.857 #Gkal/h
power_2 = 2.857 #Gkal/h



exp_tank_1 = equipment.Expansion_tank('tank1', power_1, 90, 70, 6, 9)
# exp_tank_22 = equipment.Expansion_tank('tank22', power_22, 90, 70, 6, 9)
# exp_tank_23 = equipment.Expansion_tank('tank23', power_23, 90, 70, 6, 9)

#volume equipment and pipes 
volume_boiler_eco = [650, 750, 850, 950, 1050, 1150, 1300, 1450, 1600]
volume_boiler_eco = [53, 70, 75, 80, 85, 97, 109, 116, 123]

volume_of_system = volume_boiler_eco[6]+volume_boiler_eco[6]+volume_boiler_eco[5] + 1200 + 394

print(exp_tank_1.tank_volume_manually(volume_of_system))







import source_data

"""
hp - heating point
br - boiler room
ahss - Autonomous heat supply sources

"""

# Release of Blast Relief Panels
#СП 89.13330 п7.8
coef_BRP_br = 0.05
#СП 373.13330 п5.14
coef_BRP_ahss = 0.03 

#СП 253.13330 п6.9
coef_BRP_ahss_heigth = 0.05

# S_boiler_room = source_data.wall_0 * source_data.wall_1 
# V_boiler_room = round(source_data.wall_0 * source_data.wall_1 * source_data.height, 3)

# S_glass = coef_BRP_ahss * V_boiler_room


def gas_consution(list:source_data.Q_boilers, efficiency_boiler=0.92, heating_value=8000):
    """
    return gas consumption for list of boilers 
    Q_boiler - Gcal/h - boiler power 
    """
    #расчет расхода природного газа  
    G_gas = [i for i in range (0, len(source_data.Q_boilers))]
    for boiler in source_data.Q_boilers:
        G_gas.append(round(10 **6 * boiler / heating_value / efficiency_boiler, 3)) 
        # print("расход газа котел,", boiler,"  м3/ч - ", G_gas[-1])

    G_gas_sum = sum(i for i in G_gas)
    # print("расход газа сумма, м3/ч - ", G_gas_sum)

    return(G_gas_sum)


def gas_consution_one(Q_boiler, efficiency_boiler=0.92, heating_value=8000):
    """
    return gas consumption for one boiler 
    Q_boiler - Gcal/h - boiler power 
    """
    return round(10 **6 * Q_boiler / heating_value / efficiency_boiler, 3)



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

S_boiler_room = source_data.wall_0 * source_data.wall_1 
V_boiler_room = round(source_data.wall_0 * source_data.wall_1 * source_data.height, 3)

S_glass = coef_BRP_ahss * V_boiler_room

print(S_glass)
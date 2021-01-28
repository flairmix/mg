import source_data
import gas_in


class Vent():
    def __init__(self):

        self.S_boiler_room = source_data.wall_0 * source_data.wall_1 
        self.V_boiler_room = round(source_data.wall_0 * source_data.wall_1 * source_data.height, 3)

    def print_info(self):
        print("Вентиляция")
        print("Габариты помещения")
        print("длина_0, м - ", source_data.wall_0, "; длина_1, м - ", source_data.wall_1, "; высота, м - ", source_data.height)
        print("объем здания, м3 - ", self.V_boiler_room)

    def volume_without_eqp(self, coef=0.9):
        """объем помещения минус объем оборудования """ 
        return (self.V_boiler_room * coef)

    def general_exchange_vent(self, coef_exchange=3):
        """ Расход воздуха на общеобменный воздухообмен, м3ч  """
        return (self.V_boiler_room * coef_exchange)

    def G_air_for_fire(self):
        """ Расход воздуха на горение, м3ч  """
        return (gas_in.gas_consution(source_data.Q_boilers) * 1.2 * ((1.13 * source_data.heating_value) / 1000))

    def G_air_sum(self):
        """ Расход воздуха на горение и общеобмен, м3ч  """
        return (self.G_air_for_fire() + self.general_exchange_vent())


class Vent_grill(Vent):
    def __init__(self):
        super().__init__()
        
        self.grill_number = 1 
        self.v_grill = 1

    def S_grill_calc(self):
        """ Сечение приточной решетки расчетное, м2 """
        return (self.G_air_sum() / 3600 / self.v_grill)
        
    def S_grill_sum(self):
        """ Сечение приточной решетки живое, м2 """
        return (self.S_grill_calc() * 0.7)

    def S_grill(self):
        """ Сечение одной приточной решетки живое, м2 """
        return (self.S_grill_sum() / self.grill_number)



class Vent_deflector(Vent):
    def __init__(self):
        super().__init__()

        self.grill_number = 1 
        self.v_grill = 1

# print("приточная решетка ")
# # print("кратность воздухообмена - ", multiplicity)


# v_in = 1
# Sgrill = Gsum / 3600 / v_in
# print("сечение расчетное, м2 - ", round(Sgrill, 3))
# Coef_grill = 0.7
# Sgrill_fin = round((Sgrill / Coef_grill / source_data.n_grills), 3)
# print("площадь решетки общая, м2 - ", Sgrill_fin)

# width = round(1000 * (Sgrill_fin ** 0.5))

# while width % 50 != 0:
#     width += 1

# width = width / 1000
# height = width

# print("площадь решетки расчетная, м2 - ", Sgrill_fin, ", решетка - ", source_data.n_grills, " шт, " , width, "x", height, " = ", round((height * width), 3), " м2;")




vent = Vent()
print(vent.S_boiler_room)
print(vent.general_exchange_vent())
print(vent.G_air_for_fire())

vent_grill = Vent_grill()
print(vent_grill.S_boiler_room)

# # #объем помещения - объем оборудования 
# V_boiler_room = V_boiler_room * 0.9
# print("объем здания, с учетом оборудования, м3 - ", V_boiler_room)
# # расход воздуха на 3-х кр воздухообмен 
# Gv_3 = V_boiler_room * 3
# print("расход воздуха на 3-х кр воздухообмен, м3ч - ", Gv_3)

# # расход воздуха на горение 
# print(gas_in.gas_consution(source_data.Q_boilers))

# G_air_for_fire = gas_in.gas_consution(source_data.Q_boilers) * 1.2 * ((1.13 * source_data.heating_value) / 1000)
# print("расход воздуха на горение, м3ч - ", G_air_for_fire)

# # #расход воздуха всего 
# Gsum = Gv_3 + G_air_for_fire
# print("расход воздуха всего, м3ч - ", Gsum)

# # #площадь приточной решетки 

# print("----------------------")
# print("приточная решетка ")
# # print("кратность воздухообмена - ", multiplicity)


# v_in = 1
# Sgrill = Gsum / 3600 / v_in
# print("сечение расчетное, м2 - ", round(Sgrill, 3))
# Coef_grill = 0.7
# Sgrill_fin = round((Sgrill / Coef_grill / source_data.n_grills), 3)
# print("площадь решетки общая, м2 - ", Sgrill_fin)

# width = round(1000 * (Sgrill_fin ** 0.5))

# while width % 50 != 0:
#     width += 1

# width = width / 1000
# height = width

# print("площадь решетки расчетная, м2 - ", Sgrill_fin, ", решетка - ", source_data.n_grills, " шт, " , width, "x", height, " = ", round((height * width), 3), " м2;")

# print("----------------------")
# print("дефлекторы")

# #дефлекторы для котельной

# v_out = 1
# S_defl = Gv_3 / 3600 / v_out
# dn_defl_1 = round((4 * (S_defl / source_data.n_defl) / 3.14) ** 0.5, 3)
# print("сечение расчетное, м2 - ", S_defl)
# print("сечение расчетное для ", source_data.n_defl, "дефлекторов, м2 - ", S_defl / source_data.n_defl)
# print("диаметр 1 дефлектора, м, - ", dn_defl_1)

# print("----------------------")

# print("Количество теплоты для нагрева приточного воздуха")
# print("Q_air = Vприт * с * density * (tвн - tнар)")

# #ккал/ч
# Q_air_ccal_h = round(Gsum * source_data.thermal_capacity * source_data.density * (source_data.t_in + abs(source_data.t_out)), 3)
# Q_air_kW =  round((Q_air_ccal_h) / 1163, 3)
# print("Количество теплоты на нагрев воздуха #ккал/ч - ", Q_air_ccal_h)
# print("Количество теплоты на нагрев воздуха #кВт - ", Q_air_kW)
# print("----------------------")


# #теплопотери через огр конструкции, kW
# print("Теплопотери через ограждающие конструкции, кВт - ", source_data.Q_heat_loss)

# # тепловыделения 0,5 % от мощности 
# Q_heat_release = 0.005 * source_data.POWER_one * 1163
# print("Тепловыделения основного оборудования 0.5% POWER, кВт - ", Q_heat_release)

# Q_sum = source_data.Q_heat_loss + Q_air_kW - Q_heat_release
# print("Нагрузка на отопление расчетная суммарная, кВт - ", Q_sum)


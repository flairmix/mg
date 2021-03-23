import source_data
import vent

txt = open("heating_calc_output.txt", "w")

txt.write("Расчет отопления котельной\n")
txt.write("Объект: %s \n" %source_data.project_name)
txt.write("Исходные данные\n")


txt.write("V_(прит.общ.) = %f м3/ч - общее количество приточного воздуха;\n" %vent.vent.G_air_sum())
txt.write("c = %f ккал/(кг * K) - весовая теплоемкость воздуха;\n" %source_data.C_AIR)
txt.write("p = %f  кг/м3 - плотность воздуха при нормальных условиях;\n" %source_data.P_AIR)
txt.write("t_(вн) = + %i C - расчетная температура воздуха внутри помещения;\n" %source_data.t_in)
txt.write("t_(вн) = + %i C - расчетная температура воздуха в с/у;\n" %source_data.t_in_wc)
txt.write("t_(н.) = - %i C - расчетная температура наружного воздуха;\n" %source_data.t_out)
txt.write("a = 0.5 % - тепловое излучение от общей мощности работающих котлов;\n")
txt.write("Q = %i кВт - суммарная мощность котлов;\n" %(source_data.POWER_sum_23
 * 1163))

txt.write("Количество теплоты на нагрев приточного воздуха, поступающего в котельный зал, определяем по формуле:\n")
txt.write("Q_прит = %f\n" %(vent.vent.G_air_sum() * source_data.C_AIR * source_data.P_AIR * (source_data.t_in - source_data.t_out)))



txt.write("Количество тепловыделений от оборудования, установленного в помещении котельной, определяем по формуле:\n")
txt.write("Q_об = {power} * 0.005 = {result}\n".format(power=sum(source_data.Q_boilers) * 1163, result=sum(source_data.Q_boilers) * 1163 * 0.005))

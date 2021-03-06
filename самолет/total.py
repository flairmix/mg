import source_data

# Подраздел "Отопление, вентиляция и кондиционирование воздуха, тепловые сети"
# 19. Подраздел "Отопление, вентиляция и кондиционирование воздуха, тепловые сети" раздела 5 должен содержать:

# в текстовой части


a = """
    а) сведения о климатических и метеорологических условиях района строительства, расчетных параметрах наружного воздуха;
    "Климатические параметры приведены в соответствии с СП 131.13330.2018 «СНиП 23-01-99* «Строительная климатология».

    Наименование                                            Единица     Величина измерения
    Продолжительность отопительного периода                 дней        205
    Температура воздуха наиболее холодной пятидневки        гр.         0.92
    обеспеченностью 0,92
    Средняя температура воздуха периода со средней          гр.         -5,5
    суточной температурой ≤ 0 гр
    Средняя температура воздуха периода со средней          гр.         -2,2
    суточной температурой ≤ 8 гр (холодный период)
    Расчетная скорость ветра со средней суточной")          м/с         2,0
    температурой ≤ 8С (холодный период)
    Средняя максимальная температура воздуха наиболее       гр.         23.5
    теплого месяца
    Минимальная из средних скоростей ветра по румбам за     м/с         1,0
    июль (пункт 10, Таблица 10.1)
    Барометрическое давление                                гПа         997
    Географическая широта                                               55,8
"""

b = """
    б) сведения об источниках теплоснабжения, параметрах теплоносителей систем отопления и вентиляции

    Источником теплоснабжения для здания проектируемой водогрейной котельной является сетевой контур котельной. 
    Тепловая нагрузка на отопление и вентиляцию котельной %f МВт. Давление в подающем/ обратном трубопроводах %f / %f кг/см2, 
    расход теплоносителя (воды) %f м³/ч. 

    Температурный график при расчетном режиме - %i / %i °С.
    Регулирование – количественное (изменение скорости вращения электродвигателей)
""" %(source_data.POWER * 1.163, 
    source_data.t1_pressure,
    source_data.t2_pressure, 
    1000 * source_data.POWER / (source_data.temp_T1_outside - source_data.temp_T2_outside),
    source_data.temp_T1_outside,
    source_data.temp_T2_outside,
    )


print(b)

c = """
в) описание и обоснование способов прокладки и конструктивных решений, включая решения в отношении
диаметров и теплоизоляции труб теплотрассы от точки присоединения к сетям общего пользования до объекта капитального строительства;




"""

d = """ 
г) перечень мер по защите трубопроводов от агрессивного воздействия грунтов и грунтовых вод;


"""

# print("г) перечень мер по защите трубопроводов от агрессивного воздействия грунтов и грунтовых вод;")

# print("д) обоснование принятых систем и принципиальных решений по отоплению, вентиляции и кондиционированию воздуха помещений \
#     с приложением расчета совокупного выделения в воздух внутренней среды помещений химических веществ с учетом совместного \
#     использования строительных материалов, применяемых в проектируемом объекте капитального строительства, в соответствии \
    # с методикой, утверждаемой Министерством строительства и жилищно-коммунального хозяйства Российской Федерации;")
# (Подпункт в редакции, введенной в действие с 1 января 2018 года постановлением Правительства Российской Федерации от 28 января 2017 года N 95.


# д_1) обоснование энергетической эфективности конструктивных и инженерно-технических решений, используемых в системах отопления, вентиляции и кондиционирования воздуха помещений, тепловых сетях;
# (Подпункт дополнительно включен с 20 сентября 2017 года постановлением Правительства Российской Федерации от 8 сентября 2017 года N 1081)

# е) сведения о тепловых нагрузках на отопление, вентиляцию, горячее водоснабжение на производственные и другие нужды;

# е_1) описание мест расположения приборов учета используемой тепловой энергии и устройств сбора и передачи данных от таких приборов;
# (Подпункт дополнительно включен с 20 сентября 2017 года постановлением Правительства Российской Федерации от 8 сентября 2017 года N 1081)

# ж) сведения о потребности в паре;

# з) обоснование оптимальности размещения отопительного оборудования, характеристик материалов для изготовления воздуховодов;

# и) обоснование рациональности трассировки воздуховодов вентиляционных систем - для объектов производственного назначения;

# к) описание технических решений, обеспечивающих надежность работы систем в экстремальных условиях;

# л) описание систем автоматизации и диспетчеризации процесса регулирования отопления, вентиляции и кондиционирования воздуха;

# м) характеристика технологического оборудования, выделяющего вредные вещества - для объектов производственного назначения;

# н) обоснование выбранной системы очистки от газов и пыли - для объектов производственного назначения;

# о) перечень мероприятий по обеспечению эффективности работы систем вентиляции в аварийной ситуации (при необходимости);

# о_1) перечень мероприятий по обеспечению соблюдения установленных требований энергетической эффективности к устройствам, технологиям и материалам, используемым в системах отопления, вентиляции и кондиционирования воздуха помещений, тепловых сетях, позволяющих исключить нерациональный расход тепловой энергии, если такие требования предусмотрены в задании на проектирование;
# (Подпункт дополнительно включен с 20 сентября 2017 года постановлением Правительства Российской Федерации от 8 сентября 2017 года N 1081)


# в графической части


# п) принципиальные схемы систем отопления, вентиляции и кондиционирования воздуха;

# р) схему паропроводов (при наличии);

# с) схему холодоснабжения (при наличии);

# т) план сетей теплоснабжения.
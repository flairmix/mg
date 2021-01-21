import source_data
from samolet_vent import Q_air_kW

#теплопотери через огр конструкции, kW
Q_heat_loss = 21.241

print("Количество теплоты на нагрев воздуха #кВт - ", samolet_vent.Q_air_kW)

# тепловыделения 0,5 % от мощности 
Q_heat_release = 0.05 * source_data.POWER 



if __name__ == "__main__":
        
    print("Количество теплоты на нагрев воздуха #кВт - ", samolet_vent.Q_air_kW)
        
    print(Q_heat_release)


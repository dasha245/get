import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage = 3.22):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)

    plt.title('График зависимости напряжения на входе АЦП от времени')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.ylim(0, max_voltage*1.1)
    plt.grid()

    plt.show()

def plot_sampling_period_hits(time_values):
    sampling_periods = []
    for i in range(1, len(time_values)):
        period = time_values[i] - time_values[i-1]
        sampling_periods.append(period)

    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)

    plt.title('распределение периодов дискретизации измерений по времени на одно измерение')
    plt.xlabel('Период измерения, с')
    plt.ylabel('Количество измерений')

    plt.xlim(0, 0.06)
    plt.grid()
    plt.show()

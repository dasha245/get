import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time
from adc_plot import plot_sampling_period_hits


adc = R2R_ADC(3.22)
voltage_values = []
time_values = []
duration = 3.0


if __name__ == "__main__":
    
    try: 
        voltage_values = []
        time_values = []
        start = time.time()
        while(time.time() - start) < duration:
            voltage = adc.get_sar_voltage()
            voltage_values.append(voltage)
            current_time = time.time() - start
            time_values.append(current_time)
            time.sleep(0.001)
        plot_voltage_vs_time(time_values, voltage_values)
        plot_sampling_period_hits(time_values)

    finally:
        adc.deinit()
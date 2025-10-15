import pwm_dac as pd
import signsl_generator as sg

amplitude = 3.2
signsl_frequency = 10
sampling_frequency = 1000
a=0.0

if __name__ == "__main__":
    try:
        dac = pd.PWM_DAC(12, 500, 3.3, True)

        while True:
            voltage = sg.get_sin_wave(signsl_frequency, a)*amplitude
            dac.set_voltage(voltage)
            a += 1.0/sampling_frequency
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()
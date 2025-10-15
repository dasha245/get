import numpy as np
import time

def get_sin_wave(freq, time):
    sin1 = np.sin(2*np.pi*freq*time) + 1
    sin = sin1/2
    return sin

def wait_for_sampling_period(sampling_frequency):
    sampling_period = 1.0 / sampling_frequency
    time.sleep(sampling_period)
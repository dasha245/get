if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.22)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"Напряжение: {voltage:.3f} В")

    finally:
        adc.deinit()